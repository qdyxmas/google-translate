# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(492, 348)
        self.config_file = QtGui.QLineEdit(Form)
        self.config_file.setGeometry(QtCore.QRect(140, 10, 341, 20))
        self.config_file.setObjectName(_fromUtf8("config_file"))
        self.cfgbutton = QtGui.QPushButton(Form)
        self.cfgbutton.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.cfgbutton.setObjectName(_fromUtf8("cfgbutton"))
        self.excelfile = QtGui.QLineEdit(Form)
        self.excelfile.setGeometry(QtCore.QRect(140, 50, 341, 20))
        self.excelfile.setObjectName(_fromUtf8("excelfile"))
        self.excelbutton = QtGui.QPushButton(Form)
        self.excelbutton.setGeometry(QtCore.QRect(20, 50, 101, 23))
        self.excelbutton.setObjectName(_fromUtf8("excelbutton"))
        self.startchk = QtGui.QPushButton(Form)
        self.startchk.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.startchk.setObjectName(_fromUtf8("startchk"))
        self.logmsg = QtGui.QTextEdit(Form)
        self.logmsg.setGeometry(QtCore.QRect(20, 120, 461, 201))
        self.logmsg.setObjectName(_fromUtf8("logmsg"))
        self.statuslabel = QtGui.QLabel(Form)
        self.statuslabel.setGeometry(QtCore.QRect(110, 92, 291, 20))
        self.statuslabel.setText(_fromUtf8(""))
        self.statuslabel.setObjectName(_fromUtf8("statuslabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cfgbutton.setText(_translate("Form", "选择配置文件", None))
        self.excelbutton.setText(_translate("Form", "选择Excel文件", None))
        self.startchk.setText(_translate("Form", "开始检查", None))

