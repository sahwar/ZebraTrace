# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_build\mainwindow.ui'
#
# Created: Sat Apr 04 23:03:54 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(885, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/ico/zebra.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topPanel = QtGui.QHBoxLayout()
        self.topPanel.setObjectName(_fromUtf8("topPanel"))
        self.labelPreview = QtGui.QLabel(self.centralwidget)
        self.labelPreview.setObjectName(_fromUtf8("labelPreview"))
        self.topPanel.addWidget(self.labelPreview)
        self.previewMode = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewMode.sizePolicy().hasHeightForWidth())
        self.previewMode.setSizePolicy(sizePolicy)
        self.previewMode.setMinimumSize(QtCore.QSize(150, 0))
        self.previewMode.setObjectName(_fromUtf8("previewMode"))
        self.previewMode.addItem(_fromUtf8(""))
        self.previewMode.addItem(_fromUtf8(""))
        self.topPanel.addWidget(self.previewMode)
        self.labelTransparency = QtGui.QLabel(self.centralwidget)
        self.labelTransparency.setObjectName(_fromUtf8("labelTransparency"))
        self.topPanel.addWidget(self.labelTransparency)
        self.sliderTransparency = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderTransparency.sizePolicy().hasHeightForWidth())
        self.sliderTransparency.setSizePolicy(sizePolicy)
        self.sliderTransparency.setMinimumSize(QtCore.QSize(150, 0))
        self.sliderTransparency.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderTransparency.setMaximum(100)
        self.sliderTransparency.setSingleStep(1)
        self.sliderTransparency.setPageStep(10)
        self.sliderTransparency.setProperty("value", 50)
        self.sliderTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTransparency.setInvertedAppearance(False)
        self.sliderTransparency.setInvertedControls(False)
        self.sliderTransparency.setObjectName(_fromUtf8("sliderTransparency"))
        self.topPanel.addWidget(self.sliderTransparency)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topPanel.addItem(spacerItem)
        self.labelResolution = QtGui.QLabel(self.centralwidget)
        self.labelResolution.setObjectName(_fromUtf8("labelResolution"))
        self.topPanel.addWidget(self.labelResolution)
        self.docResolution = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docResolution.sizePolicy().hasHeightForWidth())
        self.docResolution.setSizePolicy(sizePolicy)
        self.docResolution.setDecimals(3)
        self.docResolution.setMinimum(0.001)
        self.docResolution.setMaximum(10000.0)
        self.docResolution.setSingleStep(0.1)
        self.docResolution.setProperty("value", 90.0)
        self.docResolution.setObjectName(_fromUtf8("docResolution"))
        self.topPanel.addWidget(self.docResolution)
        self.labelUnits = QtGui.QLabel(self.centralwidget)
        self.labelUnits.setObjectName(_fromUtf8("labelUnits"))
        self.topPanel.addWidget(self.labelUnits)
        self.units = QtGui.QComboBox(self.centralwidget)
        self.units.setObjectName(_fromUtf8("units"))
        self.units.addItem(_fromUtf8(""))
        self.units.addItem(_fromUtf8(""))
        self.units.addItem(_fromUtf8(""))
        self.units.addItem(_fromUtf8(""))
        self.topPanel.addWidget(self.units)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topPanel.addItem(spacerItem1)
        self.topPanel.setStretch(9, 1)
        self.verticalLayout.addLayout(self.topPanel)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 3, 3, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame_2 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.viewContainer = QtGui.QHBoxLayout()
        self.viewContainer.setSpacing(6)
        self.viewContainer.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.viewContainer.setObjectName(_fromUtf8("viewContainer"))
        self.horizontalLayout_3.addLayout(self.viewContainer)
        self.tabPreferences = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabPreferences.sizePolicy().hasHeightForWidth())
        self.tabPreferences.setSizePolicy(sizePolicy)
        self.tabPreferences.setMinimumSize(QtCore.QSize(240, 0))
        self.tabPreferences.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabPreferences.setTabPosition(QtGui.QTabWidget.North)
        self.tabPreferences.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabPreferences.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabPreferences.setDocumentMode(False)
        self.tabPreferences.setObjectName(_fromUtf8("tabPreferences"))
        self.tabOptions = QtGui.QWidget()
        self.tabOptions.setObjectName(_fromUtf8("tabOptions"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabOptions)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.boxCurves = QtGui.QGroupBox(self.tabOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxCurves.sizePolicy().hasHeightForWidth())
        self.boxCurves.setSizePolicy(sizePolicy)
        self.boxCurves.setMinimumSize(QtCore.QSize(0, 0))
        self.boxCurves.setFlat(True)
        self.boxCurves.setCheckable(False)
        self.boxCurves.setObjectName(_fromUtf8("boxCurves"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.boxCurves)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.boxCurves)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.numberCurves = QtGui.QSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberCurves.sizePolicy().hasHeightForWidth())
        self.numberCurves.setSizePolicy(sizePolicy)
        self.numberCurves.setMinimum(1)
        self.numberCurves.setMaximum(9999)
        self.numberCurves.setSingleStep(1)
        self.numberCurves.setProperty("value", 100)
        self.numberCurves.setObjectName(_fromUtf8("numberCurves"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.numberCurves)
        self.label_2 = QtGui.QLabel(self.boxCurves)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.curveWidthMin = QtGui.QDoubleSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveWidthMin.sizePolicy().hasHeightForWidth())
        self.curveWidthMin.setSizePolicy(sizePolicy)
        self.curveWidthMin.setDecimals(5)
        self.curveWidthMin.setMaximum(10000.0)
        self.curveWidthMin.setSingleStep(0.1)
        self.curveWidthMin.setProperty("value", 0.1)
        self.curveWidthMin.setObjectName(_fromUtf8("curveWidthMin"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.curveWidthMin)
        self.label_3 = QtGui.QLabel(self.boxCurves)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.curveWidthMax = QtGui.QDoubleSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveWidthMax.sizePolicy().hasHeightForWidth())
        self.curveWidthMax.setSizePolicy(sizePolicy)
        self.curveWidthMax.setDecimals(5)
        self.curveWidthMax.setMaximum(10000.0)
        self.curveWidthMax.setSingleStep(0.1)
        self.curveWidthMax.setProperty("value", 3.0)
        self.curveWidthMax.setObjectName(_fromUtf8("curveWidthMax"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.curveWidthMax)
        self.label_10 = QtGui.QLabel(self.boxCurves)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.curveWriting = QtGui.QComboBox(self.boxCurves)
        self.curveWriting.setObjectName(_fromUtf8("curveWriting"))
        self.curveWriting.addItem(_fromUtf8(""))
        self.curveWriting.addItem(_fromUtf8(""))
        self.curveWriting.addItem(_fromUtf8(""))
        self.curveWriting.addItem(_fromUtf8(""))
        self.curveWriting.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.curveWriting)
        self.label_8 = QtGui.QLabel(self.boxCurves)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.nodeReduction = QtGui.QSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeReduction.sizePolicy().hasHeightForWidth())
        self.nodeReduction.setSizePolicy(sizePolicy)
        self.nodeReduction.setMinimum(0)
        self.nodeReduction.setMaximum(100)
        self.nodeReduction.setSingleStep(1)
        self.nodeReduction.setProperty("value", 0)
        self.nodeReduction.setObjectName(_fromUtf8("nodeReduction"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.nodeReduction)
        self.horizontalLayout_4.addLayout(self.formLayout_3)
        self.verticalLayout_5.addWidget(self.boxCurves)
        self.boxAdvancedPref = QtGui.QGroupBox(self.tabOptions)
        self.boxAdvancedPref.setFlat(True)
        self.boxAdvancedPref.setCheckable(True)
        self.boxAdvancedPref.setChecked(True)
        self.boxAdvancedPref.setObjectName(_fromUtf8("boxAdvancedPref"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.boxAdvancedPref)
        self.verticalLayout_7.setContentsMargins(14, -1, 0, 0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.boxFunctions = QtGui.QGroupBox(self.boxAdvancedPref)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxFunctions.sizePolicy().hasHeightForWidth())
        self.boxFunctions.setSizePolicy(sizePolicy)
        self.boxFunctions.setFlat(True)
        self.boxFunctions.setCheckable(False)
        self.boxFunctions.setChecked(False)
        self.boxFunctions.setObjectName(_fromUtf8("boxFunctions"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.boxFunctions)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_1 = QtGui.QLabel(self.boxFunctions)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.resolution = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution.sizePolicy().hasHeightForWidth())
        self.resolution.setSizePolicy(sizePolicy)
        self.resolution.setDecimals(2)
        self.resolution.setMaximum(999.99)
        self.resolution.setSingleStep(1.0)
        self.resolution.setProperty("value", 100.0)
        self.resolution.setObjectName(_fromUtf8("resolution"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.resolution)
        self.label_4 = QtGui.QLabel(self.boxFunctions)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.rangeMin = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeMin.sizePolicy().hasHeightForWidth())
        self.rangeMin.setSizePolicy(sizePolicy)
        self.rangeMin.setDecimals(5)
        self.rangeMin.setMinimum(-1000.0)
        self.rangeMin.setMaximum(1000.0)
        self.rangeMin.setSingleStep(0.1)
        self.rangeMin.setProperty("value", -1.0)
        self.rangeMin.setObjectName(_fromUtf8("rangeMin"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rangeMin)
        self.label_5 = QtGui.QLabel(self.boxFunctions)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.rangeMax = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeMax.sizePolicy().hasHeightForWidth())
        self.rangeMax.setSizePolicy(sizePolicy)
        self.rangeMax.setDecimals(5)
        self.rangeMax.setMinimum(-1000.0)
        self.rangeMax.setMaximum(1000.0)
        self.rangeMax.setSingleStep(0.1)
        self.rangeMax.setProperty("value", 1.0)
        self.rangeMax.setObjectName(_fromUtf8("rangeMax"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rangeMax)
        self.label_9 = QtGui.QLabel(self.boxFunctions)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.coordSystem = QtGui.QComboBox(self.boxFunctions)
        self.coordSystem.setObjectName(_fromUtf8("coordSystem"))
        self.coordSystem.addItem(_fromUtf8(""))
        self.coordSystem.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.coordSystem)
        self.label_6 = QtGui.QLabel(self.boxFunctions)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditX = QtGui.QLineEdit(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditX.sizePolicy().hasHeightForWidth())
        self.lineEditX.setSizePolicy(sizePolicy)
        self.lineEditX.setText(_fromUtf8(""))
        self.lineEditX.setObjectName(_fromUtf8("lineEditX"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditX)
        self.label_7 = QtGui.QLabel(self.boxFunctions)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditY = QtGui.QLineEdit(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditY.sizePolicy().hasHeightForWidth())
        self.lineEditY.setSizePolicy(sizePolicy)
        self.lineEditY.setToolTip(_fromUtf8(""))
        self.lineEditY.setText(_fromUtf8(""))
        self.lineEditY.setObjectName(_fromUtf8("lineEditY"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditY)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_6.addWidget(self.boxFunctions)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addWidget(self.boxAdvancedPref)
        self.boxInfo = QtGui.QGroupBox(self.tabOptions)
        self.boxInfo.setFlat(True)
        self.boxInfo.setObjectName(_fromUtf8("boxInfo"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.boxInfo)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelObject = QtGui.QLabel(self.boxInfo)
        self.labelObject.setObjectName(_fromUtf8("labelObject"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelObject)
        self.labelNumberObject = QtGui.QLabel(self.boxInfo)
        self.labelNumberObject.setObjectName(_fromUtf8("labelNumberObject"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelNumberObject)
        self.labelNodes = QtGui.QLabel(self.boxInfo)
        self.labelNodes.setObjectName(_fromUtf8("labelNodes"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelNodes)
        self.labelNumberNodes = QtGui.QLabel(self.boxInfo)
        self.labelNumberNodes.setObjectName(_fromUtf8("labelNumberNodes"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelNumberNodes)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.boxInfo)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.tabPreferences.addTab(self.tabOptions, _fromUtf8(""))
        self.tabInfo = QtGui.QWidget()
        self.tabInfo.setEnabled(True)
        self.tabInfo.setObjectName(_fromUtf8("tabInfo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabInfo)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.infoText = QtGui.QPlainTextEdit(self.tabInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoText.sizePolicy().hasHeightForWidth())
        self.infoText.setSizePolicy(sizePolicy)
        self.infoText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.infoText.setLineWidth(1)
        self.infoText.setPlainText(_fromUtf8(""))
        self.infoText.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.infoText.setBackgroundVisible(False)
        self.infoText.setCenterOnScroll(False)
        self.infoText.setObjectName(_fromUtf8("infoText"))
        self.verticalLayout_4.addWidget(self.infoText)
        self.tabPreferences.addTab(self.tabInfo, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.bottomPanel = QtGui.QHBoxLayout()
        self.bottomPanel.setObjectName(_fromUtf8("bottomPanel"))
        self.labelPos = QtGui.QLabel(self.centralwidget)
        self.labelPos.setText(_fromUtf8("(0.000;0.000)"))
        self.labelPos.setObjectName(_fromUtf8("labelPos"))
        self.bottomPanel.addWidget(self.labelPos)
        self.labelFeedback = QtGui.QLabel(self.centralwidget)
        self.labelFeedback.setObjectName(_fromUtf8("labelFeedback"))
        self.bottomPanel.addWidget(self.labelFeedback)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottomPanel.addItem(spacerItem3)
        self.buttonAutoTrace = QtGui.QPushButton(self.centralwidget)
        self.buttonAutoTrace.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/png32/046-32_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/png32/046-32_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonAutoTrace.setIcon(icon1)
        self.buttonAutoTrace.setCheckable(True)
        self.buttonAutoTrace.setChecked(False)
        self.buttonAutoTrace.setFlat(False)
        self.buttonAutoTrace.setObjectName(_fromUtf8("buttonAutoTrace"))
        self.bottomPanel.addWidget(self.buttonAutoTrace)
        self.buttonTrace = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTrace.sizePolicy().hasHeightForWidth())
        self.buttonTrace.setSizePolicy(sizePolicy)
        self.buttonTrace.setAutoDefault(True)
        self.buttonTrace.setDefault(False)
        self.buttonTrace.setFlat(False)
        self.buttonTrace.setObjectName(_fromUtf8("buttonTrace"))
        self.bottomPanel.addWidget(self.buttonTrace)
        self.buttonSave = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSave.sizePolicy().hasHeightForWidth())
        self.buttonSave.setSizePolicy(sizePolicy)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.bottomPanel.addWidget(self.buttonSave)
        self.buttonHelp = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonHelp.sizePolicy().hasHeightForWidth())
        self.buttonHelp.setSizePolicy(sizePolicy)
        self.buttonHelp.setAutoDefault(False)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.bottomPanel.addWidget(self.buttonHelp)
        self.bottomPanel.setStretch(2, 1)
        self.verticalLayout.addLayout(self.bottomPanel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpenBitmap = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenBitmap.setIcon(icon2)
        self.actionOpenBitmap.setMenuRole(QtGui.QAction.NoRole)
        self.actionOpenBitmap.setObjectName(_fromUtf8("actionOpenBitmap"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionBackground = QtGui.QAction(MainWindow)
        self.actionBackground.setCheckable(True)
        self.actionBackground.setChecked(True)
        self.actionBackground.setObjectName(_fromUtf8("actionBackground"))
        self.actionBorder = QtGui.QAction(MainWindow)
        self.actionBorder.setCheckable(True)
        self.actionBorder.setChecked(True)
        self.actionBorder.setObjectName(_fromUtf8("actionBorder"))
        self.actionLoadPreset = QtGui.QAction(MainWindow)
        self.actionLoadPreset.setObjectName(_fromUtf8("actionLoadPreset"))
        self.actionSavePreset = QtGui.QAction(MainWindow)
        self.actionSavePreset.setObjectName(_fromUtf8("actionSavePreset"))
        self.actionTraceImage = QtGui.QAction(MainWindow)
        self.actionTraceImage.setCheckable(True)
        self.actionTraceImage.setChecked(True)
        self.actionTraceImage.setObjectName(_fromUtf8("actionTraceImage"))
        self.menuFile.addAction(self.actionOpenBitmap)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadPreset)
        self.menuFile.addAction(self.actionSavePreset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menu_View.addAction(self.actionBackground)
        self.menu_View.addAction(self.actionBorder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.previewMode.setCurrentIndex(0)
        self.tabPreferences.setCurrentIndex(0)
        QtCore.QObject.connect(self.boxAdvancedPref, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.boxFunctions.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.numberCurves, self.curveWidthMin)
        MainWindow.setTabOrder(self.curveWidthMin, self.curveWidthMax)
        MainWindow.setTabOrder(self.curveWidthMax, self.curveWriting)
        MainWindow.setTabOrder(self.curveWriting, self.nodeReduction)
        MainWindow.setTabOrder(self.nodeReduction, self.boxAdvancedPref)
        MainWindow.setTabOrder(self.boxAdvancedPref, self.resolution)
        MainWindow.setTabOrder(self.resolution, self.rangeMin)
        MainWindow.setTabOrder(self.rangeMin, self.rangeMax)
        MainWindow.setTabOrder(self.rangeMax, self.coordSystem)
        MainWindow.setTabOrder(self.coordSystem, self.lineEditX)
        MainWindow.setTabOrder(self.lineEditX, self.lineEditY)
        MainWindow.setTabOrder(self.lineEditY, self.buttonTrace)
        MainWindow.setTabOrder(self.buttonTrace, self.buttonSave)
        MainWindow.setTabOrder(self.buttonSave, self.buttonHelp)
        MainWindow.setTabOrder(self.buttonHelp, self.previewMode)
        MainWindow.setTabOrder(self.previewMode, self.sliderTransparency)
        MainWindow.setTabOrder(self.sliderTransparency, self.docResolution)
        MainWindow.setTabOrder(self.docResolution, self.units)
        MainWindow.setTabOrder(self.units, self.tabPreferences)
        MainWindow.setTabOrder(self.tabPreferences, self.infoText)
        MainWindow.setTabOrder(self.infoText, self.buttonAutoTrace)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ZebraTRACE", None))
        self.labelPreview.setText(_translate("MainWindow", "Preview:", None))
        self.previewMode.setItemText(0, _translate("MainWindow", "Tracing Result", None))
        self.previewMode.setItemText(1, _translate("MainWindow", "Wireframe Overlay", None))
        self.labelTransparency.setText(_translate("MainWindow", "Transparency:", None))
        self.sliderTransparency.setToolTip(_translate("MainWindow", "Transparent bitmap layer", None))
        self.labelResolution.setText(_translate("MainWindow", "Resolution:", None))
        self.docResolution.setToolTip(_translate("MainWindow", "Dots per inch in Image", None))
        self.labelUnits.setText(_translate("MainWindow", "Units:", None))
        self.units.setToolTip(_translate("MainWindow", "Drawing Units", None))
        self.units.setItemText(0, _translate("MainWindow", "px", None))
        self.units.setItemText(1, _translate("MainWindow", "mm", None))
        self.units.setItemText(2, _translate("MainWindow", "cm", None))
        self.units.setItemText(3, _translate("MainWindow", "in", None))
        self.boxCurves.setTitle(_translate("MainWindow", " Curves", None))
        self.label.setText(_translate("MainWindow", "Number of Curves (<b>n</b>):", None))
        self.numberCurves.setToolTip(_translate("MainWindow", "<b>i</b> = 1... <b>n</b>", None))
        self.label_2.setText(_translate("MainWindow", "Minimum Width:", None))
        self.curveWidthMin.setToolTip(_translate("MainWindow", "In the current unit", None))
        self.label_3.setText(_translate("MainWindow", "Maximum Width:", None))
        self.curveWidthMax.setToolTip(_translate("MainWindow", "In the current unit", None))
        self.label_10.setText(_translate("MainWindow", "Writing:", None))
        self.curveWriting.setItemText(0, _translate("MainWindow", "Center Line", None))
        self.curveWriting.setItemText(1, _translate("MainWindow", "Left End", None))
        self.curveWriting.setItemText(2, _translate("MainWindow", "Right End", None))
        self.curveWriting.setItemText(3, _translate("MainWindow", "Left Line", None))
        self.curveWriting.setItemText(4, _translate("MainWindow", "Right Line", None))
        self.label_8.setText(_translate("MainWindow", "Node Reduction:", None))
        self.nodeReduction.setToolTip(_translate("MainWindow", "Node reduction tolerance", None))
        self.boxAdvancedPref.setTitle(_translate("MainWindow", "Advanced", None))
        self.boxFunctions.setTitle(_translate("MainWindow", "Functions", None))
        self.label_1.setText(_translate("MainWindow", "Quality:", None))
        self.resolution.setToolTip(_translate("MainWindow", "Percentage", None))
        self.label_4.setText(_translate("MainWindow", "Min (<b>a</b>) value:", None))
        self.rangeMin.setToolTip(_translate("MainWindow", "Minimum value for (a) variable", None))
        self.label_5.setText(_translate("MainWindow", "Max (<b>a</b>) value:", None))
        self.rangeMax.setToolTip(_translate("MainWindow", "Maximum value for (a) variable", None))
        self.label_9.setText(_translate("MainWindow", "Coordinates:", None))
        self.coordSystem.setItemText(0, _translate("MainWindow", "Cartesian", None))
        self.coordSystem.setItemText(1, _translate("MainWindow", "Polar", None))
        self.label_6.setText(_translate("MainWindow", "Function <b>X(a)</b>:", None))
        self.lineEditX.setToolTip(_translate("MainWindow", "Use (a),( i) and (n) as parameters", None))
        self.label_7.setText(_translate("MainWindow", "Function <b>Y(a)</b>:", None))
        self.boxInfo.setTitle(_translate("MainWindow", "Trace result details", None))
        self.labelObject.setText(_translate("MainWindow", "Paths:", None))
        self.labelNumberObject.setText(_translate("MainWindow", "0", None))
        self.labelNodes.setText(_translate("MainWindow", "Nodes:", None))
        self.labelNumberNodes.setText(_translate("MainWindow", "0", None))
        self.tabPreferences.setTabText(self.tabPreferences.indexOf(self.tabOptions), _translate("MainWindow", "Preferences", None))
        self.tabPreferences.setTabText(self.tabPreferences.indexOf(self.tabInfo), _translate("MainWindow", "Info", None))
        self.progressBar.setFormat(_translate("MainWindow", "%p%", None))
        self.labelFeedback.setText(_translate("MainWindow", "Message", None))
        self.buttonAutoTrace.setToolTip(_translate("MainWindow", "Auto Update", None))
        self.buttonTrace.setToolTip(_translate("MainWindow", "Trace the raster content", None))
        self.buttonTrace.setText(_translate("MainWindow", "Trace", None))
        self.buttonTrace.setShortcut(_translate("MainWindow", "Return", None))
        self.buttonSave.setToolTip(_translate("MainWindow", "Save trace result to a file", None))
        self.buttonSave.setText(_translate("MainWindow", "Save", None))
        self.buttonHelp.setText(_translate("MainWindow", "Help", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menu_View.setTitle(_translate("MainWindow", "&View", None))
        self.actionOpenBitmap.setText(_translate("MainWindow", "Open Bitmap...", None))
        self.actionSaveAs.setText(_translate("MainWindow", "Save &As...", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt", None))
        self.actionBackground.setText(_translate("MainWindow", "&Background", None))
        self.actionBorder.setText(_translate("MainWindow", "Border &Frame", None))
        self.actionLoadPreset.setText(_translate("MainWindow", "Load Preset...", None))
        self.actionSavePreset.setText(_translate("MainWindow", "Save Preset...", None))
        self.actionTraceImage.setText(_translate("MainWindow", "Trace Image", None))

from . import mainwindow_rc
