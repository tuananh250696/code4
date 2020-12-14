from PySide2 import QtCore, QtGui, QtWidgets
import shiboken2


def for_loop_files(paths, interval=100, parent=None, objectName=""):
    timer = QtCore.QTimer(parent=parent, singleShot=True, interval=interval)
    if objectName:
        timer.setObjectName(objectName)
    loop = QtCore.QEventLoop(timer)
    timer.timeout.connect(loop.quit)
    timer.destroyed.connect(loop.quit)
    for path in paths:
        if shiboken2.isValid(timer):
            timer.start()
            loop.exec_()
            yield path


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setIconSize(QtCore.QSize(188, 190))
        self.list_widget.setResizeMode(QtWidgets.QListView.Adjust)
        self.list_widget.setFlow(QtWidgets.QListView.TopToBottom)
        self.setCentralWidget(self.list_widget)
        self.resize(640, 480)
        QtCore.QTimer.singleShot(0, self.load_icons)

    @QtCore.Slot()
    def load_icons(self):
        paths = ["3.png", "3.png", "3.png", "3.png", ".png"]
        for path in for_loop_files(paths, parent=self, objectName="icon_timer", interval=30):
            it = QtWidgets.QListWidgetItem()
            it.setIcon(QtGui.QIcon(path))
            self.list_widget.addItem(it)

    def closeEvent(self, event):
        timer = self.findChild(QtCore.QTimer, "icon_timer")
        timer.deleteLater()
        super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())