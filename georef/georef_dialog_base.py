# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'georef/georef_dialog_base.ui'
#
# Created: Tue Mar 10 11:02:57 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_GeorefDialogBase(object):
    def setupUi(self, GeorefDialogBase):
        GeorefDialogBase.setObjectName(_fromUtf8("GeorefDialogBase"))
        GeorefDialogBase.resize(1274, 923)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeorefDialogBase.sizePolicy().hasHeightForWidth())
        GeorefDialogBase.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(GeorefDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(GeorefDialogBase)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.m_fileLabel = QtGui.QLabel(self.layoutWidget)
        self.m_fileLabel.setObjectName(_fromUtf8("m_fileLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.m_fileLabel)
        self.m_fileEdit = QtGui.QLineEdit(self.layoutWidget)
        self.m_fileEdit.setReadOnly(True)
        self.m_fileEdit.setObjectName(_fromUtf8("m_fileEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.m_fileEdit)
        self.m_siteLabel = QtGui.QLabel(self.layoutWidget)
        self.m_siteLabel.setObjectName(_fromUtf8("m_siteLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.m_siteLabel)
        self.m_siteEdit = QtGui.QLineEdit(self.layoutWidget)
        self.m_siteEdit.setReadOnly(False)
        self.m_siteEdit.setObjectName(_fromUtf8("m_siteEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.m_siteEdit)
        self.m_typeLabel = QtGui.QLabel(self.layoutWidget)
        self.m_typeLabel.setObjectName(_fromUtf8("m_typeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.m_typeLabel)
        self.m_typeCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_typeCombo.setObjectName(_fromUtf8("m_typeCombo"))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.m_typeCombo)
        self.m_contextLabel = QtGui.QLabel(self.layoutWidget)
        self.m_contextLabel.setObjectName(_fromUtf8("m_contextLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.m_contextLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.m_numberSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_numberSpin.setReadOnly(False)
        self.m_numberSpin.setMaximum(9999)
        self.m_numberSpin.setObjectName(_fromUtf8("m_numberSpin"))
        self.horizontalLayout_4.addWidget(self.m_numberSpin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.m_gridLabel = QtGui.QLabel(self.layoutWidget)
        self.m_gridLabel.setObjectName(_fromUtf8("m_gridLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.m_gridLabel)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.m_eastSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_eastSpin.setReadOnly(True)
        self.m_eastSpin.setMaximum(9999)
        self.m_eastSpin.setSingleStep(5)
        self.m_eastSpin.setObjectName(_fromUtf8("m_eastSpin"))
        self.horizontalLayout_6.addWidget(self.m_eastSpin)
        self.m_northSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_northSpin.setReadOnly(True)
        self.m_northSpin.setMaximum(9999)
        self.m_northSpin.setSingleStep(5)
        self.m_northSpin.setObjectName(_fromUtf8("m_northSpin"))
        self.horizontalLayout_6.addWidget(self.m_northSpin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.m_suffixLabel = QtGui.QLabel(self.layoutWidget)
        self.m_suffixLabel.setObjectName(_fromUtf8("m_suffixLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.m_suffixLabel)
        self.m_suffixEdit = QtGui.QLineEdit(self.layoutWidget)
        self.m_suffixEdit.setMaxLength(1)
        self.m_suffixEdit.setObjectName(_fromUtf8("m_suffixEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.m_suffixEdit)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.m_outputText = QtGui.QTextEdit(self.layoutWidget)
        self.m_outputText.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_outputText.sizePolicy().hasHeightForWidth())
        self.m_outputText.setSizePolicy(sizePolicy)
        self.m_outputText.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.m_outputText.setReadOnly(True)
        self.m_outputText.setObjectName(_fromUtf8("m_outputText"))
        self.verticalLayout_4.addWidget(self.m_outputText)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.m_runButton = QtGui.QPushButton(self.layoutWidget)
        self.m_runButton.setObjectName(_fromUtf8("m_runButton"))
        self.horizontalLayout_5.addWidget(self.m_runButton)
        self.m_closeButton = QtGui.QPushButton(self.layoutWidget)
        self.m_closeButton.setObjectName(_fromUtf8("m_closeButton"))
        self.horizontalLayout_5.addWidget(self.m_closeButton)
        self.m_runCloseButton = QtGui.QPushButton(self.layoutWidget)
        self.m_runCloseButton.setDefault(True)
        self.m_runCloseButton.setObjectName(_fromUtf8("m_runCloseButton"))
        self.horizontalLayout_5.addWidget(self.m_runCloseButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.m_progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.m_progressBar.setObjectName(_fromUtf8("m_progressBar"))
        self.verticalLayout_4.addWidget(self.m_progressBar)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gcpWidget1 = GcpWidget(self.layoutWidget1)
        self.gcpWidget1.setObjectName(_fromUtf8("gcpWidget1"))
        self.gridLayout.addWidget(self.gcpWidget1, 0, 0, 1, 1)
        self.gcpWidget2 = GcpWidget(self.layoutWidget1)
        self.gcpWidget2.setObjectName(_fromUtf8("gcpWidget2"))
        self.gridLayout.addWidget(self.gcpWidget2, 1, 0, 1, 1)
        self.gcpWidget3 = GcpWidget(self.layoutWidget1)
        self.gcpWidget3.setObjectName(_fromUtf8("gcpWidget3"))
        self.gridLayout.addWidget(self.gcpWidget3, 1, 1, 1, 1)
        self.planView = GeorefGraphicsView(self.layoutWidget1)
        self.planView.setObjectName(_fromUtf8("planView"))
        self.gridLayout.addWidget(self.planView, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.m_fileLabel.setBuddy(self.m_fileEdit)
        self.m_contextLabel.setBuddy(self.m_numberSpin)
        self.m_gridLabel.setBuddy(self.m_eastSpin)

        self.retranslateUi(GeorefDialogBase)
        QtCore.QMetaObject.connectSlotsByName(GeorefDialogBase)
        GeorefDialogBase.setTabOrder(self.m_runCloseButton, self.m_runButton)
        GeorefDialogBase.setTabOrder(self.m_runButton, self.m_closeButton)

    def retranslateUi(self, GeorefDialogBase):
        GeorefDialogBase.setWindowTitle(_translate("GeorefDialogBase", "Dialog", None))
        self.m_fileLabel.setText(_translate("GeorefDialogBase", "Plan file:", None))
        self.m_siteLabel.setText(_translate("GeorefDialogBase", "Site:", None))
        self.m_typeLabel.setText(_translate("GeorefDialogBase", "Type:", None))
        self.m_typeCombo.setItemText(0, _translate("GeorefDialogBase", "Context", None))
        self.m_typeCombo.setItemText(1, _translate("GeorefDialogBase", "Plan", None))
        self.m_typeCombo.setItemText(2, _translate("GeorefDialogBase", "Section", None))
        self.m_typeCombo.setItemText(3, _translate("GeorefDialogBase", "Matrix", None))
        self.m_contextLabel.setText(_translate("GeorefDialogBase", "Number:", None))
        self.m_numberSpin.setToolTip(_translate("GeorefDialogBase", "Context Number", None))
        self.m_gridLabel.setText(_translate("GeorefDialogBase", "Grid:", None))
        self.m_suffixLabel.setText(_translate("GeorefDialogBase", "Suffix:", None))
        self.m_runButton.setText(_translate("GeorefDialogBase", "Run", None))
        self.m_closeButton.setText(_translate("GeorefDialogBase", "Close", None))
        self.m_runCloseButton.setText(_translate("GeorefDialogBase", "Run and Close", None))

from georef_graphics_view import GeorefGraphicsView
from gcp_widget import GcpWidget
