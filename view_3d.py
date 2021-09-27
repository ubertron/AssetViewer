#!/user/bin/env python3

import sys

from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.QtGui import QVector3D
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout
from PySide2.Qt3DCore import Qt3DCore


class View3D(QWidget):
    def __init__(self):
        super().__init__()
        self.view = Qt3DExtras.Qt3DWindow()
        self.container = self.createWindowContainer(self.view)

        layout = QHBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

        # put some nodes in the scene
        scene = self.create_scene()
        # Camera
        camera = self.view.camera()
        camera.lens().setPerspectiveProjection(45.0, 16.0 / 9.0, 0.1, 1000.0)
        camera.setPosition(QVector3D(0.0, 0.0, 40.0))
        camera.setViewCenter(QVector3D(0.0, 0.0, 0.0))

        # For camera controls.
        cam_controller = Qt3DExtras.QFirstPersonCameraController(scene)
        cam_controller.setLinearSpeed(50.0)
        cam_controller.setLookSpeed(180.0)
        cam_controller.setCamera(camera)

        # assign root node to the view
        self.view.setRootEntity(scene)

    @staticmethod
    def create_scene():
        node = Qt3DCore.QEntity()
        return node


if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    asset_viewer = View3D()
    asset_viewer.show()
    qt_app.exec_()
