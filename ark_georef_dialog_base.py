# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ark_georef_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.3
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

class Ui_ArkGeorefDialogBase(object):
    def setupUi(self, ArkGeorefDialogBase):
        ArkGeorefDialogBase.setObjectName(_fromUtf8("ArkGeorefDialogBase"))
        ArkGeorefDialogBase.resize(1274, 923)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ArkGeorefDialogBase.sizePolicy().hasHeightForWidth())
        ArkGeorefDialogBase.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(ArkGeorefDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(ArkGeorefDialogBase)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.m_runButton = QtGui.QPushButton(self.widget)
        self.m_runButton.setObjectName(_fromUtf8("m_runButton"))
        self.horizontalLayout_5.addWidget(self.m_runButton)
        self.m_closeButton = QtGui.QPushButton(self.widget)
        self.m_closeButton.setObjectName(_fromUtf8("m_closeButton"))
        self.horizontalLayout_5.addWidget(self.m_closeButton)
        self.m_runCloseButton = QtGui.QPushButton(self.widget)
        self.m_runCloseButton.setDefault(True)
        self.m_runCloseButton.setObjectName(_fromUtf8("m_runCloseButton"))
        self.horizontalLayout_5.addWidget(self.m_runCloseButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.m_fileLabel = QtGui.QLabel(self.widget)
        self.m_fileLabel.setObjectName(_fromUtf8("m_fileLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.m_fileLabel)
        self.m_fileEdit = QtGui.QLineEdit(self.widget)
        self.m_fileEdit.setReadOnly(True)
        self.m_fileEdit.setObjectName(_fromUtf8("m_fileEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.m_fileEdit)
        self.m_siteLabel = QtGui.QLabel(self.widget)
        self.m_siteLabel.setObjectName(_fromUtf8("m_siteLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.m_siteLabel)
        self.m_siteEdit = QtGui.QLineEdit(self.widget)
        self.m_siteEdit.setReadOnly(False)
        self.m_siteEdit.setObjectName(_fromUtf8("m_siteEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.m_siteEdit)
        self.m_contextLabel = QtGui.QLabel(self.widget)
        self.m_contextLabel.setObjectName(_fromUtf8("m_contextLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.m_contextLabel)
        self.m_gridLabel = QtGui.QLabel(self.widget)
        self.m_gridLabel.setObjectName(_fromUtf8("m_gridLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.m_gridLabel)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.m_eastSpin = QtGui.QSpinBox(self.widget)
        self.m_eastSpin.setReadOnly(True)
        self.m_eastSpin.setMaximum(9999)
        self.m_eastSpin.setSingleStep(5)
        self.m_eastSpin.setObjectName(_fromUtf8("m_eastSpin"))
        self.horizontalLayout_6.addWidget(self.m_eastSpin)
        self.m_northSpin = QtGui.QSpinBox(self.widget)
        self.m_northSpin.setReadOnly(True)
        self.m_northSpin.setMaximum(9999)
        self.m_northSpin.setSingleStep(5)
        self.m_northSpin.setObjectName(_fromUtf8("m_northSpin"))
        self.horizontalLayout_6.addWidget(self.m_northSpin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.m_typeCombo = QtGui.QComboBox(self.widget)
        self.m_typeCombo.setObjectName(_fromUtf8("m_typeCombo"))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.m_typeCombo)
        self.m_typeLabel = QtGui.QLabel(self.widget)
        self.m_typeLabel.setObjectName(_fromUtf8("m_typeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.m_typeLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.m_numberSpin = QtGui.QSpinBox(self.widget)
        self.m_numberSpin.setReadOnly(False)
        self.m_numberSpin.setMaximum(9999)
        self.m_numberSpin.setObjectName(_fromUtf8("m_numberSpin"))
        self.horizontalLayout_4.addWidget(self.m_numberSpin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.m_suffixEdit = QtGui.QLineEdit(self.widget)
        self.m_suffixEdit.setMaxLength(1)
        self.m_suffixEdit.setObjectName(_fromUtf8("m_suffixEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.m_suffixEdit)
        self.m_suffixLabel = QtGui.QLabel(self.widget)
        self.m_suffixLabel.setObjectName(_fromUtf8("m_suffixLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.m_suffixLabel)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.m_gcpTable = QtGui.QTableWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_gcpTable.sizePolicy().hasHeightForWidth())
        self.m_gcpTable.setSizePolicy(sizePolicy)
        self.m_gcpTable.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.m_gcpTable.setFont(font)
        self.m_gcpTable.setRowCount(3)
        self.m_gcpTable.setColumnCount(6)
        self.m_gcpTable.setObjectName(_fromUtf8("m_gcpTable"))
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        self.m_gcpTable.setItem(2, 5, item)
        self.m_gcpTable.horizontalHeader().setDefaultSectionSize(70)
        self.m_gcpTable.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout_4.addWidget(self.m_gcpTable)
        self.m_outputText = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_outputText.sizePolicy().hasHeightForWidth())
        self.m_outputText.setSizePolicy(sizePolicy)
        self.m_outputText.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.m_outputText.setReadOnly(True)
        self.m_outputText.setObjectName(_fromUtf8("m_outputText"))
        self.verticalLayout_4.addWidget(self.m_outputText)
        self.m_progressBar = QtGui.QProgressBar(self.widget)
        self.m_progressBar.setObjectName(_fromUtf8("m_progressBar"))
        self.verticalLayout_4.addWidget(self.m_progressBar)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.m_gridLabel1 = QtGui.QLabel(self.widget1)
        self.m_gridLabel1.setObjectName(_fromUtf8("m_gridLabel1"))
        self.horizontalLayout.addWidget(self.m_gridLabel1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.m_autoButton1 = QtGui.QPushButton(self.widget1)
        self.m_autoButton1.setEnabled(False)
        self.m_autoButton1.setObjectName(_fromUtf8("m_autoButton1"))
        self.horizontalLayout.addWidget(self.m_autoButton1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.m_gridView1 = ArkGeorefGraphicsView(self.widget1)
        self.m_gridView1.setInteractive(False)
        self.m_gridView1.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.m_gridView1.setObjectName(_fromUtf8("m_gridView1"))
        self.verticalLayout.addWidget(self.m_gridView1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.m_fullPlanLabel = QtGui.QLabel(self.widget1)
        self.m_fullPlanLabel.setObjectName(_fromUtf8("m_fullPlanLabel"))
        self.horizontalLayout_7.addWidget(self.m_fullPlanLabel)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.m_autoAllButton = QtGui.QPushButton(self.widget1)
        self.m_autoAllButton.setEnabled(False)
        self.m_autoAllButton.setObjectName(_fromUtf8("m_autoAllButton"))
        self.horizontalLayout_7.addWidget(self.m_autoAllButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.m_planView = ArkGeorefGraphicsView(self.widget1)
        self.m_planView.setInteractive(False)
        self.m_planView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.m_planView.setObjectName(_fromUtf8("m_planView"))
        self.verticalLayout_6.addWidget(self.m_planView)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.m_gridLabel2 = QtGui.QLabel(self.widget1)
        self.m_gridLabel2.setObjectName(_fromUtf8("m_gridLabel2"))
        self.horizontalLayout_2.addWidget(self.m_gridLabel2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.m_autoButton2 = QtGui.QPushButton(self.widget1)
        self.m_autoButton2.setEnabled(False)
        self.m_autoButton2.setObjectName(_fromUtf8("m_autoButton2"))
        self.horizontalLayout_2.addWidget(self.m_autoButton2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.m_gridView2 = ArkGeorefGraphicsView(self.widget1)
        self.m_gridView2.setInteractive(False)
        self.m_gridView2.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.m_gridView2.setObjectName(_fromUtf8("m_gridView2"))
        self.verticalLayout_2.addWidget(self.m_gridView2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.m_gridLabel3 = QtGui.QLabel(self.widget1)
        self.m_gridLabel3.setObjectName(_fromUtf8("m_gridLabel3"))
        self.horizontalLayout_3.addWidget(self.m_gridLabel3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.m_autoButton3 = QtGui.QPushButton(self.widget1)
        self.m_autoButton3.setEnabled(False)
        self.m_autoButton3.setObjectName(_fromUtf8("m_autoButton3"))
        self.horizontalLayout_3.addWidget(self.m_autoButton3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.m_gridView3 = ArkGeorefGraphicsView(self.widget1)
        self.m_gridView3.setInteractive(False)
        self.m_gridView3.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.m_gridView3.setObjectName(_fromUtf8("m_gridView3"))
        self.verticalLayout_3.addWidget(self.m_gridView3)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.m_fileLabel.setBuddy(self.m_fileEdit)
        self.m_contextLabel.setBuddy(self.m_numberSpin)
        self.m_gridLabel.setBuddy(self.m_eastSpin)

        self.retranslateUi(ArkGeorefDialogBase)
        QtCore.QMetaObject.connectSlotsByName(ArkGeorefDialogBase)
        ArkGeorefDialogBase.setTabOrder(self.m_gridView1, self.m_gridView2)
        ArkGeorefDialogBase.setTabOrder(self.m_gridView2, self.m_gridView3)
        ArkGeorefDialogBase.setTabOrder(self.m_gridView3, self.m_runCloseButton)
        ArkGeorefDialogBase.setTabOrder(self.m_runCloseButton, self.m_runButton)
        ArkGeorefDialogBase.setTabOrder(self.m_runButton, self.m_closeButton)
        ArkGeorefDialogBase.setTabOrder(self.m_closeButton, self.m_autoButton1)
        ArkGeorefDialogBase.setTabOrder(self.m_autoButton1, self.m_autoButton2)
        ArkGeorefDialogBase.setTabOrder(self.m_autoButton2, self.m_autoButton3)

    def retranslateUi(self, ArkGeorefDialogBase):
        ArkGeorefDialogBase.setWindowTitle(_translate("ArkGeorefDialogBase", "Dialog", None))
        self.m_runButton.setText(_translate("ArkGeorefDialogBase", "Run", None))
        self.m_closeButton.setText(_translate("ArkGeorefDialogBase", "Close", None))
        self.m_runCloseButton.setText(_translate("ArkGeorefDialogBase", "Run and Close", None))
        self.m_fileLabel.setText(_translate("ArkGeorefDialogBase", "Plan file:", None))
        self.m_siteLabel.setText(_translate("ArkGeorefDialogBase", "Site:", None))
        self.m_contextLabel.setText(_translate("ArkGeorefDialogBase", "Number:", None))
        self.m_gridLabel.setText(_translate("ArkGeorefDialogBase", "Grid:", None))
        self.m_typeCombo.setItemText(0, _translate("ArkGeorefDialogBase", "Context", None))
        self.m_typeCombo.setItemText(1, _translate("ArkGeorefDialogBase", "Plan", None))
        self.m_typeCombo.setItemText(2, _translate("ArkGeorefDialogBase", "Section", None))
        self.m_typeCombo.setItemText(3, _translate("ArkGeorefDialogBase", "Matrix", None))
        self.m_typeLabel.setText(_translate("ArkGeorefDialogBase", "Type:", None))
        self.m_numberSpin.setToolTip(_translate("ArkGeorefDialogBase", "Context Number", None))
        self.m_suffixLabel.setText(_translate("ArkGeorefDialogBase", "Suffix:", None))
        item = self.m_gcpTable.verticalHeaderItem(0)
        item.setText(_translate("ArkGeorefDialogBase", "GCP1", None))
        item = self.m_gcpTable.verticalHeaderItem(1)
        item.setText(_translate("ArkGeorefDialogBase", "GCP2", None))
        item = self.m_gcpTable.verticalHeaderItem(2)
        item.setText(_translate("ArkGeorefDialogBase", "GCP3", None))
        item = self.m_gcpTable.horizontalHeaderItem(0)
        item.setText(_translate("ArkGeorefDialogBase", "Raw X", None))
        item = self.m_gcpTable.horizontalHeaderItem(1)
        item.setText(_translate("ArkGeorefDialogBase", "Raw Y", None))
        item = self.m_gcpTable.horizontalHeaderItem(2)
        item.setText(_translate("ArkGeorefDialogBase", "Grid X", None))
        item = self.m_gcpTable.horizontalHeaderItem(3)
        item.setText(_translate("ArkGeorefDialogBase", "Grid Y", None))
        item = self.m_gcpTable.horizontalHeaderItem(4)
        item.setText(_translate("ArkGeorefDialogBase", "Geo X", None))
        item = self.m_gcpTable.horizontalHeaderItem(5)
        item.setText(_translate("ArkGeorefDialogBase", "Geo Y", None))
        __sortingEnabled = self.m_gcpTable.isSortingEnabled()
        self.m_gcpTable.setSortingEnabled(False)
        item = self.m_gcpTable.item(0, 0)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(0, 1)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(0, 2)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(0, 3)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(0, 4)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(0, 5)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 0)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 1)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 2)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 3)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 4)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(1, 5)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 0)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 1)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 2)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 3)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 4)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        item = self.m_gcpTable.item(2, 5)
        item.setText(_translate("ArkGeorefDialogBase", "0", None))
        self.m_gcpTable.setSortingEnabled(__sortingEnabled)
        self.m_gridLabel1.setText(_translate("ArkGeorefDialogBase", "000 / 000 :", None))
        self.m_autoButton1.setText(_translate("ArkGeorefDialogBase", "Auto", None))
        self.m_fullPlanLabel.setText(_translate("ArkGeorefDialogBase", "Full Plan", None))
        self.m_autoAllButton.setText(_translate("ArkGeorefDialogBase", "Auto All", None))
        self.m_gridLabel2.setText(_translate("ArkGeorefDialogBase", "000 / 000 :", None))
        self.m_autoButton2.setText(_translate("ArkGeorefDialogBase", "Auto", None))
        self.m_gridLabel3.setText(_translate("ArkGeorefDialogBase", "000 / 000 :", None))
        self.m_autoButton3.setText(_translate("ArkGeorefDialogBase", "Auto", None))

from ark_georef_graphics_view import ArkGeorefGraphicsView
