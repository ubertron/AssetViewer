#!/usr/bin/env python3

import sys
from os.path import join, dirname, isfile

from PySide2 import QtCore, QtGui
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DRender import Qt3DRender
from PySide2.Qt3DInput import Qt3DInput
from PySide2.QtWidgets import QVBoxLayout, QWidget, QApplication
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QColor, QQuaternion

INPUT_ = Qt3DInput.QInputAspect()

class SceneModifier(QtCore.QObject):
    def __init__(self, root_entity=None):
        super().__init__()
        self.root_entity = root_entity
        self.mesh_entity = Qt3DCore.QEntity(root_entity)
        self.mesh_object = None
        self.transform = None
        self.material = None
        self.add_cuboid()
        # self.add_mesh()

    def add_cuboid(self):
        # obj_path = join(dirname(__file__), 'models', 'human.obj')
        obj_path = join(dirname(__file__), 'models', 'test_model.obj')
        print(isfile(obj_path))
        self.mesh_object = Qt3DRender.QMesh()
        self.mesh_object.setSource(QUrl.fromLocalFile(obj_path))
        # self.mesh_object.setSource(QUrl("qrc:/models/test_model.obj"))
        print(f'Mesh name: {self.mesh_object.meshName()}')
        # print(self.mesh_object.status())
        # self.mesh_object = Qt3DExtras.QCuboidMesh()
        self.transform = Qt3DCore.QTransform(
            scale=2., translation=QtGui.QVector3D(0, -1, 12))
        # self.transform = Qt3DCore.QTransform(
        #     scale=4.0, translation=QtGui.QVector3D(5.0, -4.0, 0.0))
        self.material = Qt3DExtras.QPhongMaterial(diffuse=QColor("#665423"))
        self.mesh_entity.addComponent(self.mesh_object)
        self.mesh_entity.addComponent(self.material)
        self.mesh_entity.addComponent(self.transform)

    def add_mesh(self):
        obj_path = join(dirname(__file__), 'models', 'test_model.obj')
        self.mesh_object = Qt3DRender.QMesh()
        self.mesh_object.setSource(QUrl.fromLocalFile(obj_path))
        self.transform = Qt3DCore.QTransform(
            scale=2.0, translation=QtGui.QVector3D(0, -1, 12))
        self.material = Qt3DExtras.QPhongMaterial(diffuse=QColor("#665423"))
        self.mesh_entity.addComponent(self.mesh_object)
        self.mesh_entity.addComponent(self.material)
        self.mesh_entity.addComponent(self.transform)


'''
m_model = new Qt3DCore::QEntity(m_root);
m_mesh = new Qt3DRender::QMesh();
m_mesh->setSource(QUrl("qrc:/Resources/Models/MyModel.obj"));

m_material = new Qt3DExtras::QPhongMaterial;
m_material->setDiffuse(QColor(Qt::darkGray));

m_transform = new Qt3DCore::QTransform;
m_transform->setScale(1.0);
m_transform->setRotation(QQuaternion::fromEulerAngles(0.0, 0.0, 0.0));

m_model->addComponent(m_mesh);
m_model->addComponent(m_transform);
m_model->addComponent(m_material);

m_view->setRootEntity(m_root);
'''


class Viewport(QWidget):
    _title = 'Qt3d Viewport'

    def __init__(self):
        super(Viewport, self).__init__()
        self.setWindowTitle(self._title)
        layout = QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.view = Qt3DExtras.Qt3DWindow()
        self.root_entity = Qt3DCore.QEntity()
        self.modifier = SceneModifier(self.root_entity)
        container = QWidget.createWindowContainer(self.view)
        screenSize = self.view.screen().size()
        container.setMinimumSize(QtCore.QSize(200, 100))
        container.setMaximumSize(screenSize)
        self.layout().addWidget(container)
        self.setup_ui()

    def setup_ui(self):
        self.view.defaultFrameGraph().setClearColor(QtGui.QColor("#4d4d4f"))
        self.view.registerAspect(INPUT_)
        self.view.camera().lens().setPerspectiveProjection(45, 16/9, 0.1, 1000)
        self.view.camera().setPosition(QtGui.QVector3D(0, 0, 20.0))
        self.view.camera().setUpVector(QtGui.QVector3D(0, 1, 0))
        self.view.camera().setViewCenter(QtGui.QVector3D(0, 0, 0))

        lightEntity = Qt3DCore.QEntity(self.root_entity)
        light = Qt3DRender.QPointLight(lightEntity)
        light.setColor("white")
        light.setIntensity(1)
        lightEntity.addComponent(light)

        lightTransform = Qt3DCore.QTransform(lightEntity)
        # lightTransform.setTranslation(self.view.camera().position())
        lightTransform.setTranslation(QtGui.QVector3D(-1, 5, 18))
        lightEntity.addComponent(lightTransform)

        camController = Qt3DExtras.QFirstPersonCameraController(self.root_entity)
        camController.setCamera(self.view.camera())
        self.view.setRootEntity(self.root_entity)
        self.resize(1200, 800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewport = Viewport()
    viewport.show()
    sys.exit(app.exec_())
