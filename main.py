import cv2
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic             # +++
import imutils

from test2_ui import Ui_Form                                   # +++

class video (QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.value = 1
#        uic.loadUi('test2.ui',self)                           # ---
        self.setupUi(self)                                     # +++

        self.CAPTURE.clicked.connect(self.start_webcam)
        self.NEXT_5.clicked.connect(self.capture_image)
       # self.NEXT_4.clicked.connect(self.startUIWindow)       # - ()
        self.imgLabel.setScaledContents(True)

        self.cap = None                                        #  -capture <-> +cap

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0
        self.start_webcam()

    @QtCore.pyqtSlot()
    def start_webcam(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  500)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image = self.cap.read()
        image = imutils.resize(image, width=560, height=560)
        simage     = cv2.flip(image, 1)
        self.displayImage(image, True)

    @QtCore.pyqtSlot()
    def capture_image(self):
        flag, frame = self.cap.read()
        frame = imutils.resize(frame, width=80, height=60)
        self.value =self.value + 1
        cv2.imwrite('%s.png'%(self.value),frame)
        self.TEXT.setText("Kindly Press 'Show' to connect with webcam.")


    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))



if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = video()
    window.setWindowTitle('main code')
    window.show()
    sys.exit(app.exec_())

