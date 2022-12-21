# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Weather Processor", pos = wx.DefaultPosition, size = wx.Size( 500,302 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText31 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"What would you like to download?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer11.Add( self.m_staticText31, 0, wx.ALL, 5 )

		choiceDataChoices = [ u"Missing data", u"All data" ]
		self.choiceData = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDataChoices, 0 )
		self.choiceData.SetSelection( 0 )
		gSizer11.Add( self.choiceData, 0, wx.ALL, 5 )

		self.lblStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblStatus.Wrap( -1 )

		gSizer11.Add( self.lblStatus, 0, wx.ALL, 5 )

		self.btnDownload = wx.Button( self.m_panel1, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.btnDownload, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( gSizer11 )
		self.m_panel1.Layout()
		gSizer11.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Download", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Daily Avg Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Monthly Avg Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Year(YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtDailyYear = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.txtDailyYear, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Month(MM)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtDailyMonth = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.txtDailyMonth, 0, wx.ALL, 5 )


		gSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Start Year(YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer7.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.txtStartYear = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.txtStartYear, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"End Year(YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer7.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.txtEndYear = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.txtEndYear, 0, wx.ALL, 5 )


		gSizer5.Add( gSizer7, 1, wx.EXPAND, 5 )

		self.btnPlotDaily = wx.Button( self.m_panel2, wx.ID_ANY, u"Plot Daily Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.btnPlotDaily, 0, wx.ALL, 5 )

		self.btnPlotMonthly = wx.Button( self.m_panel2, wx.ID_ANY, u"Plot Monthly Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.btnPlotMonthly, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( gSizer5 )
		self.m_panel2.Layout()
		gSizer5.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Report", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnDownload.Bind( wx.EVT_BUTTON, self.download )
		self.btnPlotDaily.Bind( wx.EVT_BUTTON, self.plot_daily_temps )
		self.btnPlotMonthly.Bind( wx.EVT_BUTTON, self.plot_monthly_temps )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def download( self, event ):
		event.Skip()

	def plot_daily_temps( self, event ):
		event.Skip()

	def plot_monthly_temps( self, event ):
		event.Skip()


