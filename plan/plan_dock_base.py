# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan/plan_dock_base.ui'
#
# Created: Wed May 20 08:54:08 2015
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

class Ui_PlanDockWidget(object):
    def setupUi(self, PlanDockWidget):
        PlanDockWidget.setObjectName(_fromUtf8("PlanDockWidget"))
        PlanDockWidget.resize(357, 881)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlanDockWidget.sizePolicy().hasHeightForWidth())
        PlanDockWidget.setSizePolicy(sizePolicy)
        self.PlanDockContents = QtGui.QWidget()
        self.PlanDockContents.setObjectName(_fromUtf8("PlanDockContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.PlanDockContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.PlanDockContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 333, 829))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.m_loadRawButton = QtGui.QPushButton(self.groupBox_2)
        self.m_loadRawButton.setObjectName(_fromUtf8("m_loadRawButton"))
        self.gridLayout_2.addWidget(self.m_loadRawButton, 0, 0, 1, 1)
        self.m_loadGeoButton = QtGui.QPushButton(self.groupBox_2)
        self.m_loadGeoButton.setObjectName(_fromUtf8("m_loadGeoButton"))
        self.gridLayout_2.addWidget(self.m_loadGeoButton, 0, 1, 1, 1)
        self.m_loadContextButton = QtGui.QPushButton(self.groupBox_2)
        self.m_loadContextButton.setObjectName(_fromUtf8("m_loadContextButton"))
        self.gridLayout_2.addWidget(self.m_loadContextButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.m_planGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.m_planGroup.setObjectName(_fromUtf8("m_planGroup"))
        self.formLayout = QtGui.QFormLayout(self.m_planGroup)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.m_siteLabel = QtGui.QLabel(self.m_planGroup)
        self.m_siteLabel.setObjectName(_fromUtf8("m_siteLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.m_siteLabel)
        self.m_siteEdit = QtGui.QLineEdit(self.m_planGroup)
        self.m_siteEdit.setReadOnly(False)
        self.m_siteEdit.setObjectName(_fromUtf8("m_siteEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.m_siteEdit)
        self.m_numberLabel = QtGui.QLabel(self.m_planGroup)
        self.m_numberLabel.setObjectName(_fromUtf8("m_numberLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.m_numberLabel)
        self.m_numberSpin = QtGui.QSpinBox(self.m_planGroup)
        self.m_numberSpin.setMaximum(9999)
        self.m_numberSpin.setObjectName(_fromUtf8("m_numberSpin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.m_numberSpin)
        self.m_sourceEdit = QtGui.QLineEdit(self.m_planGroup)
        self.m_sourceEdit.setObjectName(_fromUtf8("m_sourceEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.m_sourceEdit)
        self.m_sourceLabel = QtGui.QLabel(self.m_planGroup)
        self.m_sourceLabel.setObjectName(_fromUtf8("m_sourceLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.m_sourceLabel)
        self.m_commentEdit = QtGui.QLineEdit(self.m_planGroup)
        self.m_commentEdit.setReadOnly(False)
        self.m_commentEdit.setObjectName(_fromUtf8("m_commentEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.m_commentEdit)
        self.m_commentLabel = QtGui.QLabel(self.m_planGroup)
        self.m_commentLabel.setObjectName(_fromUtf8("m_commentLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.m_commentLabel)
        self.m_sourceFileLabel = QtGui.QLabel(self.m_planGroup)
        self.m_sourceFileLabel.setObjectName(_fromUtf8("m_sourceFileLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.m_sourceFileLabel)
        self.m_sourceFileEdit = QtGui.QLineEdit(self.m_planGroup)
        self.m_sourceFileEdit.setObjectName(_fromUtf8("m_sourceFileEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.m_sourceFileEdit)
        self.m_createdByLabel = QtGui.QLabel(self.m_planGroup)
        self.m_createdByLabel.setObjectName(_fromUtf8("m_createdByLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.m_createdByLabel)
        self.m_createdByEdit = QtGui.QLineEdit(self.m_planGroup)
        self.m_createdByEdit.setObjectName(_fromUtf8("m_createdByEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.m_createdByEdit)
        self.verticalLayout.addWidget(self.m_planGroup)
        self.m_drawingToolsGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.m_drawingToolsGroup.setObjectName(_fromUtf8("m_drawingToolsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.m_drawingToolsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.m_levelTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_levelTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_levelTool.setCheckable(True)
        self.m_levelTool.setObjectName(_fromUtf8("m_levelTool"))
        self.m_toolButtonGroup = QtGui.QButtonGroup(PlanDockWidget)
        self.m_toolButtonGroup.setObjectName(_fromUtf8("m_toolButtonGroup"))
        self.m_toolButtonGroup.addButton(self.m_levelTool)
        self.gridLayout.addWidget(self.m_levelTool, 6, 2, 1, 1)
        self.m_extentTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_extentTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_extentTool.setCheckable(True)
        self.m_extentTool.setObjectName(_fromUtf8("m_extentTool"))
        self.m_toolButtonGroup.addButton(self.m_extentTool)
        self.gridLayout.addWidget(self.m_extentTool, 0, 2, 1, 1)
        self.m_cbmTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_cbmTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_cbmTool.setCheckable(True)
        self.m_cbmTool.setObjectName(_fromUtf8("m_cbmTool"))
        self.m_toolButtonGroup.addButton(self.m_cbmTool)
        self.gridLayout.addWidget(self.m_cbmTool, 4, 2, 1, 1)
        self.m_brickTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_brickTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_brickTool.setCheckable(True)
        self.m_brickTool.setObjectName(_fromUtf8("m_brickTool"))
        self.m_toolButtonGroup.addButton(self.m_brickTool)
        self.gridLayout.addWidget(self.m_brickTool, 4, 3, 1, 1)
        self.m_undercutTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_undercutTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_undercutTool.setCheckable(True)
        self.m_undercutTool.setObjectName(_fromUtf8("m_undercutTool"))
        self.m_toolButtonGroup.addButton(self.m_undercutTool)
        self.gridLayout.addWidget(self.m_undercutTool, 3, 3, 1, 1)
        self.m_uncertainEdgeTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_uncertainEdgeTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_uncertainEdgeTool.setCheckable(True)
        self.m_uncertainEdgeTool.setObjectName(_fromUtf8("m_uncertainEdgeTool"))
        self.m_toolButtonGroup.addButton(self.m_uncertainEdgeTool)
        self.gridLayout.addWidget(self.m_uncertainEdgeTool, 0, 4, 1, 1)
        self.m_sectionLineTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_sectionLineTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_sectionLineTool.setCheckable(True)
        self.m_sectionLineTool.setObjectName(_fromUtf8("m_sectionLineTool"))
        self.gridLayout.addWidget(self.m_sectionLineTool, 7, 3, 1, 1)
        self.m_limitOfExcavationTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_limitOfExcavationTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_limitOfExcavationTool.setCheckable(True)
        self.m_limitOfExcavationTool.setObjectName(_fromUtf8("m_limitOfExcavationTool"))
        self.m_toolButtonGroup.addButton(self.m_limitOfExcavationTool)
        self.gridLayout.addWidget(self.m_limitOfExcavationTool, 0, 5, 1, 1)
        self.m_verticalBreakOfSlopeTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_verticalBreakOfSlopeTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_verticalBreakOfSlopeTool.setCheckable(True)
        self.m_verticalBreakOfSlopeTool.setObjectName(_fromUtf8("m_verticalBreakOfSlopeTool"))
        self.m_toolButtonGroup.addButton(self.m_verticalBreakOfSlopeTool)
        self.gridLayout.addWidget(self.m_verticalBreakOfSlopeTool, 2, 5, 1, 1)
        self.m_returnOfSlopeTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_returnOfSlopeTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_returnOfSlopeTool.setCheckable(True)
        self.m_returnOfSlopeTool.setObjectName(_fromUtf8("m_returnOfSlopeTool"))
        self.m_toolButtonGroup.addButton(self.m_returnOfSlopeTool)
        self.gridLayout.addWidget(self.m_returnOfSlopeTool, 3, 4, 1, 1)
        self.m_mortarTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_mortarTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_mortarTool.setCheckable(True)
        self.m_mortarTool.setObjectName(_fromUtf8("m_mortarTool"))
        self.m_toolButtonGroup.addButton(self.m_mortarTool)
        self.gridLayout.addWidget(self.m_mortarTool, 4, 5, 1, 1)
        self.m_hachureTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_hachureTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_hachureTool.setCheckable(True)
        self.m_hachureTool.setObjectName(_fromUtf8("m_hachureTool"))
        self.m_toolButtonGroup.addButton(self.m_hachureTool)
        self.gridLayout.addWidget(self.m_hachureTool, 3, 2, 1, 1)
        self.m_schematicTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_schematicTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_schematicTool.setCheckable(True)
        self.m_schematicTool.setObjectName(_fromUtf8("m_schematicTool"))
        self.m_toolButtonGroup.addButton(self.m_schematicTool)
        self.gridLayout.addWidget(self.m_schematicTool, 6, 3, 1, 1)
        self.m_charcoalTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_charcoalTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_charcoalTool.setCheckable(True)
        self.m_charcoalTool.setObjectName(_fromUtf8("m_charcoalTool"))
        self.m_toolButtonGroup.addButton(self.m_charcoalTool)
        self.gridLayout.addWidget(self.m_charcoalTool, 5, 2, 1, 1)
        self.m_breakOfSlopeTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_breakOfSlopeTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_breakOfSlopeTool.setCheckable(True)
        self.m_breakOfSlopeTool.setObjectName(_fromUtf8("m_breakOfSlopeTool"))
        self.m_toolButtonGroup.addButton(self.m_breakOfSlopeTool)
        self.gridLayout.addWidget(self.m_breakOfSlopeTool, 2, 4, 1, 1)
        self.m_sectionPinTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_sectionPinTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_sectionPinTool.setCheckable(True)
        self.m_sectionPinTool.setObjectName(_fromUtf8("m_sectionPinTool"))
        self.gridLayout.addWidget(self.m_sectionPinTool, 7, 2, 1, 1)
        self.m_verticalEdgeTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_verticalEdgeTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_verticalEdgeTool.setCheckable(True)
        self.m_verticalEdgeTool.setObjectName(_fromUtf8("m_verticalEdgeTool"))
        self.m_toolButtonGroup.addButton(self.m_verticalEdgeTool)
        self.gridLayout.addWidget(self.m_verticalEdgeTool, 0, 3, 1, 1)
        self.m_clearTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_clearTool.setEnabled(True)
        self.m_clearTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_clearTool.setObjectName(_fromUtf8("m_clearTool"))
        self.m_toolButtonGroup.addButton(self.m_clearTool)
        self.gridLayout.addWidget(self.m_clearTool, 6, 4, 1, 1)
        self.m_potTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_potTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_potTool.setCheckable(True)
        self.m_potTool.setObjectName(_fromUtf8("m_potTool"))
        self.m_toolButtonGroup.addButton(self.m_potTool)
        self.gridLayout.addWidget(self.m_potTool, 5, 4, 1, 1)
        self.m_stoneTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_stoneTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_stoneTool.setCheckable(True)
        self.m_stoneTool.setObjectName(_fromUtf8("m_stoneTool"))
        self.m_toolButtonGroup.addButton(self.m_stoneTool)
        self.gridLayout.addWidget(self.m_stoneTool, 5, 3, 1, 1)
        self.m_flintTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_flintTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_flintTool.setCheckable(True)
        self.m_flintTool.setObjectName(_fromUtf8("m_flintTool"))
        self.m_toolButtonGroup.addButton(self.m_flintTool)
        self.gridLayout.addWidget(self.m_flintTool, 5, 5, 1, 1)
        self.m_tileTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_tileTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_tileTool.setCheckable(True)
        self.m_tileTool.setObjectName(_fromUtf8("m_tileTool"))
        self.m_toolButtonGroup.addButton(self.m_tileTool)
        self.gridLayout.addWidget(self.m_tileTool, 4, 4, 1, 1)
        self.m_verticalTruncationTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_verticalTruncationTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_verticalTruncationTool.setCheckable(True)
        self.m_verticalTruncationTool.setObjectName(_fromUtf8("m_verticalTruncationTool"))
        self.m_toolButtonGroup.addButton(self.m_verticalTruncationTool)
        self.gridLayout.addWidget(self.m_verticalTruncationTool, 2, 3, 1, 1)
        self.m_truncationTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_truncationTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_truncationTool.setCheckable(True)
        self.m_truncationTool.setObjectName(_fromUtf8("m_truncationTool"))
        self.m_toolButtonGroup.addButton(self.m_truncationTool)
        self.gridLayout.addWidget(self.m_truncationTool, 2, 2, 1, 1)
        self.m_basePointTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_basePointTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_basePointTool.setCheckable(True)
        self.m_basePointTool.setObjectName(_fromUtf8("m_basePointTool"))
        self.gridLayout.addWidget(self.m_basePointTool, 7, 4, 1, 1)
        self.m_baseLineTool = QtGui.QToolButton(self.m_drawingToolsGroup)
        self.m_baseLineTool.setMinimumSize(QtCore.QSize(40, 0))
        self.m_baseLineTool.setCheckable(True)
        self.m_baseLineTool.setObjectName(_fromUtf8("m_baseLineTool"))
        self.gridLayout.addWidget(self.m_baseLineTool, 7, 5, 1, 1)
        self.verticalLayout.addWidget(self.m_drawingToolsGroup)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 3, 1, 1)
        self.m_snapLinesLayerTool = SnappingToolButton(self.groupBox)
        self.m_snapLinesLayerTool.setCheckable(True)
        self.m_snapLinesLayerTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapLinesLayerTool.setObjectName(_fromUtf8("m_snapLinesLayerTool"))
        self.gridLayout_3.addWidget(self.m_snapLinesLayerTool, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.m_snapLinesBufferTool = SnappingToolButton(self.groupBox)
        self.m_snapLinesBufferTool.setCheckable(True)
        self.m_snapLinesBufferTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapLinesBufferTool.setObjectName(_fromUtf8("m_snapLinesBufferTool"))
        self.gridLayout_3.addWidget(self.m_snapLinesBufferTool, 1, 1, 1, 1)
        self.m_snapPolygonsBufferTool = SnappingToolButton(self.groupBox)
        self.m_snapPolygonsBufferTool.setCheckable(True)
        self.m_snapPolygonsBufferTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapPolygonsBufferTool.setObjectName(_fromUtf8("m_snapPolygonsBufferTool"))
        self.gridLayout_3.addWidget(self.m_snapPolygonsBufferTool, 1, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.m_snapPolygonsLayerTool = SnappingToolButton(self.groupBox)
        self.m_snapPolygonsLayerTool.setCheckable(True)
        self.m_snapPolygonsLayerTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapPolygonsLayerTool.setObjectName(_fromUtf8("m_snapPolygonsLayerTool"))
        self.gridLayout_3.addWidget(self.m_snapPolygonsLayerTool, 2, 2, 1, 1)
        self.m_snapSchematicsLayerTool = SnappingToolButton(self.groupBox)
        self.m_snapSchematicsLayerTool.setCheckable(True)
        self.m_snapSchematicsLayerTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapSchematicsLayerTool.setObjectName(_fromUtf8("m_snapSchematicsLayerTool"))
        self.gridLayout_3.addWidget(self.m_snapSchematicsLayerTool, 2, 3, 1, 1)
        self.m_snapSchematicsBufferTool = SnappingToolButton(self.groupBox)
        self.m_snapSchematicsBufferTool.setCheckable(True)
        self.m_snapSchematicsBufferTool.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.m_snapSchematicsBufferTool.setObjectName(_fromUtf8("m_snapSchematicsBufferTool"))
        self.gridLayout_3.addWidget(self.m_snapSchematicsBufferTool, 1, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.m_topologicalLabel = QtGui.QLabel(self.groupBox)
        self.m_topologicalLabel.setObjectName(_fromUtf8("m_topologicalLabel"))
        self.horizontalLayout_3.addWidget(self.m_topologicalLabel)
        self.m_topologicalTool = TopoEditToolButton(self.groupBox)
        self.m_topologicalTool.setCheckable(True)
        self.m_topologicalTool.setObjectName(_fromUtf8("m_topologicalTool"))
        self.horizontalLayout_3.addWidget(self.m_topologicalTool)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.m_clearButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.m_clearButton.setObjectName(_fromUtf8("m_clearButton"))
        self.horizontalLayout.addWidget(self.m_clearButton)
        self.m_mergeButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.m_mergeButton.setObjectName(_fromUtf8("m_mergeButton"))
        self.horizontalLayout.addWidget(self.m_mergeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(17, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        PlanDockWidget.setWidget(self.PlanDockContents)
        self.m_siteLabel.setBuddy(self.m_siteEdit)
        self.m_numberLabel.setBuddy(self.m_numberSpin)
        self.m_sourceLabel.setBuddy(self.m_sourceEdit)
        self.m_commentLabel.setBuddy(self.m_commentEdit)
        self.m_sourceFileLabel.setBuddy(self.m_sourceFileEdit)
        self.m_createdByLabel.setBuddy(self.m_createdByEdit)

        self.retranslateUi(PlanDockWidget)
        QtCore.QMetaObject.connectSlotsByName(PlanDockWidget)
        PlanDockWidget.setTabOrder(self.scrollArea, self.m_loadRawButton)
        PlanDockWidget.setTabOrder(self.m_loadRawButton, self.m_loadGeoButton)
        PlanDockWidget.setTabOrder(self.m_loadGeoButton, self.m_loadContextButton)
        PlanDockWidget.setTabOrder(self.m_loadContextButton, self.m_siteEdit)
        PlanDockWidget.setTabOrder(self.m_siteEdit, self.m_numberSpin)
        PlanDockWidget.setTabOrder(self.m_numberSpin, self.m_sourceEdit)
        PlanDockWidget.setTabOrder(self.m_sourceEdit, self.m_sourceFileEdit)
        PlanDockWidget.setTabOrder(self.m_sourceFileEdit, self.m_commentEdit)
        PlanDockWidget.setTabOrder(self.m_commentEdit, self.m_createdByEdit)
        PlanDockWidget.setTabOrder(self.m_createdByEdit, self.m_extentTool)
        PlanDockWidget.setTabOrder(self.m_extentTool, self.m_verticalEdgeTool)
        PlanDockWidget.setTabOrder(self.m_verticalEdgeTool, self.m_uncertainEdgeTool)
        PlanDockWidget.setTabOrder(self.m_uncertainEdgeTool, self.m_limitOfExcavationTool)
        PlanDockWidget.setTabOrder(self.m_limitOfExcavationTool, self.m_truncationTool)
        PlanDockWidget.setTabOrder(self.m_truncationTool, self.m_verticalTruncationTool)
        PlanDockWidget.setTabOrder(self.m_verticalTruncationTool, self.m_breakOfSlopeTool)
        PlanDockWidget.setTabOrder(self.m_breakOfSlopeTool, self.m_verticalBreakOfSlopeTool)
        PlanDockWidget.setTabOrder(self.m_verticalBreakOfSlopeTool, self.m_hachureTool)
        PlanDockWidget.setTabOrder(self.m_hachureTool, self.m_undercutTool)
        PlanDockWidget.setTabOrder(self.m_undercutTool, self.m_returnOfSlopeTool)
        PlanDockWidget.setTabOrder(self.m_returnOfSlopeTool, self.m_cbmTool)
        PlanDockWidget.setTabOrder(self.m_cbmTool, self.m_brickTool)
        PlanDockWidget.setTabOrder(self.m_brickTool, self.m_tileTool)
        PlanDockWidget.setTabOrder(self.m_tileTool, self.m_mortarTool)
        PlanDockWidget.setTabOrder(self.m_mortarTool, self.m_charcoalTool)
        PlanDockWidget.setTabOrder(self.m_charcoalTool, self.m_stoneTool)
        PlanDockWidget.setTabOrder(self.m_stoneTool, self.m_potTool)
        PlanDockWidget.setTabOrder(self.m_potTool, self.m_flintTool)
        PlanDockWidget.setTabOrder(self.m_flintTool, self.m_levelTool)
        PlanDockWidget.setTabOrder(self.m_levelTool, self.m_schematicTool)
        PlanDockWidget.setTabOrder(self.m_schematicTool, self.m_clearTool)
        PlanDockWidget.setTabOrder(self.m_clearTool, self.m_sectionPinTool)
        PlanDockWidget.setTabOrder(self.m_sectionPinTool, self.m_sectionLineTool)
        PlanDockWidget.setTabOrder(self.m_sectionLineTool, self.m_basePointTool)
        PlanDockWidget.setTabOrder(self.m_basePointTool, self.m_baseLineTool)
        PlanDockWidget.setTabOrder(self.m_baseLineTool, self.m_snapLinesBufferTool)
        PlanDockWidget.setTabOrder(self.m_snapLinesBufferTool, self.m_snapPolygonsBufferTool)
        PlanDockWidget.setTabOrder(self.m_snapPolygonsBufferTool, self.m_snapSchematicsBufferTool)
        PlanDockWidget.setTabOrder(self.m_snapSchematicsBufferTool, self.m_snapLinesLayerTool)
        PlanDockWidget.setTabOrder(self.m_snapLinesLayerTool, self.m_snapPolygonsLayerTool)
        PlanDockWidget.setTabOrder(self.m_snapPolygonsLayerTool, self.m_snapSchematicsLayerTool)
        PlanDockWidget.setTabOrder(self.m_snapSchematicsLayerTool, self.m_topologicalTool)
        PlanDockWidget.setTabOrder(self.m_topologicalTool, self.m_clearButton)
        PlanDockWidget.setTabOrder(self.m_clearButton, self.m_mergeButton)

    def retranslateUi(self, PlanDockWidget):
        PlanDockWidget.setWindowTitle(_translate("PlanDockWidget", "ArkPlan", None))
        self.groupBox_2.setTitle(_translate("PlanDockWidget", "Load Plans", None))
        self.m_loadRawButton.setText(_translate("PlanDockWidget", "Raw Plan", None))
        self.m_loadGeoButton.setText(_translate("PlanDockWidget", "Geo Plan", None))
        self.m_loadContextButton.setText(_translate("PlanDockWidget", "Context", None))
        self.m_planGroup.setTitle(_translate("PlanDockWidget", "Attributes", None))
        self.m_siteLabel.setText(_translate("PlanDockWidget", "Site Code:", None))
        self.m_numberLabel.setText(_translate("PlanDockWidget", "Number:", None))
        self.m_numberSpin.setToolTip(_translate("PlanDockWidget", "Context Number", None))
        self.m_sourceEdit.setToolTip(_translate("PlanDockWidget", "Source", None))
        self.m_sourceLabel.setText(_translate("PlanDockWidget", "Source:", None))
        self.m_commentLabel.setText(_translate("PlanDockWidget", "Comment:", None))
        self.m_sourceFileLabel.setText(_translate("PlanDockWidget", "Source File:", None))
        self.m_createdByLabel.setText(_translate("PlanDockWidget", "Created By:", None))
        self.m_drawingToolsGroup.setTitle(_translate("PlanDockWidget", "Drawing Tools", None))
        self.m_levelTool.setToolTip(_translate("PlanDockWidget", "Level", None))
        self.m_levelTool.setText(_translate("PlanDockWidget", "lvl", None))
        self.m_extentTool.setToolTip(_translate("PlanDockWidget", "Extent of context", None))
        self.m_extentTool.setText(_translate("PlanDockWidget", "ext", None))
        self.m_cbmTool.setToolTip(_translate("PlanDockWidget", "CBM", None))
        self.m_cbmTool.setText(_translate("PlanDockWidget", "cbm", None))
        self.m_brickTool.setToolTip(_translate("PlanDockWidget", "Brick", None))
        self.m_brickTool.setText(_translate("PlanDockWidget", "brk", None))
        self.m_undercutTool.setToolTip(_translate("PlanDockWidget", "Undercut", None))
        self.m_undercutTool.setText(_translate("PlanDockWidget", "unc", None))
        self.m_uncertainEdgeTool.setToolTip(_translate("PlanDockWidget", "Uncertain Edge", None))
        self.m_uncertainEdgeTool.setText(_translate("PlanDockWidget", "ueg", None))
        self.m_sectionLineTool.setToolTip(_translate("PlanDockWidget", "Level", None))
        self.m_sectionLineTool.setText(_translate("PlanDockWidget", "sln", None))
        self.m_limitOfExcavationTool.setToolTip(_translate("PlanDockWidget", "Limit of Excavation", None))
        self.m_limitOfExcavationTool.setText(_translate("PlanDockWidget", "loe", None))
        self.m_verticalBreakOfSlopeTool.setToolTip(_translate("PlanDockWidget", "Vertical Break of Slope", None))
        self.m_verticalBreakOfSlopeTool.setText(_translate("PlanDockWidget", "vbs", None))
        self.m_returnOfSlopeTool.setToolTip(_translate("PlanDockWidget", "Return of Slope", None))
        self.m_returnOfSlopeTool.setText(_translate("PlanDockWidget", "ros", None))
        self.m_mortarTool.setToolTip(_translate("PlanDockWidget", "Mortar", None))
        self.m_mortarTool.setText(_translate("PlanDockWidget", "mtr", None))
        self.m_hachureTool.setToolTip(_translate("PlanDockWidget", "Hachure", None))
        self.m_hachureTool.setText(_translate("PlanDockWidget", "hch", None))
        self.m_schematicTool.setToolTip(_translate("PlanDockWidget", "Schematic", None))
        self.m_schematicTool.setText(_translate("PlanDockWidget", "sch", None))
        self.m_charcoalTool.setToolTip(_translate("PlanDockWidget", "Charcoal", None))
        self.m_charcoalTool.setText(_translate("PlanDockWidget", "cha", None))
        self.m_breakOfSlopeTool.setToolTip(_translate("PlanDockWidget", "Break of Slope", None))
        self.m_breakOfSlopeTool.setText(_translate("PlanDockWidget", "bos", None))
        self.m_sectionPinTool.setToolTip(_translate("PlanDockWidget", "Level", None))
        self.m_sectionPinTool.setText(_translate("PlanDockWidget", "sec", None))
        self.m_verticalEdgeTool.setToolTip(_translate("PlanDockWidget", "Vertical Edge", None))
        self.m_verticalEdgeTool.setText(_translate("PlanDockWidget", "veg", None))
        self.m_clearTool.setText(_translate("PlanDockWidget", "clr", None))
        self.m_potTool.setToolTip(_translate("PlanDockWidget", "Pot", None))
        self.m_potTool.setText(_translate("PlanDockWidget", "pot", None))
        self.m_stoneTool.setToolTip(_translate("PlanDockWidget", "Stone", None))
        self.m_stoneTool.setText(_translate("PlanDockWidget", "sto", None))
        self.m_flintTool.setToolTip(_translate("PlanDockWidget", "Flint", None))
        self.m_flintTool.setText(_translate("PlanDockWidget", "fli", None))
        self.m_tileTool.setToolTip(_translate("PlanDockWidget", "Tile", None))
        self.m_tileTool.setText(_translate("PlanDockWidget", "til", None))
        self.m_verticalTruncationTool.setToolTip(_translate("PlanDockWidget", "Vertical Truncation", None))
        self.m_verticalTruncationTool.setText(_translate("PlanDockWidget", "vtr", None))
        self.m_truncationTool.setToolTip(_translate("PlanDockWidget", "Truncation", None))
        self.m_truncationTool.setText(_translate("PlanDockWidget", "trn", None))
        self.m_basePointTool.setToolTip(_translate("PlanDockWidget", "Level", None))
        self.m_basePointTool.setText(_translate("PlanDockWidget", "bpt", None))
        self.m_baseLineTool.setToolTip(_translate("PlanDockWidget", "Level", None))
        self.m_baseLineTool.setText(_translate("PlanDockWidget", "bln", None))
        self.groupBox.setTitle(_translate("PlanDockWidget", "Editing:", None))
        self.label_13.setText(_translate("PlanDockWidget", "Schms", None))
        self.m_snapLinesLayerTool.setText(_translate("PlanDockWidget", "...", None))
        self.label_11.setText(_translate("PlanDockWidget", "Lines", None))
        self.m_snapLinesBufferTool.setText(_translate("PlanDockWidget", "...", None))
        self.m_snapPolygonsBufferTool.setText(_translate("PlanDockWidget", "...", None))
        self.label_12.setText(_translate("PlanDockWidget", "Polys", None))
        self.label_2.setText(_translate("PlanDockWidget", "Snap Layers:", None))
        self.label.setText(_translate("PlanDockWidget", "Snap Buffers:", None))
        self.m_snapPolygonsLayerTool.setText(_translate("PlanDockWidget", "...", None))
        self.m_snapSchematicsLayerTool.setText(_translate("PlanDockWidget", "...", None))
        self.m_snapSchematicsBufferTool.setText(_translate("PlanDockWidget", "...", None))
        self.m_topologicalLabel.setText(_translate("PlanDockWidget", "Topological editing:", None))
        self.m_topologicalTool.setText(_translate("PlanDockWidget", "topo", None))
        self.m_clearButton.setToolTip(_translate("PlanDockWidget", "Clear unsaved changes from work layers", None))
        self.m_clearButton.setText(_translate("PlanDockWidget", "Clear", None))
        self.m_mergeButton.setToolTip(_translate("PlanDockWidget", "Move new context to main layers", None))
        self.m_mergeButton.setText(_translate("PlanDockWidget", "Merge", None))

from ..core.dock import QgsDockWidget
from ..core.snap_widgets import SnappingToolButton, TopoEditToolButton
