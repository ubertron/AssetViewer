#!/user/bin/env python3

import sys

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, \
    QOpenGLWidget, QSizePolicy
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.QtCore import Qt
from qt3d_window import ADQt3DWindow

class AssetViewer(QWidget):
    _title = 'Asset Viewer'

    def __init__(self, *args):
        super(AssetViewer, self).__init__(*args)
        self.setWindowTitle(self._title)
        layout = QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(0)
        self.setLayout(layout)
        test_label = QLabel(self._title)
        test_label.setAlignment(Qt.AlignCenter)
        test_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # open_gl_widget = QOpenGLWidget()
        self.qt3d_widget = QWidget.createWindowContainer(Qt3DExtras.Qt3DWindow())
        layout.addWidget(test_label)
        # layout.addWidget(open_gl_widget)
        layout.addWidget(self.qt3d_widget)
        self.setMinimumSize(320, 120)
        self.setup_ui()

    def setup_ui(self):
        # self.qt3d_widget.createWindowContainer(ADQt3DWindow())
        pass

    def add_widget(self, widget):
        self.layout().addWidget(widget)


if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    asset_viewer = AssetViewer()
    asset_viewer.show()
    qt_app.exec_()
