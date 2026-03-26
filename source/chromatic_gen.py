# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import math
import random
import threading
from os.path import exists

import numpy as np
import parselmouth
import wx

import app_ui


# Musical constants
NOTES    = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
A4_MIDI  = 69
A4_HZ    = 440.0


# Helper functions - outside class for easier testing
def hz_to_midi(hz: float) -> float:
    """Convert frequency (Hz) to MIDI number (decimal)."""
    return A4_MIDI + 12.0 * math.log2(hz / A4_HZ)


def midi_to_note_octave(n: int) -> tuple:
    """Convert MIDI integer to (note_string, musical_octave)."""
    n = round(n)
    return NOTES[n % 12], (n // 12) - 1


def detect_file_pitch(filepath: str):
    """
    Analyze the middle 2 seconds of an audio file and return the median F0 in Hz.
    Returns None if no clear pitch is detected (percussion/noise).
    """
    try:
        snd = parselmouth.Sound(filepath)
        mid = snd.duration / 2.0
        seg = snd.extract_part(
            max(0.0, mid - 1.0),
            min(snd.duration, mid + 1.0),
            preserve_times=False
        )
        seg_mono = parselmouth.praat.call(seg, "Convert to mono")
        pitch    = parselmouth.praat.call(seg_mono, "To Pitch", 0.0, 50.0, 1500.0)
        n_frames = parselmouth.praat.call(pitch, "Get number of frames")

        voiced = []
        for i in range(1, n_frames + 1):
            f = parselmouth.praat.call(pitch, "Get value in frame", i, "Hertz")
            if f is not None and f > 0 and not math.isnan(f):
                voiced.append(f)

        return float(np.median(voiced)) if voiced else None
    except Exception:
        return None


class GeneratorGUI(app_ui.AppFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self._busy               = False
        self._status_idle_colour = wx.Colour(80, 90, 120)

    # Shared tools (thread-safe)
    def _lock(self):
        """Disable UI buttons during processing."""
        self._busy = True
        wx.CallAfter(self.chromGenerate.Enable, False)
        wx.CallAfter(self.autoDetectBtn.Enable, False)

    def _unlock(self):
        """Re-enable buttons after processing completes."""
        self._busy = False
        wx.CallAfter(self.chromGenerate.Enable, True)
        wx.CallAfter(self.autoDetectBtn.Enable, True)

    def _set_status(self, text: str, colour: wx.Colour = None):
        """Update status text from any thread safely."""
        c = colour or self._status_idle_colour
        wx.CallAfter(self.statusLabel.SetLabel, text)
        wx.CallAfter(self.statusLabel.SetForegroundColour, c)

    def _set_progress(self, value: int):
        """Update progress bar from any thread safely (0-100)."""
        wx.CallAfter(self.progressGauge.SetValue, max(0, min(100, int(value))))

    # Feature 1: Auto Pitch Detection
    def auto_detect(self, event):
        if self._busy:
            return

        sample_path = self.dirPicker.GetPath()
        if not os.path.isdir(sample_path):
            wx.MessageBox("Please select a valid sample folder first.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return

        # Collect files 1.wav, 2.wav, ... automatically
        files, i = [], 1
        while exists(os.path.join(sample_path, f"{i}.wav")):
            files.append(os.path.join(sample_path, f"{i}.wav"))
            i += 1

        if not files:
            wx.MessageBox("No audio files found (1.wav, 2.wav ...) in selected folder.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return

        self._lock()
        self.detectedPitchLabel.SetLabel("Analysing...")
        self.detectedPitchLabel.SetForegroundColour(wx.Colour(150, 160, 180))
        self._set_progress(0)
        self._set_status("Detecting pitch...")

        threading.Thread(
            target=self._detect_worker, args=(files,), daemon=True
        ).start()

    def _detect_worker(self, files: list):
        """Background thread worker - analyze up to 8 files."""
        analyze = files[:8]
        freqs   = []
        for idx, fp in enumerate(analyze):
            self._set_progress(int((idx + 1) / len(analyze) * 100))
            f = detect_file_pitch(fp)
            if f is not None:
                freqs.append(f)

        wx.CallAfter(self._detect_finish, freqs)

    def _detect_finish(self, freqs: list):
        self._unlock()
        self._set_progress(0)

        if not freqs:
            self.detectedPitchLabel.SetLabel("No pitched content detected")
            self.detectedPitchLabel.SetForegroundColour(wx.Colour(220, 100, 80))
            self._set_status("Detection failed - try a melodic sample")
            return

        median_hz           = float(np.median(freqs))
        midi_f              = hz_to_midi(median_hz)
        midi_i              = round(midi_f)
        cents_off           = round((midi_f - midi_i) * 100)
        note_str, music_oct = midi_to_note_octave(midi_i)

        # Set Note choice
        self.startNoteChoice.SetSelection(NOTES.index(note_str))

        # Set Octave choice
        # Mapping: UI octave n produces musical octave (n+1)
        # Therefore: selection_index = musical_octave - 2
        sel = max(0, min(3, music_oct - 2))
        self.startOctaveChoice.SetSelection(sel)

        cents_str = f"+{cents_off} cents" if cents_off >= 0 else f"{cents_off} cents"
        self.detectedPitchLabel.SetLabel(
            f"Detected: {note_str}{music_oct}  {median_hz:.1f} Hz  ({cents_str})"
        )
        self.detectedPitchLabel.SetForegroundColour(wx.Colour(100, 210, 140))
        self._set_status(f"Pitch detected: {note_str}{music_oct}")
        self.mainPanel.Layout()

    # Feature 2 & 3: Generate (with Normalize and Progress)
    def generate_chromatic(self, event):
        if self._busy:
            return

        sample_path = self.dirPicker.GetPath()
        if not os.path.isdir(sample_path):
            wx.MessageBox("Please select a valid sample folder first.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return

        self._lock()
        self._set_progress(0)
        self._set_status("Generating...")

        params = {
            "sample_path"    : sample_path,
            "gap"            : float(self.gapInput.GetValue()),
            "semitones"      : int(self.rangeInput.GetValue()),
            "pitched"        : self.pitchedCheck.IsChecked(),
            "dump_samples"   : self.samplesCheck.IsChecked(),
            "shuffle"        : self.sampleShuffleCheck.IsChecked(),
            "normalize"      : self.normalizeCheck.IsChecked(),
            "selected_octave": self.startOctaveChoice.GetSelection() + 1,
            "note_selection" : self.startNoteChoice.GetSelection(),
        }

        threading.Thread(
            target=self._generate_worker, args=(params,), daemon=True
        ).start()

    def _generate_worker(self, p: dict):
        try:
            result = self._run_generation(p)
            wx.CallAfter(self._generate_finish, None, result)
        except Exception as err:
            wx.CallAfter(self._generate_finish, str(err), None)

    def _generate_finish(self, error, result):
        self._unlock()
        if error:
            self._set_progress(0)
            self._set_status(f"Error: {error}", wx.Colour(220, 80, 60))
            wx.MessageBox(str(error), "Generation failed", wx.OK | wx.ICON_ERROR)
        else:
            self._set_progress(100)
            self._set_status(f"Done - {result}", wx.Colour(80, 200, 120))

    def _run_generation(self, p: dict) -> str:
        """Core logic - runs in background thread."""
        sample_path  = p["sample_path"]
        semitones    = p["semitones"]
        starting_key = p["note_selection"] + 12 * p["selected_octave"]
        do_pitch     = p["pitched"]
        do_normalize = p["normalize"]

        # Collect sample files
        file_index, i = 0, 1
        while exists(os.path.join(sample_path, f"{i}.wav")):
            file_index += 1
            i += 1

        if file_index == 0:
            raise RuntimeError("No audio files (1.wav, 2.wav ...) found.")

        # Build sample list
        base_list   = list(range(1, file_index + 1))
        sample_list = []
        while len(sample_list) < semitones:
            cycle = base_list.copy()
            if p["shuffle"]:
                random.shuffle(cycle)
            sample_list.extend(cycle)
        sample_list = sample_list[:semitones]

        # Create silent gap sound
        sample_gap = parselmouth.praat.call(
            "Create Sound from formula", "Gap", 1, 0, p["gap"], 48000, "0"
        )

        pitched_sounds        = []
        spaced_pitched_sounds = []

        # Process note by note
        for i in range(semitones):
            self._set_progress(int((i + 1) / semitones * 93))

            fp       = os.path.join(sample_path, f"{sample_list[i]}.wav")
            snd_rs   = parselmouth.praat.call(parselmouth.Sound(fp), "Resample", 48000, 1)
            snd_mono = parselmouth.praat.call(snd_rs, "Convert to mono")

            if do_pitch:
                manip      = parselmouth.praat.call(snd_mono, "To Manipulation", 0.05, 60, 600)
                pitch_tier = parselmouth.praat.call(manip, "Extract pitch tier")
                target_hz  = 32.703 * (2 ** ((i + starting_key) / 12))
                parselmouth.praat.call(pitch_tier, "Formula", f"{target_hz}")
                parselmouth.praat.call([pitch_tier, manip], "Replace pitch tier")
                out_snd = parselmouth.praat.call(manip, "Get resynthesis (overlap-add)")
            else:
                out_snd = snd_mono

            # Normalize each sample individually before combining
            if do_normalize:
                parselmouth.praat.call(out_snd, "Scale peak", 0.99)

            pitched_sounds.append(out_snd)
            spaced_pitched_sounds.append(out_snd)
            spaced_pitched_sounds.append(sample_gap)

        # Combine and final normalize
        self._set_progress(95)
        chromatic = parselmouth.Sound.concatenate(spaced_pitched_sounds)

        if do_normalize:
            parselmouth.praat.call(chromatic, "Scale peak", 0.99)

        out_path = os.path.join(sample_path, "chromatic.wav")
        chromatic.save(out_path, "WAV")

        # Save individual pitched samples if requested
        if p["dump_samples"] and do_pitch:
            dump_dir = os.path.join(sample_path, "pitched_samples")
            os.makedirs(dump_dir, exist_ok=True)
            for idx, snd in enumerate(pitched_sounds):
                snd.save(os.path.join(dump_dir, f"pitched_{idx + 1}.wav"), "WAV")

        return out_path


# Entry Point
if __name__ == "__main__":
    app   = wx.App(False)
    frame = GeneratorGUI(None)
    frame.Show(True)
    app.MainLoop()