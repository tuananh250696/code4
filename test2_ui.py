from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 600)
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(10, 470, 191, 111))
        self.TEXT.setObjectName("TEXT")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(200, 120,590, 470))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")

        self.CAPTURE = QtWidgets.QPushButton(Dialog)
        self.CAPTURE.setGeometry(QtCore.QRect(10, 130, 181, 91))
        self.CAPTURE.setObjectName("CAPTURE")

        self.imgLabel_2 = QtWidgets.QLabel(Dialog)
        self.imgLabel_2.setGeometry(QtCore.QRect(0, 0, 1922,35))
        self.imgLabel_2.setAutoFillBackground(False)
        self.imgLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_2.setText("")
        self.imgLabel_2.setPixmap(QtGui.QPixmap("ngang1.png"))
        self.imgLabel_2.setObjectName("imgLabel_2")

        # creating a combo box for selecting camera
        self.camera_selector = QtWidgets.QComboBox(Dialog)
        self.camera_selector.setGeometry(QtCore.QRect(0, 37, 201, 81))
        # adding status tip to it
        self.camera_selector.setStatusTip("Choose camera to take pictures")

        # adding tool tip to it
        self.camera_selector.setToolTip("Select Camera")
        self.camera_selector.setToolTipDuration(2500)


        self.NEXT_4 = QtWidgets.QPushButton(Dialog)
        self.NEXT_4.setGeometry(QtCore.QRect(200, 37, 191, 81))
        self.NEXT_4.setObjectName("NEXT_4")
        self.NEXT_5 = QtWidgets.QPushButton(Dialog)
        self.NEXT_5.setGeometry(QtCore.QRect(390, 37, 191, 81))
        self.NEXT_5.setObjectName("NEXT_5")
        self.NEXT_3 = QtWidgets.QPushButton(Dialog)
        self.NEXT_3.setGeometry(QtCore.QRect(10, 230, 181, 101))
        self.NEXT_3.setObjectName("NEXT_3")
        self.NEXT_7 = QtWidgets.QPushButton(Dialog)
        self.NEXT_7.setGeometry(QtCore.QRect(580, 37, 181, 81))
        self.NEXT_7.setObjectName("NEXT_7")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(790, 20, 230, 570))
        self.listWidget.setObjectName("ListWidgetItem")
        self.listWidget.setIconSize(QtCore.QSize(188, 190))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)

        self.it = QtWidgets.QListWidgetItem(self.listWidget)
        self.it1 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it2 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it3 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it4 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it5 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it6 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it7 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it8 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it9 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it10 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it11 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it12 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it13 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it14 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it15 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it16 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it17 = QtWidgets.QListWidgetItem(self.listWidget)


        self.TEXT.raise_()
        self.imgLabel.raise_()
        self.NEXT_4.raise_()
        self.NEXT_5.raise_()
        self.imgLabel_2.raise_()
        self.CAPTURE.raise_()
        self.NEXT_3.raise_()
        self.NEXT_7.raise_()


        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CAPTURE.setText(_translate("Dialog", "Chụp Ảnh"))
        self.NEXT_4.setText(_translate("Dialog", "Thư Mục Lưu Video"))
        self.NEXT_5.setText(_translate("Dialog", "Quay Video"))
        self.NEXT_3.setText(_translate("Dialog", "IN PHIẾU KHÁM"))
        self.NEXT_7.setText(_translate("Dialog", "Đóng"))


