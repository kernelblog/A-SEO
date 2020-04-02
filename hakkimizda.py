# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hakkimizda(object):
    def setupUi(self, hakkimizda):
        hakkimizda.setObjectName("hakkimizda")
        hakkimizda.resize(370, 427)
        hakkimizda.setMinimumSize(QtCore.QSize(370, 427))
        hakkimizda.setMaximumSize(QtCore.QSize(370, 427))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("KernelBlog.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hakkimizda.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(hakkimizda)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 191, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kb_b.jpg"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 370, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 340, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        hakkimizda.setCentralWidget(self.centralwidget)

        self.retranslateUi(hakkimizda)
        QtCore.QMetaObject.connectSlotsByName(hakkimizda)

    def retranslateUi(self, hakkimizda):
        _translate = QtCore.QCoreApplication.translate
        hakkimizda.setWindowTitle(_translate("hakkimizda", "A+SEO - Hakkında"))
        self.label_2.setText(_translate("hakkimizda", "A+SEO - KernelBlog"))
        self.label_3.setText(_translate("hakkimizda", "Version: Alpha"))
        self.label_4.setText(_translate("hakkimizda", "Powered By KernelBlog"))
        self.label_5.setText(_translate("hakkimizda", "Asistan + SEO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hakkimizda = QtWidgets.QMainWindow()
    ui = Ui_hakkimizda()
    ui.setupUi(hakkimizda)
    hakkimizda.show()
    sys.exit(app.exec_())
