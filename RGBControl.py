#!/usr/bin/python2

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import serial
from serial import SerialException
import time
import sys
import os

serialConnect = False
reason = 0
a = 0
pwd = os.path.dirname(os.path.abspath(__file__))
fn = os.path.join(os.path.dirname(__file__), 'store')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_RGBControl(object):
    if sys.argv[1] == '0':
        Port = "/dev/ttyACM0"
    if sys.argv[1] == '1':
        Port = "/dev/ttyACM1"
    if sys.argv[1] == '2':
        Port = "/dev/ttyACM2"
    serialPort = Port
    serialBaud = 57600
    serialConnect = False

    def setupUi(self, RGBControl):
        RGBControl.setObjectName(_fromUtf8("RGBControl"))
        RGBControl.resize(593, 292)
        RGBControl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        RGBControl.setFocusPolicy(QtCore.Qt.NoFocus)
        RGBControl.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.icon = QSystemTrayIcon()
        self.icon.setToolTip('RGBControl')
        self.icon.setIcon(QtGui.QIcon('%s/icons/applications-graphics.svg' % pwd))
        self.icon.show()
        self.centralwidget = QtGui.QWidget(RGBControl)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, -20, 263, 115))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 0, 261, 35))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.HSVSlider = QtGui.QSlider(self.centralwidget)
        self.HSVSlider.setGeometry(QtCore.QRect(21, 72, 171, 31))
        self.HSVSlider.setEnabled(False)
        self.HSVSlider.setMinimum(5)
        self.HSVSlider.setMaximum(200)
        self.HSVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HSVSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.HSVSlider.setTickInterval(10)
        self.HSVSlider.setObjectName(_fromUtf8("HSVSlider"))
        self.BLUESlide = QtGui.QSlider(self.centralwidget)
        self.BLUESlide.setGeometry(QtCore.QRect(380, 163, 141, 31))
        self.BLUESlide.setEnabled(False)
        self.BLUESlide.setMaximum(255)
        self.BLUESlide.setOrientation(QtCore.Qt.Horizontal)
        self.BLUESlide.setTickPosition(QtGui.QSlider.NoTicks)
        self.BLUESlide.setTickInterval(15)
        self.BLUESlide.setObjectName(_fromUtf8("BLUESlide"))
        self.GREENSlide = QtGui.QSlider(self.centralwidget)
        self.GREENSlide.setEnabled(False)
        self.GREENSlide.setGeometry(QtCore.QRect(380, 113, 141, 31))
        self.GREENSlide.setMaximum(255)
        self.GREENSlide.setOrientation(QtCore.Qt.Horizontal)
        self.GREENSlide.setTickPosition(QtGui.QSlider.NoTicks)
        self.GREENSlide.setTickInterval(15)
        self.GREENSlide.setObjectName(_fromUtf8("GREENSlide"))
        self.REDSlide = QtGui.QSlider(self.centralwidget)
        self.REDSlide.setEnabled(False)
        self.REDSlide.setGeometry(QtCore.QRect(380, 63, 141, 31))
        self.REDSlide.setAutoFillBackground(False)
        self.REDSlide.setMinimum(0)
        self.REDSlide.setMaximum(255)
        self.REDSlide.setProperty("value", 0)
        self.REDSlide.setSliderPosition(0)
        self.REDSlide.setOrientation(QtCore.Qt.Horizontal)
        self.REDSlide.setTickPosition(QtGui.QSlider.NoTicks)
        self.REDSlide.setTickInterval(15)
        self.REDSlide.setObjectName(_fromUtf8("REDSlide"))
        self.HSVButton = QtGui.QPushButton(self.centralwidget)
        self.HSVButton.setGeometry(QtCore.QRect(20, 120, 261, 61))
        self.HSVButton.setObjectName(_fromUtf8("HSVButton"))
        self.REDLbl = QtGui.QLabel(self.centralwidget)
        self.REDLbl.setEnabled(False)
        self.REDLbl.setGeometry(QtCore.QRect(320, 70, 48, 20))
        self.REDLbl.setObjectName(_fromUtf8("REDLbl"))
        self.GREENLbl = QtGui.QLabel(self.centralwidget)
        self.GREENLbl.setEnabled(False)
        self.GREENLbl.setGeometry(QtCore.QRect(320, 120, 50, 20))
        self.GREENLbl.setObjectName(_fromUtf8("GREENLbl"))
        self.BLUELbl = QtGui.QLabel(self.centralwidget)
        self.BLUELbl.setEnabled(False)
        self.BLUELbl.setGeometry(QtCore.QRect(320, 170, 49, 20))
        self.BLUELbl.setObjectName(_fromUtf8("BLUELbl"))
        self.REDBox = QtGui.QSpinBox(self.centralwidget)
        self.REDBox.setEnabled(False)
        self.REDBox.setGeometry(QtCore.QRect(530, 60, 60, 30))
        self.REDBox.setMaximum(255)
        self.REDBox.setObjectName(_fromUtf8("REDBox"))
        self.GREENBox = QtGui.QSpinBox(self.centralwidget)
        self.GREENBox.setEnabled(False)
        self.GREENBox.setGeometry(QtCore.QRect(530, 110, 60, 30))
        self.GREENBox.setMaximum(255)
        self.GREENBox.setObjectName(_fromUtf8("GREENBox"))
        self.BLUEBox = QtGui.QSpinBox(self.centralwidget)
        self.BLUEBox.setEnabled(False)
        self.BLUEBox.setGeometry(QtCore.QRect(530, 160, 60, 30))
        self.BLUEBox.setMaximum(255)
        self.BLUEBox.setObjectName(_fromUtf8("BLUEBox"))
        self.HSVBox = QtGui.QSpinBox(self.centralwidget)
        self.HSVBox.setEnabled(False)
        self.HSVBox.setGeometry(QtCore.QRect(220, 70, 61, 30))
        self.HSVBox.setMaximum(255)
        self.HSVBox.setObjectName(_fromUtf8("HSVBox"))
        RGBControl.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RGBControl)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 26))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuColor"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        RGBControl.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RGBControl)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RGBControl.setStatusBar(self.statusbar)
        self.statusbar.showMessage("System Status: Disconnected")
        self.toolBar = QtGui.QToolBar(RGBControl)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setMovable(False)
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        RGBControl.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        RGBControl.insertToolBarBreak(self.toolBar)
        self.actionSerial_Connect = QtGui.QAction(RGBControl)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/mail-send-receive-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSerial_Connect.setIcon(icon)
        self.actionSerial_Connect.setIconVisibleInMenu(True)
        self.actionSerial_Connect.setObjectName(_fromUtf8("actionSerial_Connect"))
        self.actionQuit = QtGui.QAction(RGBControl)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/edit-delete-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHSV_Loop = QtGui.QAction(RGBControl)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/document-open-recent-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHSV_Loop.setIcon(icon2)
        self.actionHSV_Loop.setEnabled(False)
        self.actionHSV_Loop.setIconVisibleInMenu(True)
        self.actionHSV_Loop.setObjectName(_fromUtf8("actionHSV_Loop"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-red.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Red = QtGui.QAction(RGBControl)
        self.actionSet_Red.setIcon(icon3)
        self.actionSet_Red.setEnabled(False)
        self.actionSet_Red.setIconVisibleInMenu(True)
        self.actionSet_Red.setObjectName(_fromUtf8("actionSet_Red"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-green.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Green = QtGui.QAction(RGBControl)
        self.actionSet_Green.setEnabled(False)
        self.actionSet_Green.setIcon(icon4)
        self.actionSet_Green.setIconVisibleInMenu(True)
        self.actionSet_Green.setObjectName(_fromUtf8("actionSet_Green"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-blue.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Blue = QtGui.QAction(RGBControl)
        self.actionSet_Blue.setEnabled(False)
        self.actionSet_Blue.setIcon(icon5)
        self.actionSet_Blue.setIconVisibleInMenu(True)
        self.actionSet_Blue.setObjectName(_fromUtf8("actionSet_Blue"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-white.png" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_White = QtGui.QAction(RGBControl)
        self.actionSet_White.setEnabled(False)
        self.actionSet_White.setIcon(icon6)
        self.actionSet_White.setIconVisibleInMenu(True)
        self.actionSet_White.setObjectName(_fromUtf8("actionSet_White"))
        icon6a = QtGui.QIcon()
        icon6a.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-grey.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Soft_White = QtGui.QAction(RGBControl)
        self.actionSet_Soft_White.setEnabled(False)
        self.actionSet_Soft_White.setIcon(icon6a)
        self.actionSet_Soft_White.setIconVisibleInMenu(True)
        self.actionSet_Soft_White.setObjectName(_fromUtf8("actionSet_Soft_White"))
        icon6b = QtGui.QIcon()
        icon6b.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Black = QtGui.QAction(RGBControl)
        self.actionSet_Black.setEnabled(False)
        self.actionSet_Black.setIcon(icon6b)
        self.actionSet_Black.setIconVisibleInMenu(True)
        self.actionSet_Black.setObjectName(_fromUtf8("actionSet_Black"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/folder-cyan.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_LightBlue = QtGui.QAction(RGBControl)
        self.actionSet_LightBlue.setEnabled(False)
        self.actionSet_LightBlue.setIcon(icon7)
        self.actionSet_LightBlue.setIconVisibleInMenu(True)
        self.actionSet_LightBlue.setObjectName(_fromUtf8("actionSet_LightBlue"))
        icon7d = QtGui.QIcon()
        icon7d.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/applications-graphics.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_ColorDial = QtGui.QAction(RGBControl)
        self.actionSet_ColorDial.setEnabled(False)
        self.actionSet_ColorDial.setIcon(icon7d)
        self.actionSet_ColorDial.setIconVisibleInMenu(True)
        self.actionSet_ColorDial.setObjectName(_fromUtf8("actionSet_ColorDial"))
        icon7a = QtGui.QIcon()
        icon7a.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/go-top-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Last = QtGui.QAction(RGBControl)
        self.actionSet_Last.setEnabled(False)
        self.actionSet_Last.setIcon(icon7a)
        self.actionSet_Last.setIconVisibleInMenu(True)
        self.actionSet_Last.setObjectName(_fromUtf8("actionSet_Last"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/go-bottom-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveRGB = QtGui.QAction(RGBControl)
        self.actionSaveRGB.setEnabled(False)
        self.actionSaveRGB.setIcon(icon8)
        self.actionSaveRGB.setIconVisibleInMenu(True)
        self.actionSaveRGB.setObjectName(_fromUtf8("actionSaveRGB"))
        self.actionAbout = QtGui.QAction(RGBControl)
        self.HSVButton.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("%s/icons/user-away-symbolic.svg" % pwd)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionSerial_Connect)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_Red)
        self.menuEdit.addAction(self.actionSet_Green)
        self.menuEdit.addAction(self.actionSet_Blue)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_White)
        self.menuEdit.addAction(self.actionSet_Soft_White)
        self.menuEdit.addAction(self.actionSet_Black)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_LightBlue)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_ColorDial)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_Last)
        self.menuEdit.addAction(self.actionSaveRGB)
        self.menuEdit.addAction(self.actionHSV_Loop)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSerial_Connect)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_Red)
        self.toolBar.addAction(self.actionSet_Green)
        self.toolBar.addAction(self.actionSet_Blue)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_White)
        self.toolBar.addAction(self.actionSet_Soft_White)
        self.toolBar.addAction(self.actionSet_Black)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_LightBlue)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_ColorDial)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_Last)
        self.toolBar.addAction(self.actionSaveRGB)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHSV_Loop)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(RGBControl)
        self.actionSerial_Connect.triggered.connect(lambda: self.setup_serial())
        self.actionSet_Red.triggered.connect(lambda: self.setRed())
        self.actionSet_Green.triggered.connect(lambda: self.setGreen())
        self.actionSet_Blue.triggered.connect(lambda: self.setBlue())
        self.actionSet_White.triggered.connect(lambda: self.setWhite())
        self.actionSet_Soft_White.triggered.connect(lambda: self.setSoftWhite())
        self.actionSet_Black.triggered.connect(lambda: self.setBlack())
        self.actionSet_LightBlue.triggered.connect(lambda: self.setLightBlue())
        self.actionSet_Last.triggered.connect(lambda: self.setLast())
        self.actionSaveRGB.triggered.connect(lambda: self.SaveRGB())
        self.actionSet_ColorDial.triggered.connect(lambda: self.showDialog())
        self.actionHSV_Loop.triggered.connect(lambda: self.hsvLoop())
        self.actionAbout.triggered.connect(lambda: self.aboutDial())
        self.BLUESlide.valueChanged.connect(lambda: self.slider_changed("blue", self.BLUESlide.value()))
        self.GREENSlide.valueChanged.connect(lambda: self.slider_changed("green", self.GREENSlide.value()))
        self.REDSlide.valueChanged.connect(lambda: self.slider_changed("red", self.REDSlide.value()))
        self.HSVButton.clicked.connect(lambda: self.hsvLoop())
        self.actionQuit.triggered.connect(lambda: self.quit())
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), RGBControl.close)
        QtCore.QObject.connect(self.REDSlide, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.REDBox.setValue)
        QtCore.QObject.connect(self.GREENSlide, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.GREENBox.setValue)
        QtCore.QObject.connect(self.BLUESlide, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BLUEBox.setValue)
        QtCore.QObject.connect(self.BLUEBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.BLUESlide.setValue)
        QtCore.QObject.connect(self.GREENBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.GREENSlide.setValue)
        QtCore.QObject.connect(self.REDBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.REDSlide.setValue)
        QtCore.QObject.connect(self.HSVSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.HSVBox.setValue)
        QtCore.QObject.connect(self.icon, QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.trayIconActivated)

    def retranslateUi(self, RGBControl):
        RGBControl.setWindowTitle(QtGui.QApplication.translate("RGBControl", "RGB Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RGBControl", "Fade Delay variable on Arduino(ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RGBControl", "RGB Control App for Arduino", None, QtGui.QApplication.UnicodeUTF8))
        self.HSVButton.setText(QtGui.QApplication.translate("RGBControl", "HSV Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.REDLbl.setText(QtGui.QApplication.translate("RGBControl", "Red:    ", None, QtGui.QApplication.UnicodeUTF8))
        self.GREENLbl.setText(QtGui.QApplication.translate("RGBControl", "Green:", None, QtGui.QApplication.UnicodeUTF8))
        self.BLUELbl.setText(QtGui.QApplication.translate("RGBControl", "Blue:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("RGBControl", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("RGBControl", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("RGBControl", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("RGBControl", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSerial_Connect.setText(QtGui.QApplication.translate("RGBControl", "Serial Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("RGBControl", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("RGBControl", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHSV_Loop.setText(QtGui.QApplication.translate("RGBControl", "HSV Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Red.setText(QtGui.QApplication.translate("RGBControl", "Set Red", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Green.setText(QtGui.QApplication.translate("RGBControl", "Set Green", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Blue.setText(QtGui.QApplication.translate("RGBControl", "Set Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_White.setText(QtGui.QApplication.translate("RGBControl", "Set White", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Soft_White.setText(QtGui.QApplication.translate("RGBControl", "Set Soft-White", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Black.setText(QtGui.QApplication.translate("RGBControl", "Set Black (Turn Off w/o Quit)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_LightBlue.setText(QtGui.QApplication.translate("RGBControl", "Set Light Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Last.setText(QtGui.QApplication.translate("RGBControl", "Set from Saved", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveRGB.setText(QtGui.QApplication.translate("RGBControl", "Save RGB", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("RGBControl", "About", None, QtGui.QApplication.UnicodeUTF8))

    def disableAll(self):
            self.HSVSlider.setEnabled(False)
            self.BLUESlide.setEnabled(False)
            self.GREENSlide.setEnabled(False)
            self.REDSlide.setEnabled(False)
            self.REDLbl.setEnabled(False)
            self.GREENLbl.setEnabled(False)
            self.BLUELbl.setEnabled(False)
            self.REDBox.setEnabled(False)
            self.GREENBox.setEnabled(False)
            self.BLUEBox.setEnabled(False)
            self.HSVBox.setEnabled(False)
            self.actionSet_Red.setEnabled(False)
            self.actionSet_Green.setEnabled(False)
            self.actionSet_Blue.setEnabled(False)
            self.actionSet_White.setEnabled(False)
            self.actionSet_Soft_White.setEnabled(False)
            self.actionSet_Black.setEnabled(False)
            self.actionSet_LightBlue.setEnabled(False)
            self.actionSet_Last.setEnabled(False)
            self.actionSaveRGB.setEnabled(False)
            self.actionHSV_Loop.setEnabled(False)
            self.statusbar.showMessage("System Status: Disconnected")

    def enableAll(self):
            self.HSVSlider.setEnabled(True)
            self.BLUESlide.setEnabled(True)
            self.GREENSlide.setEnabled(True)
            self.REDSlide.setEnabled(True)
            self.REDLbl.setEnabled(True)
            self.GREENLbl.setEnabled(True)
            self.BLUELbl.setEnabled(True)
            self.REDBox.setEnabled(True)
            self.GREENBox.setEnabled(True)
            self.BLUEBox.setEnabled(True)
            self.HSVBox.setEnabled(True)
            self.HSVButton.setEnabled(True)
            self.actionSet_Red.setEnabled(True)
            self.actionSet_Green.setEnabled(True)
            self.actionSet_Blue.setEnabled(True)
            self.actionSet_White.setEnabled(True)
            self.actionSet_Soft_White.setEnabled(True)
            self.actionSet_Black.setEnabled(True)
            self.actionSet_LightBlue.setEnabled(True)
            self.actionSet_Last.setEnabled(True)
            self.actionSaveRGB.setEnabled(True)
            self.actionSet_ColorDial.setEnabled(True)
            self.actionHSV_Loop.setEnabled(True)
            self.statusbar.showMessage("System Status: Connected")

    def setup_serial(self):
            try:
                if (self.serialConnect is False):
                        self.ser = serial.Serial()
                        self.ser.port = self.serialPort
                        self.ser.baudrate = self.serialBaud
                        self.ser.open()
                if (self.ser.isOpen()):
                    self.serialConnect = True
                    self.enableAll()
                    self.setBlack()
                print "Serial Port Connected..."
            except serial.SerialException, e:
                print "No connection to the device could be established: " + str(e)
            #else:
            #        self.disableAll()
            #        self.serialConnect = False
            #        print "ERROR: Serial Unable to connect on " + self.ser.portstr

    def setRed(self):
            self.REDSlide.setValue(255)
            self.GREENSlide.setValue(0)
            self.BLUESlide.setValue(0)
            self.serial_write(255, 0, 0)
            print "Red preset activeted"
            self.statusbar.showMessage("Red preset activeted")

    def setGreen(self):
            self.REDSlide.setValue(0)
            self.GREENSlide.setValue(255)
            self.BLUESlide.setValue(0)
            self.serial_write(0, 255, 0)
            print "Green preset activeted"
            self.statusbar.showMessage("Green preset activeted")

    def setBlue(self):
            self.REDSlide.setValue(0)
            self.GREENSlide.setValue(0)
            self.BLUESlide.setValue(255)
            self.serial_write(0, 0, 255)
            print "Blue preset activeted"
            self.statusbar.showMessage("Blue preset activeted")

    def setWhite(self):
            self.REDSlide.setValue(255)
            self.GREENSlide.setValue(255)
            self.BLUESlide.setValue(255)
            self.serial_write(255, 255, 255)
            print "White preset activeted"
            self.statusbar.showMessage("White preset activeted")

    def setSoftWhite(self):
            self.REDSlide.setValue(223)
            self.GREENSlide.setValue(161)
            self.BLUESlide.setValue(59)
            self.serial_write(223, 161, 59)
            print "Soft White preset activeted"
            self.statusbar.showMessage("Soft White preset activeted")

    def setBlack(self):
            self.REDSlide.setValue(0)
            self.GREENSlide.setValue(0)
            self.BLUESlide.setValue(0)
            self.serial_write(0, 0, 0)
            print "Black preset activeted"
            self.statusbar.showMessage("Black preset activeted")

    def setLightBlue(self):
            self.REDSlide.setValue(67)
            self.GREENSlide.setValue(123)
            self.BLUESlide.setValue(224)
            self.serial_write(67, 123, 224)
            print "Light Blue preset activeted"
            self.statusbar.showMessage("Light Blue preset activeted")

    def setLast(self):
            el = []
            f = open(fn, 'r')
            for line in f:
                el.append(line)
            self.REDSlide.setValue(int(el[0]))
            self.GREENSlide.setValue(int(el[1]))
            self.BLUESlide.setValue(int(el[2]))
            try:
                self.serial_write(int(el[0]), int(el[1]), int(el[2]))
            except serial.SerialException, e:
                raise e

    def SaveRGB(self):
            listel = []
            listel.append(self.REDSlide.value())
            listel.append(self.GREENSlide.value())
            listel.append(self.BLUESlide.value())
            print "RGB combination saved is: ", listel
            a = "RGB combination saved is: " + str(listel)
            self.statusbar.showMessage(a)
            f = open(fn, 'w')
            f.write("\n".join(str(x) for x in listel))
            f.close()

    def showDialog(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.REDSlide.setValue(col.red())
            self.GREENSlide.setValue(col.green())
            self.BLUESlide.setValue(col.blue())
            self.serial_write(col.red(), col.green(), col.blue())

    def slider_changed(self, n, value):
        val = value
        name = n
        if name == "red":
            self.ser.write("r" + chr(int(val)))
        elif name == "green":
            self.ser.write("g" + chr(int(val)))
        elif name == "blue":
            self.ser.write("b" + chr(int(val)))
        else:
            print "ERROR: Invalid widget name, in on_changed function"
            self.statusbar.showMessage("ERROR: Invalid widget name, in on_changed function")

    def serial_write(self, rval, gval, bval):
        self.ser.write("r" + chr(int(rval)))
        self.ser.write("g" + chr(int(gval)))
        self.ser.write("b" + chr(int(bval)))
        array = []
        array.append(rval)
        array.append(gval)
        array.append(bval)
        print "RGB combination sent to Arduino is: ", array
        a = "RGB combination sent to Arduino is: " + str(array)
        self.statusbar.showMessage(a)

    def hsvLoop(self):
        delay = self.HSVSlider.value()
        self.ser.write("f" + chr(int(delay)))
        time.sleep(.015)
        self.ser.write("f" + chr(int(delay)))
        print "HSV Loop activeted with delay of " + str(delay)
        a = "HSV Loop activeted with delay of " + str(delay) + " ms"
        self.statusbar.showMessage(a)

    def quit(self):
        if (serialConnect is True):
            print 'Closing Serial Connection...'
            self.ser.close()
        print 'Close program'

    def aboutDial(self):
        w = QtGui.QWidget()
        w.resize(200, 200)
        w.move(600, 600)
        QMessageBox.about(w, 'About RGBControl', "\n\nA program by\n\n  cbar\n\n")

    def trayIconActivated(self, reason):
        global a
        if (reason == QSystemTrayIcon.DoubleClick and a == 0):
            RGBControl.hide()
            RGBControl.raise_()
            a += 1
        elif (reason == QSystemTrayIcon.DoubleClick and a == 1):
            RGBControl.show()
            RGBControl.raise_()
            a -= 1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    RGBControl = QtGui.QMainWindow()
    RGBControl.setWindowIcon(QtGui.QIcon('%s/icons/applications-graphics.svg' % pwd))
    ui = Ui_RGBControl()
    ui.setupUi(RGBControl)
    RGBControl.show()
    sys.exit(app.exec_())
