# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 274)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.current_node_detail = QtWidgets.QPlainTextEdit(Dialog)
        self.current_node_detail.setReadOnly(True)
        self.current_node_detail.setObjectName("current_node_detail")
        self.verticalLayout.addWidget(self.current_node_detail)
        self.get_node = QtWidgets.QPushButton(Dialog)
        self.get_node.setObjectName("get_node")
        self.verticalLayout.addWidget(self.get_node)
        self.set_node = QtWidgets.QPushButton(Dialog)
        self.set_node.setObjectName("set_node")
        self.verticalLayout.addWidget(self.set_node)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "NodePropertyTransfer", None, -1))
        self.get_node.setText(QtWidgets.QApplication.translate("Dialog", "GetNodeParameter", None, -1))
        self.set_node.setText(QtWidgets.QApplication.translate("Dialog", "TransferParameter", None, -1))
