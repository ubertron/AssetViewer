#!/user/bin/env python3

import sys

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QOpenGLWidget, QSizePolicy
from PySide2.QtCore import Qt


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
        open_gl_widget = QOpenGLWidget()
        layout.addWidget(test_label)
        layout.addWidget(open_gl_widget)
        self.setMinimumSize(240, 120)


if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    asset_viewer = AssetViewer()
    asset_viewer.show()
    qt_app.exec_()
