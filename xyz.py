import os, sys, json
sys.path.append('Z:\\pipeline\\site-packages')
from PySide import QtGui, QtCore, QtSvg

################################################################################
# Custom Widgets
################################################################################
class LayerWidget(QtGui.QWidget):

    def __init__(self):
        super(LayerWidget, self).__init__()

        # controls
        self.ui_thumbnail = QtGui.QToolButton()
        self.ui_thumbnail.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ui_thumbnail.setFixedSize(128,128)
        self.ui_thumbnail.setIconSize(QtCore.QSize(80,80))
        self.ui_thumbnail.setText('TITLE HERE')

        self.ui_profiles = QtGui.QComboBox()
        self.ui_profiles.addItems(['Item 1','Item 2','Item 3'])

        # layout
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.ui_thumbnail)
        main_layout.addWidget(self.ui_profiles)
        main_layout.addStretch()
        self.setLayout(main_layout)


class LayerManager(QtGui.QWidget):
    def __init__(self):
        super(LayerManager, self).__init__()
        self.resize(400, 500)

        self.ui_layers = QtGui.QListWidget()
        self.ui_layers.setViewMode(QtGui.QListWidget.IconMode)
        self.ui_layers.setResizeMode(QtGui.QListWidget.Adjust)
        self.ui_layers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui_layers.setMovement(QtGui.QListView.Static)
        self.ui_layers.setIconSize(QtCore.QSize(96,96))
        self.ui_layers.setSpacing(10)

        main_layout = QtGui.QVBoxLayout(self)
        main_layout.addWidget(self.ui_layers)


    def add_new_layers(self):
        for x in range(4):
            widget = LayerWidget()
            item = QtGui.QListWidgetItem()
            self.ui_layers.insertItem(self.ui_layers.count(), item)
            self.ui_layers.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())


################################################################################
# Main Window
################################################################################
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Hyv')
        self.resize(500, 500)

        self.ui_layerManager = LayerManager()
        self.setCentralWidget(self.ui_layerManager)
        self.ui_layerManager.add_new_layers()


################################################################################
# Launch Methods
################################################################################
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()