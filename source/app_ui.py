# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
# Features: Auto Detect · Normalize · Progress Bar

import wx
import wx.xrc


class AppFrame(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Chromatic Scale Generator",
		                    pos=wx.DefaultPosition, size=wx.Size(650, 660),
		                    style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size(650, 660), wx.DefaultSize)

		# Theme colors
		bgColour          = wx.Colour(18,  18,  24)
		panelBgColour     = wx.Colour(26,  26,  36)
		titleColour       = wx.Colour(100, 160, 255)
		textColour        = wx.Colour(210, 215, 230)
		labelColour       = wx.Colour(140, 155, 185)
		btnColour         = wx.Colour(35,  110, 230)
		btnHoverColour    = wx.Colour(55,  130, 245)
		btnTextColour     = wx.Colour(255, 255, 255)
		detectBtnColour   = wx.Colour(25,  75,  140)
		detectHoverColour = wx.Colour(40,  100, 175)
		inputBgColour     = wx.Colour(35,  35,  50)
		inputTextColour   = wx.Colour(230, 235, 245)
		separatorColour   = wx.Colour(45,  48,  65)
		checkColour       = wx.Colour(180, 190, 210)

		self.SetBackgroundColour(bgColour)
		self.SetForegroundColour(textColour)

		# Main sizer
		outerSizer = wx.BoxSizer(wx.VERTICAL)
		outerSizer.Add((0, 8), 0, 0, 0)

		self.mainPanel = wx.Panel(self, wx.ID_ANY)
		self.mainPanel.SetBackgroundColour(panelBgColour)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add((0, 10), 0, 0, 0)

		# Title section
		titleSizer = wx.BoxSizer(wx.HORIZONTAL)
		titleSizer.Add((0, 0), 1, wx.EXPAND, 5)
		self.titleLabel = wx.StaticText(self.mainPanel, wx.ID_ANY, "Chromatic Scale Generator")
		self.titleLabel.Wrap(-1)
		self.titleLabel.SetFont(wx.Font(22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.titleLabel.SetForegroundColour(titleColour)
		titleSizer.Add(self.titleLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		titleSizer.Add((0, 0), 1, wx.EXPAND, 5)
		mainSizer.Add(titleSizer, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)

		# Description section
		descSizer = wx.BoxSizer(wx.HORIZONTAL)
		descSizer.Add((0, 0), 1, wx.EXPAND, 0)
		self.descLabel = wx.StaticText(self.mainPanel, wx.ID_ANY,
		                                "Generate chromatic scales from your audio samples")
		self.descLabel.Wrap(-1)
		self.descLabel.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL))
		self.descLabel.SetForegroundColour(wx.Colour(100, 110, 140))
		descSizer.Add(self.descLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		descSizer.Add((0, 0), 1, wx.EXPAND, 0)
		mainSizer.Add(descSizer, 0, wx.EXPAND | wx.BOTTOM, 5)

		# Separator 1
		self.separator1 = wx.StaticLine(self.mainPanel, wx.ID_ANY)
		self.separator1.SetBackgroundColour(separatorColour)
		mainSizer.Add(self.separator1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 15)

		# Sample folder section
		dirSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.dirText = wx.StaticText(self.mainPanel, wx.ID_ANY, "Sample folder:")
		self.dirText.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.dirText.SetForegroundColour(labelColour)
		dirSizer.Add(self.dirText, 0, wx.ALIGN_CENTER | wx.ALL, 6)
		self.dirPicker = wx.DirPickerCtrl(self.mainPanel, wx.ID_ANY, wx.EmptyString,
		                                   "Select a folder", wx.DefaultPosition,
		                                   wx.Size(350, -1), wx.DIRP_DEFAULT_STYLE)
		dirSizer.Add(self.dirPicker, 1, wx.ALIGN_CENTER | wx.ALL, 6)
		mainSizer.Add(dirSizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

		# Starting note and octave section
		noteOctaveSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.startNoteText = wx.StaticText(self.mainPanel, wx.ID_ANY, "Starting note:")
		self.startNoteText.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.startNoteText.SetForegroundColour(labelColour)
		noteOctaveSizer.Add(self.startNoteText, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		noteChoices = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
		self.startNoteChoice = wx.Choice(self.mainPanel, wx.ID_ANY, wx.DefaultPosition,
		                                  wx.Size(70, -1), noteChoices, 0)
		self.startNoteChoice.SetSelection(0)
		self.startNoteChoice.SetBackgroundColour(inputBgColour)
		self.startNoteChoice.SetForegroundColour(inputTextColour)
		noteOctaveSizer.Add(self.startNoteChoice, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		noteOctaveSizer.Add((20, 0), 0, 0, 0)

		self.startOctaveText = wx.StaticText(self.mainPanel, wx.ID_ANY, "Octave:")
		self.startOctaveText.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.startOctaveText.SetForegroundColour(labelColour)
		noteOctaveSizer.Add(self.startOctaveText, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		octaveChoices = ["1", "2", "3", "4"]
		self.startOctaveChoice = wx.Choice(self.mainPanel, wx.ID_ANY, wx.DefaultPosition,
		                                    wx.Size(60, -1), octaveChoices, 0)
		self.startOctaveChoice.SetSelection(0)
		self.startOctaveChoice.SetBackgroundColour(inputBgColour)
		self.startOctaveChoice.SetForegroundColour(inputTextColour)
		noteOctaveSizer.Add(self.startOctaveChoice, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		mainSizer.Add(noteOctaveSizer, 0, wx.LEFT | wx.RIGHT, 10)

		# Auto Detect Pitch section
		autoDetectSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.autoDetectBtn = wx.Button(self.mainPanel, wx.ID_ANY, "   Auto Detect Pitch",
		                                wx.DefaultPosition, wx.Size(170, 30), 0)
		self.autoDetectBtn.SetBackgroundColour(detectBtnColour)
		self.autoDetectBtn.SetForegroundColour(btnTextColour)
		self.autoDetectBtn.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.autoDetectBtn.SetCursor(wx.Cursor(wx.CURSOR_HAND))
		autoDetectSizer.Add(self.autoDetectBtn, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		self.detectedPitchLabel = wx.StaticText(self.mainPanel, wx.ID_ANY, "",
		                                          wx.DefaultPosition, wx.Size(240, -1), 0)
		self.detectedPitchLabel.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.detectedPitchLabel.SetForegroundColour(wx.Colour(100, 200, 130))
		autoDetectSizer.Add(self.detectedPitchLabel, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		mainSizer.Add(autoDetectSizer, 0, wx.LEFT | wx.RIGHT, 10)

		# Range and Gap section
		rangeGapSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.rangeText = wx.StaticText(self.mainPanel, wx.ID_ANY, "   Range:")
		self.rangeText.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.rangeText.SetForegroundColour(labelColour)
		rangeGapSizer.Add(self.rangeText, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		self.rangeInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "48", wx.DefaultPosition, wx.Size(60, -1), 0)
		self.rangeInput.SetBackgroundColour(inputBgColour)
		self.rangeInput.SetForegroundColour(inputTextColour)
		rangeGapSizer.Add(self.rangeInput, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		rangeGapSizer.Add((20, 0), 0, 0, 0)

		self.gapText = wx.StaticText(self.mainPanel, wx.ID_ANY, "   Gap (sec):")
		self.gapText.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.gapText.SetForegroundColour(labelColour)
		rangeGapSizer.Add(self.gapText, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		self.gapInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "0.3", wx.DefaultPosition, wx.Size(60, -1), 0)
		self.gapInput.SetBackgroundColour(inputBgColour)
		self.gapInput.SetForegroundColour(inputTextColour)
		rangeGapSizer.Add(self.gapInput, 0, wx.ALIGN_CENTER | wx.ALL, 6)

		mainSizer.Add(rangeGapSizer, 0, wx.LEFT | wx.RIGHT, 10)
		mainSizer.Add((0, 5), 0, 0, 0)

		# Separator 2
		self.separator2 = wx.StaticLine(self.mainPanel, wx.ID_ANY)
		self.separator2.SetBackgroundColour(separatorColour)
		mainSizer.Add(self.separator2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, 15)

		# Checkboxes - Row 1
		checkRow1 = wx.BoxSizer(wx.HORIZONTAL)

		self.pitchedCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "  Pitched")
		self.pitchedCheck.SetValue(True)
		self.pitchedCheck.SetForegroundColour(checkColour)
		self.pitchedCheck.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		checkRow1.Add(self.pitchedCheck, 0, wx.ALIGN_CENTER | wx.ALL, 8)

		checkRow1.Add((30, 0), 0, 0, 0)

		self.samplesCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "  Dump individual pitched samples")
		self.samplesCheck.SetValue(True)
		self.samplesCheck.SetForegroundColour(checkColour)
		self.samplesCheck.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		checkRow1.Add(self.samplesCheck, 0, wx.ALIGN_CENTER | wx.ALL, 8)

		mainSizer.Add(checkRow1, 0, wx.LEFT | wx.RIGHT, 10)

		# Checkboxes - Row 2
		checkRow2 = wx.BoxSizer(wx.HORIZONTAL)

		self.sampleShuffleCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "  Random samples")
		self.sampleShuffleCheck.SetValue(False)
		self.sampleShuffleCheck.SetForegroundColour(checkColour)
		self.sampleShuffleCheck.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		checkRow2.Add(self.sampleShuffleCheck, 0, wx.ALIGN_CENTER | wx.ALL, 8)

		checkRow2.Add((30, 0), 0, 0, 0)

		# Normalize Checkbox
		self.normalizeCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "  Normalize amplitude")
		self.normalizeCheck.SetValue(True)
		self.normalizeCheck.SetForegroundColour(checkColour)
		self.normalizeCheck.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		checkRow2.Add(self.normalizeCheck, 0, wx.ALIGN_CENTER | wx.ALL, 8)

		mainSizer.Add(checkRow2, 0, wx.LEFT | wx.RIGHT, 10)
		mainSizer.Add((0, 12), 0, 0, 0)

		# Progress Bar
		self.progressGauge = wx.Gauge(self.mainPanel, wx.ID_ANY, 100,
		                               wx.DefaultPosition, wx.Size(-1, 10),
		                               wx.GA_HORIZONTAL | wx.GA_SMOOTH)
		self.progressGauge.SetValue(0)
		mainSizer.Add(self.progressGauge, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 15)

		# Generate Button
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)
		btnSizer.Add((0, 0), 1, wx.EXPAND, 0)

		self.chromGenerate = wx.Button(self.mainPanel, wx.ID_ANY, "   Generate Chromatic",
		                                wx.DefaultPosition, wx.Size(250, 45), 0)
		self.chromGenerate.SetBackgroundColour(btnColour)
		self.chromGenerate.SetForegroundColour(btnTextColour)
		self.chromGenerate.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.chromGenerate.SetCursor(wx.Cursor(wx.CURSOR_HAND))
		btnSizer.Add(self.chromGenerate, 0, wx.ALL, 5)

		btnSizer.Add((0, 0), 1, wx.EXPAND, 0)
		mainSizer.Add(btnSizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

		# Separator 3
		self.separator3 = wx.StaticLine(self.mainPanel, wx.ID_ANY)
		self.separator3.SetBackgroundColour(separatorColour)
		mainSizer.Add(self.separator3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

		# Status Bar
		statusSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.statusLabel = wx.StaticText(self.mainPanel, wx.ID_ANY, "Ready")
		self.statusLabel.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.statusLabel.SetForegroundColour(wx.Colour(80, 90, 120))
		statusSizer.Add(self.statusLabel, 0, wx.ALL, 8)
		statusSizer.Add((0, 0), 1, wx.EXPAND, 0)

		self.versionLabel = wx.StaticText(self.mainPanel, wx.ID_ANY, "v1.5")
		self.versionLabel.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		self.versionLabel.SetForegroundColour(wx.Colour(60, 65, 85))
		statusSizer.Add(self.versionLabel, 0, wx.ALL, 8)

		mainSizer.Add(statusSizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

		self.mainPanel.SetSizer(mainSizer)
		self.mainPanel.Layout()
		outerSizer.Add(self.mainPanel, 1, wx.EXPAND | wx.ALL, 12)
		self.SetSizer(outerSizer)
		self.Layout()
		self.Centre(wx.BOTH)

		# Bind events
		self.chromGenerate.Bind(wx.EVT_BUTTON, self.generate_chromatic)
		self.autoDetectBtn.Bind(wx.EVT_BUTTON, self.auto_detect)

		self.chromGenerate.Bind(wx.EVT_ENTER_WINDOW,
			lambda e: self.chromGenerate.SetBackgroundColour(btnHoverColour) or self.chromGenerate.Refresh())
		self.chromGenerate.Bind(wx.EVT_LEAVE_WINDOW,
			lambda e: self.chromGenerate.SetBackgroundColour(btnColour) or self.chromGenerate.Refresh())

		self.autoDetectBtn.Bind(wx.EVT_ENTER_WINDOW,
			lambda e: self.autoDetectBtn.SetBackgroundColour(detectHoverColour) or self.autoDetectBtn.Refresh())
		self.autoDetectBtn.Bind(wx.EVT_LEAVE_WINDOW,
			lambda e: self.autoDetectBtn.SetBackgroundColour(detectBtnColour) or self.autoDetectBtn.Refresh())

	def __del__(self):
		pass

	# Virtual handlers - override in derived class
	def generate_chromatic(self, event):
		event.Skip()

	def auto_detect(self, event):
		event.Skip()