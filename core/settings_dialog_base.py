# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/settings_dialog_base.ui'
#
# Created: Wed Apr  8 09:00:29 2015
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

class Ui_SettingsDialogBase(object):
    def setupUi(self, SettingsDialogBase):
        SettingsDialogBase.setObjectName(_fromUtf8("SettingsDialogBase"))
        SettingsDialogBase.resize(534, 371)
        self.gridLayout = QtGui.QGridLayout(SettingsDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.planFolderEdit = QtGui.QLineEdit(SettingsDialogBase)
        self.planFolderEdit.setObjectName(_fromUtf8("planFolderEdit"))
        self.horizontalLayout_2.addWidget(self.planFolderEdit)
        self.planFolderButton = QtGui.QPushButton(SettingsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planFolderButton.sizePolicy().hasHeightForWidth())
        self.planFolderButton.setSizePolicy(sizePolicy)
        self.planFolderButton.setObjectName(_fromUtf8("planFolderButton"))
        self.horizontalLayout_2.addWidget(self.planFolderButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.separatePlansLabel = QtGui.QLabel(SettingsDialogBase)
        self.separatePlansLabel.setObjectName(_fromUtf8("separatePlansLabel"))
        self.gridLayout.addWidget(self.separatePlansLabel, 7, 0, 1, 1)
        self.planTransparencyLabel = QtGui.QLabel(SettingsDialogBase)
        self.planTransparencyLabel.setObjectName(_fromUtf8("planTransparencyLabel"))
        self.gridLayout.addWidget(self.planTransparencyLabel, 8, 0, 1, 1)
        self.siteCodeLabel = QtGui.QLabel(SettingsDialogBase)
        self.siteCodeLabel.setObjectName(_fromUtf8("siteCodeLabel"))
        self.gridLayout.addWidget(self.siteCodeLabel, 0, 0, 1, 1)
        self.siteCodeEdit = QtGui.QLineEdit(SettingsDialogBase)
        self.siteCodeEdit.setObjectName(_fromUtf8("siteCodeEdit"))
        self.gridLayout.addWidget(self.siteCodeEdit, 0, 1, 1, 1)
        self.dataFolderLabel = QtGui.QLabel(SettingsDialogBase)
        self.dataFolderLabel.setObjectName(_fromUtf8("dataFolderLabel"))
        self.gridLayout.addWidget(self.dataFolderLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dataFolderEdit = QtGui.QLineEdit(SettingsDialogBase)
        self.dataFolderEdit.setObjectName(_fromUtf8("dataFolderEdit"))
        self.horizontalLayout.addWidget(self.dataFolderEdit)
        self.dataFolderButton = QtGui.QPushButton(SettingsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFolderButton.sizePolicy().hasHeightForWidth())
        self.dataFolderButton.setSizePolicy(sizePolicy)
        self.dataFolderButton.setObjectName(_fromUtf8("dataFolderButton"))
        self.horizontalLayout.addWidget(self.dataFolderButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.gridFolderLabel = QtGui.QLabel(SettingsDialogBase)
        self.gridFolderLabel.setObjectName(_fromUtf8("gridFolderLabel"))
        self.gridLayout.addWidget(self.gridFolderLabel, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridFolderEdit = QtGui.QLineEdit(SettingsDialogBase)
        self.gridFolderEdit.setObjectName(_fromUtf8("gridFolderEdit"))
        self.horizontalLayout_3.addWidget(self.gridFolderEdit)
        self.gridFolderButton = QtGui.QPushButton(SettingsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFolderButton.sizePolicy().hasHeightForWidth())
        self.gridFolderButton.setSizePolicy(sizePolicy)
        self.gridFolderButton.setObjectName(_fromUtf8("gridFolderButton"))
        self.horizontalLayout_3.addWidget(self.gridFolderButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.prependSiteCodeLabel = QtGui.QLabel(SettingsDialogBase)
        self.prependSiteCodeLabel.setObjectName(_fromUtf8("prependSiteCodeLabel"))
        self.gridLayout.addWidget(self.prependSiteCodeLabel, 5, 0, 1, 1)
        self.prependSiteCodeCheck = QtGui.QCheckBox(SettingsDialogBase)
        self.prependSiteCodeCheck.setText(_fromUtf8(""))
        self.prependSiteCodeCheck.setChecked(True)
        self.prependSiteCodeCheck.setObjectName(_fromUtf8("prependSiteCodeCheck"))
        self.gridLayout.addWidget(self.prependSiteCodeCheck, 5, 1, 1, 1)
        self.planFolderLabel = QtGui.QLabel(SettingsDialogBase)
        self.planFolderLabel.setObjectName(_fromUtf8("planFolderLabel"))
        self.gridLayout.addWidget(self.planFolderLabel, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.styleFolderEdit = QtGui.QLineEdit(SettingsDialogBase)
        self.styleFolderEdit.setEnabled(False)
        self.styleFolderEdit.setObjectName(_fromUtf8("styleFolderEdit"))
        self.horizontalLayout_5.addWidget(self.styleFolderEdit)
        self.styleFolderButton = QtGui.QPushButton(SettingsDialogBase)
        self.styleFolderButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.styleFolderButton.sizePolicy().hasHeightForWidth())
        self.styleFolderButton.setSizePolicy(sizePolicy)
        self.styleFolderButton.setObjectName(_fromUtf8("styleFolderButton"))
        self.horizontalLayout_5.addWidget(self.styleFolderButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.planTransparencySpin = QtGui.QSpinBox(SettingsDialogBase)
        self.planTransparencySpin.setMaximum(100)
        self.planTransparencySpin.setProperty("value", 50)
        self.planTransparencySpin.setObjectName(_fromUtf8("planTransparencySpin"))
        self.horizontalLayout_4.addWidget(self.planTransparencySpin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)
        self.separatePlansCheck = QtGui.QCheckBox(SettingsDialogBase)
        self.separatePlansCheck.setText(_fromUtf8(""))
        self.separatePlansCheck.setChecked(True)
        self.separatePlansCheck.setObjectName(_fromUtf8("separatePlansCheck"))
        self.gridLayout.addWidget(self.separatePlansCheck, 7, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 0, 1, 2)
        self.defaultStylesCheck = QtGui.QCheckBox(SettingsDialogBase)
        self.defaultStylesCheck.setText(_fromUtf8(""))
        self.defaultStylesCheck.setChecked(True)
        self.defaultStylesCheck.setObjectName(_fromUtf8("defaultStylesCheck"))
        self.gridLayout.addWidget(self.defaultStylesCheck, 3, 1, 1, 1)
        self.defaultStylesLabel = QtGui.QLabel(SettingsDialogBase)
        self.defaultStylesLabel.setObjectName(_fromUtf8("defaultStylesLabel"))
        self.gridLayout.addWidget(self.defaultStylesLabel, 3, 0, 1, 1)
        self.customStylesLabel = QtGui.QLabel(SettingsDialogBase)
        self.customStylesLabel.setObjectName(_fromUtf8("customStylesLabel"))
        self.gridLayout.addWidget(self.customStylesLabel, 4, 0, 1, 1)
        self.separatePlansLabel.setBuddy(self.separatePlansCheck)
        self.planTransparencyLabel.setBuddy(self.planTransparencySpin)
        self.siteCodeLabel.setBuddy(self.siteCodeEdit)
        self.dataFolderLabel.setBuddy(self.dataFolderEdit)
        self.prependSiteCodeLabel.setBuddy(self.prependSiteCodeCheck)
        self.planFolderLabel.setBuddy(self.planFolderEdit)

        self.retranslateUi(SettingsDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialogBase)
        SettingsDialogBase.setTabOrder(self.siteCodeEdit, self.dataFolderEdit)
        SettingsDialogBase.setTabOrder(self.dataFolderEdit, self.dataFolderButton)
        SettingsDialogBase.setTabOrder(self.dataFolderButton, self.prependSiteCodeCheck)
        SettingsDialogBase.setTabOrder(self.prependSiteCodeCheck, self.planFolderEdit)
        SettingsDialogBase.setTabOrder(self.planFolderEdit, self.planFolderButton)
        SettingsDialogBase.setTabOrder(self.planFolderButton, self.separatePlansCheck)
        SettingsDialogBase.setTabOrder(self.separatePlansCheck, self.planTransparencySpin)
        SettingsDialogBase.setTabOrder(self.planTransparencySpin, self.buttonBox)

    def retranslateUi(self, SettingsDialogBase):
        SettingsDialogBase.setWindowTitle(_translate("SettingsDialogBase", "Settings", None))
        self.planFolderButton.setText(_translate("SettingsDialogBase", "...", None))
        self.separatePlansLabel.setText(_translate("SettingsDialogBase", "Separate plan folders:", None))
        self.planTransparencyLabel.setText(_translate("SettingsDialogBase", "Plan tranparency:", None))
        self.siteCodeLabel.setText(_translate("SettingsDialogBase", "Site Code:", None))
        self.dataFolderLabel.setText(_translate("SettingsDialogBase", "Data Folder:", None))
        self.dataFolderButton.setText(_translate("SettingsDialogBase", "...", None))
        self.gridFolderLabel.setText(_translate("SettingsDialogBase", "Grid Folder:", None))
        self.gridFolderButton.setText(_translate("SettingsDialogBase", "...", None))
        self.prependSiteCodeLabel.setText(_translate("SettingsDialogBase", "Prepend site code:", None))
        self.planFolderLabel.setText(_translate("SettingsDialogBase", "Plan Folder:", None))
        self.styleFolderButton.setText(_translate("SettingsDialogBase", "...", None))
        self.planTransparencySpin.setSuffix(_translate("SettingsDialogBase", "%", None))
        self.separatePlansCheck.setToolTip(_translate("SettingsDialogBase", "Select if the raw and processed plans should be stored in separate folders.", None))
        self.defaultStylesLabel.setText(_translate("SettingsDialogBase", "Use Default Styles:", None))
        self.customStylesLabel.setText(_translate("SettingsDialogBase", "Custom Styles Folder:", None))

