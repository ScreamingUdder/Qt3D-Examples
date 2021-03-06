#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide2 port of the qt3d/simple-cpp example from Qt v5.x"""

import sys
from PySide2.QtCore import Property, QObject, QPropertyAnimation, Signal, Slot
from PySide2.QtGui import QGuiApplication, QMatrix4x4, QQuaternion, QVector3D, QWindow
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DRender import Qt3DRender
from PySide2.Qt3DExtras import Qt3DExtras


class CylinderWindow(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super(CylinderWindow, self).__init__()

        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 0, 40))
        self.camera().setViewCenter(QVector3D(0, 0, 0))

        # For camera controls
        self.createScene()
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(50)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())

        self.setRootEntity(self.rootEntity)

        self.cylinders = []
        self.meshes = []
        self.transforms = []

    def createScene(self):
        # Root entity
        self.rootEntity = Qt3DCore.QEntity()

        # Material
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)

    def add_cylinder(self, radius, length, x, y, z, rings=10, slices=10):

        cylinderEntity = Qt3DCore.QEntity(self.rootEntity)
        cylinderMesh = Qt3DExtras.QCylinderMesh()
        cylinderMesh.setRadius(radius)
        cylinderMesh.setLength(length)
        cylinderMesh.setSlices(rings)
        cylinderMesh.setRings(slices)
        cylinderTransform = Qt3DCore.QTransform()
        cylinderTransform.setTranslation(QVector3D(x, y, z))

        cylinderEntity.addComponent(cylinderMesh)
        cylinderEntity.addComponent(self.material)
        cylinderEntity.addComponent(cylinderTransform)

        self.cylinders.append(cylinderEntity)
        self.meshes.append(cylinderMesh)
        self.transforms.append(cylinderTransform)
