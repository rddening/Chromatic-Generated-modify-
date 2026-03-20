#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chromatic Scale Generator", pos = wx.DefaultPosition, size = wx.Size( 650, 560 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 650, 560 ), wx.DefaultSize )

		# ===== ألوان الثيم =====
		bgColour = wx.Colour( 18, 18, 24 )              # خلفية سوداء مائلة للأزرق
		panelBgColour = wx.Colour( 26, 26, 36 )          # خلفية اللوحة الداخلية
		titleColour = wx.Colour( 100, 160, 255 )         # لون العنوان أزرق فاتح
		textColour = wx.Colour( 210, 215, 230 )          # نص رمادي فاتح
		labelColour = wx.Colour( 140, 155, 185 )         # نص التسميات
		btnColour = wx.Colour( 35, 110, 230 )            # أزرار زرقاء
		btnHoverColour = wx.Colour( 55, 130, 245 )       # لون الزر عند التمرير
		btnTextColour = wx.Colour( 255, 255, 255 )       # نص الأزرار أبيض
		inputBgColour = wx.Colour( 35, 35, 50 )          # خلفية الحقول
		inputTextColour = wx.Colour( 230, 235, 245 )     # نص الحقول
		inputBorderColour = wx.Colour( 60, 65, 90 )      # حدود الحقول
		accentColour = wx.Colour( 80, 140, 255 )         # لون التمييز
		separatorColour = wx.Colour( 45, 48, 65 )        # لون الفاصل
		checkColour = wx.Colour( 180, 190, 210 )         # لون النص في الـ checkboxes

		self.SetBackgroundColour( bgColour )
		self.SetForegroundColour( textColour )

		# ===== السايزر الرئيسي =====
		outerSizer = wx.BoxSizer( wx.VERTICAL )
		outerSizer.Add( ( 0, 8 ), 0, 0, 0 )

		# ===== لوحة داخلية مع حواف مدورة =====
		self.mainPanel = wx.Panel( self, wx.ID_ANY )
		self.mainPanel.SetBackgroundColour( panelBgColour )

		mainSizer = wx.BoxSizer( wx.VERTICAL )
		mainSizer.Add( ( 0, 10 ), 0, 0, 0 )

		# ===== العنوان =====
		titleSizer = wx.BoxSizer( wx.HORIZONTAL )
		titleSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 5 )

		self.titleLabel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Chromatic Scale Generator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titleLabel.Wrap( -1 )
		self.titleLabel.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.titleLabel.SetForegroundColour( titleColour )
		titleSizer.Add( self.titleLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		titleSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 5 )
		mainSizer.Add( titleSizer, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 8 )

		# ===== وصف بسيط =====
		descSizer = wx.BoxSizer( wx.HORIZONTAL )
		descSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 0 )
		self.descLabel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Generate chromatic scales from your audio samples", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.descLabel.Wrap( -1 )
		self.descLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.descLabel.SetForegroundColour( wx.Colour( 100, 110, 140 ) )
		descSizer.Add( self.descLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		descSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 0 )
		mainSizer.Add( descSizer, 0, wx.EXPAND|wx.BOTTOM, 5 )

		# ===== فاصل =====
		self.separator1 = wx.StaticLine( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.separator1.SetBackgroundColour( separatorColour )
		self.separator1.SetForegroundColour( separatorColour )
		mainSizer.Add( self.separator1, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 15 )

		# ===== Sample folder =====
		dirSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.dirText = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Sample folder:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dirText.Wrap( -1 )
		self.dirText.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dirText.SetForegroundColour( labelColour )
		dirSizer.Add( self.dirText, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		self.dirPicker = wx.DirPickerCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 350, -1 ), wx.DIRP_DEFAULT_STYLE )
		dirSizer.Add( self.dirPicker, 1, wx.ALIGN_CENTER|wx.ALL, 6 )

		mainSizer.Add( dirSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10 )

		# ===== Starting note & octave في سطر واحد =====
		noteOctaveSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.startNoteText = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Starting note:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startNoteText.Wrap( -1 )
		self.startNoteText.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.startNoteText.SetForegroundColour( labelColour )
		noteOctaveSizer.Add( self.startNoteText, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		startNoteChoiceChoices = [ u"C", u"C#", u"D", u"D#", u"E", u"F", u"F#", u"G", u"G#", u"A", u"A#", u"B" ]
		self.startNoteChoice = wx.Choice( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70, -1 ), startNoteChoiceChoices, 0 )
		self.startNoteChoice.SetSelection( 0 )
		self.startNoteChoice.SetBackgroundColour( inputBgColour )
		self.startNoteChoice.SetForegroundColour( inputTextColour )
		noteOctaveSizer.Add( self.startNoteChoice, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		noteOctaveSizer.Add( ( 20, 0 ), 0, 0, 0 )

		self.startOctaveText = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Octave:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startOctaveText.Wrap( -1 )
		self.startOctaveText.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.startOctaveText.SetForegroundColour( labelColour )
		noteOctaveSizer.Add( self.startOctaveText, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		startOctaveChoiceChoices = [ u"1", u"2", u"3", u"4" ]
		self.startOctaveChoice = wx.Choice( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60, -1 ), startOctaveChoiceChoices, 0 )
		self.startOctaveChoice.SetSelection( 0 )
		self.startOctaveChoice.SetBackgroundColour( inputBgColour )
		self.startOctaveChoice.SetForegroundColour( inputTextColour )
		noteOctaveSizer.Add( self.startOctaveChoice, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		mainSizer.Add( noteOctaveSizer, 0, wx.LEFT|wx.RIGHT, 10 )

		# ===== Range & Gap في سطر واحد =====
		rangeGapSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.rangeText = wx.StaticText( self.mainPanel, wx.ID_ANY, u"📏  Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rangeText.Wrap( -1 )
		self.rangeText.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.rangeText.SetForegroundColour( labelColour )
		rangeGapSizer.Add( self.rangeText, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		self.rangeInput = wx.TextCtrl( self.mainPanel, wx.ID_ANY, u"24", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
		self.rangeInput.SetBackgroundColour( inputBgColour )
		self.rangeInput.SetForegroundColour( inputTextColour )
		rangeGapSizer.Add( self.rangeInput, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		rangeGapSizer.Add( ( 20, 0 ), 0, 0, 0 )

		self.gapText = wx.StaticText( self.mainPanel, wx.ID_ANY, u"⏱  Gap (sec):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gapText.Wrap( -1 )
		self.gapText.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.gapText.SetForegroundColour( labelColour )
		rangeGapSizer.Add( self.gapText, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		self.gapInput = wx.TextCtrl( self.mainPanel, wx.ID_ANY, u"0.1", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
		self.gapInput.SetBackgroundColour( inputBgColour )
		self.gapInput.SetForegroundColour( inputTextColour )
		rangeGapSizer.Add( self.gapInput, 0, wx.ALIGN_CENTER|wx.ALL, 6 )

		mainSizer.Add( rangeGapSizer, 0, wx.LEFT|wx.RIGHT, 10 )

		mainSizer.Add( ( 0, 5 ), 0, 0, 0 )

		# ===== فاصل =====
		self.separator2 = wx.StaticLine( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.separator2.SetBackgroundColour( separatorColour )
		self.separator2.SetForegroundColour( separatorColour )
		mainSizer.Add( self.separator2, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, 15 )

		# ===== Checkboxes =====
		checkSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.pitchedCheck = wx.CheckBox( self.mainPanel, wx.ID_ANY, u"  Pitched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pitchedCheck.SetValue( True )
		self.pitchedCheck.SetForegroundColour( checkColour )
		self.pitchedCheck.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		checkSizer.Add( self.pitchedCheck, 0, wx.ALIGN_CENTER|wx.ALL, 8 )

		checkSizer.Add( ( 30, 0 ), 0, 0, 0 )

		self.samplesCheck = wx.CheckBox( self.mainPanel, wx.ID_ANY, u"  Dump individual pitched samples", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.samplesCheck.SetValue( True )
		self.samplesCheck.SetForegroundColour( checkColour )
		self.samplesCheck.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		checkSizer.Add( self.samplesCheck, 0, wx.ALIGN_CENTER|wx.ALL, 8 )

		mainSizer.Add( checkSizer, 0, wx.LEFT|wx.RIGHT, 10 )

		mainSizer.Add( ( 0, 10 ), 0, 0, 0 )

		# ===== Generate Button (أزرق مع حجم أكبر) =====
		btnSizer = wx.BoxSizer( wx.HORIZONTAL )
		btnSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 0 )

		self.chromGenerate = wx.Button( self.mainPanel, wx.ID_ANY, u"⚡  Generate Chromatic", wx.DefaultPosition, wx.Size( 250, 45 ), 0 )
		self.chromGenerate.SetBackgroundColour( btnColour )
		self.chromGenerate.SetForegroundColour( btnTextColour )
		self.chromGenerate.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.chromGenerate.SetCursor( wx.Cursor( wx.CURSOR_HAND ) )
		btnSizer.Add( self.chromGenerate, 0, wx.ALL, 5 )

		btnSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 0 )
		mainSizer.Add( btnSizer, 0, wx.EXPAND|wx.ALL, 10 )

		# ===== شريط الحالة في الأسفل =====
		self.separator3 = wx.StaticLine( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.separator3.SetBackgroundColour( separatorColour )
		self.separator3.SetForegroundColour( separatorColour )
		mainSizer.Add( self.separator3, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 15 )

		statusSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.statusLabel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Ready", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statusLabel.Wrap( -1 )
		self.statusLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.statusLabel.SetForegroundColour( wx.Colour( 80, 90, 120 ) )
		statusSizer.Add( self.statusLabel, 0, wx.ALL, 8 )
		statusSizer.Add( ( 0, 0 ), 1, wx.EXPAND, 0 )

		self.versionLabel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"v1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.versionLabel.Wrap( -1 )
		self.versionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.versionLabel.SetForegroundColour( wx.Colour( 60, 65, 85 ) )
		statusSizer.Add( self.versionLabel, 0, wx.ALL, 8 )

		mainSizer.Add( statusSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10 )

		self.mainPanel.SetSizer( mainSizer )
		self.mainPanel.Layout()

		outerSizer.Add( self.mainPanel, 1, wx.EXPAND|wx.ALL, 12 )

		self.SetSizer( outerSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# ===== Connect Events =====
		self.chromGenerate.Bind( wx.EVT_BUTTON, self.generate_chromatic )

		# ===== تأثير الزر عند التمرير =====
		self.chromGenerate.Bind( wx.EVT_ENTER_WINDOW, lambda e: self.chromGenerate.SetBackgroundColour( btnHoverColour ) and self.chromGenerate.Refresh() or self.chromGenerate.Refresh() )
		self.chromGenerate.Bind( wx.EVT_LEAVE_WINDOW, lambda e: self.chromGenerate.SetBackgroundColour( btnColour ) and self.chromGenerate.Refresh() or self.chromGenerate.Refresh() )

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def generate_chromatic( self, event ):
		event.Skip()