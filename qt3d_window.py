import sys
from PySide2.QtCore import Property, QObject, QPropertyAnimation, Signal, Slot
from PySide2.QtGui import QGuiApplication, QMatrix4x4, QQuaternion, QVector3D, QWindow
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DRender import Qt3DRender
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.QtWidgets import QWidget


class ADQt3DWindow(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super(ADQt3DWindow, self).__init__()
        # self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        # self.camera().setPosition(QVector3D(0, 0, 40))
        # self.camera().setViewCenter(QVector3D(0, 0, 0))

        # For camera controls
        self.root_entity = Qt3DCore.QEntity()
        # self.material = Qt3DExtras.QPhongMaterial(self.root_entity)
        # self.camController = Qt3DExtras.QOrbitCameraController(self.root_entity)
        # self.camController.setLinearSpeed(50)
        # self.camController.setLookSpeed(180)
        # self.camController.setCamera(self.camera())

        self.setRootEntity(self.root_entity)

        # self.spheres = []
        # self.meshes = []
        # self.transforms = []

    def add_sphere(self, radius, xyz, rings=10, slices=10):
        sphere_entity = Qt3DCore.QEntity(self.root_entity)
        sphere_mesh = Qt3DExtras.QSphereMesh()
        sphere_mesh.setRadius(radius)
        sphere_mesh.setRings(rings)
        sphere_mesh.setSlices(slices)
        sphere_transform = Qt3DCore.QTransform()
        sphere_transform.setTranslation(QVector3D(*xyz))
        sphere_entity.addComponent(sphere_mesh)
        sphere_entity.addComponent(self.material)
        sphere_entity.addComponent(sphere_transform)

        self.spheres.append(sphere_entity)
        self.meshes.append(sphere_mesh)
        self.transforms.append(sphere_transform)

# class Qt3dWidget(QWidget):
#     def __init__(self):
#         super(Qt3dWidget, self).__init__()

        # class SphereDialog(Ui_sphdialog):
        #     def __init__(self):
        #         super().__init__()
        #         self.window = SphereWindow()
        #
        #     def setupUi(self, SphereDialog):
        #         super().setupUi(SphereDialog)
        #         self.horizontalLayout.replaceWidget(
        #             self.widget, QWidget.createWindowContainer(self.window)
        #         )
        #         self.pushButton.clicked.connect(self.add_sphere)
