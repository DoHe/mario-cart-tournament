# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupWidget.ui'
#
# Created: Tue Dec 25 11:24:56 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GroupWidget(object):
    def setupUi(self, GroupWidget):
        GroupWidget.setObjectName(_fromUtf8("GroupWidget"))
        GroupWidget.resize(348, 532)
        GroupWidget.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(GroupWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.group_label = QtGui.QLabel(GroupWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.group_label.setFont(font)
        self.group_label.setObjectName(_fromUtf8("group_label"))
        self.verticalLayout.addWidget(self.group_label)
        self.frame = QtGui.QFrame(GroupWidget)
        self.frame.setStyleSheet(_fromUtf8("#frame{\n"
"border: 1.5px solid rgb(190, 190, 190);\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.driver1 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.driver1.setFont(font)
        self.driver1.setObjectName(_fromUtf8("driver1"))
        self.horizontalLayout.addWidget(self.driver1)
        self.name1 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: rgb(255, 0, 0)\n"
"}"))
        self.name1.setText(_fromUtf8(""))
        self.name1.setObjectName(_fromUtf8("name1"))
        self.horizontalLayout.addWidget(self.name1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.rank_combo1 = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rank_combo1.setFont(font)
        self.rank_combo1.setObjectName(_fromUtf8("rank_combo1"))
        self.rank_combo1.addItem(_fromUtf8(""))
        self.rank_combo1.addItem(_fromUtf8(""))
        self.rank_combo1.addItem(_fromUtf8(""))
        self.rank_combo1.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.rank_combo1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.driver2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.driver2.setFont(font)
        self.driver2.setObjectName(_fromUtf8("driver2"))
        self.horizontalLayout_2.addWidget(self.driver2)
        self.name2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: rgb(255, 0, 0)\n"
"}"))
        self.name2.setText(_fromUtf8(""))
        self.name2.setObjectName(_fromUtf8("name2"))
        self.horizontalLayout_2.addWidget(self.name2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.rank_combo2 = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rank_combo2.setFont(font)
        self.rank_combo2.setObjectName(_fromUtf8("rank_combo2"))
        self.rank_combo2.addItem(_fromUtf8(""))
        self.rank_combo2.addItem(_fromUtf8(""))
        self.rank_combo2.addItem(_fromUtf8(""))
        self.rank_combo2.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.rank_combo2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.driver3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.driver3.setFont(font)
        self.driver3.setObjectName(_fromUtf8("driver3"))
        self.horizontalLayout_3.addWidget(self.driver3)
        self.name3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name3.setFont(font)
        self.name3.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: rgb(255, 0, 0)\n"
"}"))
        self.name3.setText(_fromUtf8(""))
        self.name3.setObjectName(_fromUtf8("name3"))
        self.horizontalLayout_3.addWidget(self.name3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.rank_combo3 = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rank_combo3.setFont(font)
        self.rank_combo3.setObjectName(_fromUtf8("rank_combo3"))
        self.rank_combo3.addItem(_fromUtf8(""))
        self.rank_combo3.addItem(_fromUtf8(""))
        self.rank_combo3.addItem(_fromUtf8(""))
        self.rank_combo3.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.rank_combo3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.driver4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.driver4.setFont(font)
        self.driver4.setObjectName(_fromUtf8("driver4"))
        self.horizontalLayout_4.addWidget(self.driver4)
        self.name4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name4.setFont(font)
        self.name4.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: rgb(255, 0, 0)\n"
"}"))
        self.name4.setText(_fromUtf8(""))
        self.name4.setObjectName(_fromUtf8("name4"))
        self.horizontalLayout_4.addWidget(self.name4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.rank_combo4 = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rank_combo4.setFont(font)
        self.rank_combo4.setObjectName(_fromUtf8("rank_combo4"))
        self.rank_combo4.addItem(_fromUtf8(""))
        self.rank_combo4.addItem(_fromUtf8(""))
        self.rank_combo4.addItem(_fromUtf8(""))
        self.rank_combo4.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.rank_combo4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(GroupWidget)
        QtCore.QMetaObject.connectSlotsByName(GroupWidget)

    def retranslateUi(self, GroupWidget):
        GroupWidget.setWindowTitle(QtGui.QApplication.translate("GroupWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.group_label.setText(QtGui.QApplication.translate("GroupWidget", "Gruppe:", None, QtGui.QApplication.UnicodeUTF8))
        self.driver1.setText(QtGui.QApplication.translate("GroupWidget", "Fahrer 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GroupWidget", "Platz:", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo1.setItemText(0, QtGui.QApplication.translate("GroupWidget", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo1.setItemText(1, QtGui.QApplication.translate("GroupWidget", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo1.setItemText(2, QtGui.QApplication.translate("GroupWidget", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo1.setItemText(3, QtGui.QApplication.translate("GroupWidget", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.driver2.setText(QtGui.QApplication.translate("GroupWidget", "Fahrer 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GroupWidget", "Platz:", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo2.setItemText(0, QtGui.QApplication.translate("GroupWidget", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo2.setItemText(1, QtGui.QApplication.translate("GroupWidget", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo2.setItemText(2, QtGui.QApplication.translate("GroupWidget", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo2.setItemText(3, QtGui.QApplication.translate("GroupWidget", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.driver3.setText(QtGui.QApplication.translate("GroupWidget", "Fahrer 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GroupWidget", "Platz:", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo3.setItemText(0, QtGui.QApplication.translate("GroupWidget", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo3.setItemText(1, QtGui.QApplication.translate("GroupWidget", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo3.setItemText(2, QtGui.QApplication.translate("GroupWidget", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo3.setItemText(3, QtGui.QApplication.translate("GroupWidget", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.driver4.setText(QtGui.QApplication.translate("GroupWidget", "Fahrer 4:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GroupWidget", "Platz:", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo4.setItemText(0, QtGui.QApplication.translate("GroupWidget", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo4.setItemText(1, QtGui.QApplication.translate("GroupWidget", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo4.setItemText(2, QtGui.QApplication.translate("GroupWidget", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.rank_combo4.setItemText(3, QtGui.QApplication.translate("GroupWidget", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("GroupWidget", "OK", None, QtGui.QApplication.UnicodeUTF8))

