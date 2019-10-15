"""A .py file containing assets required for 3D rendering the scene"""

import pygame

from Resources.TMatrix import TMatrix


class Camera:
    def __init__(self, fov, transform, registry):
        """Create a new camera.

        Arguments:
            fov (int) -- The field of view in degrees.
            transform (TMatrix) -- The TMatrix including rotation and vector.
            registry (Registry) -- The Registry to pull information from.

        Raises:
            Exception: Transform must be of type TMatrix.
        """
        self.fov = fov
        self.registry = registry

        if isinstance(transform, TMatrix):
            self.transform = transform
        else:
            raise Exception("Transform must be of type TMatrix!")

    def tmatrix_to_position(self, transform):
        """Transforms a TMatrix into screen coordinates.

        Arguments:
            transform (TMatrix) -- A TMatrix created using the TMatrix constructor.
        """

        width, height = self.registry.currentWindow.get_size()
        # biggestDim = max((width, height))

        localTransform = transform * self.transform.get_matrix_inverse()

        # frameSize = FSize(biggestDim, biggestDim)

        if localTransform.get_value("zp") > 0:
            transformedZ = self.transform * localTransform.get_value("zp")
            transformedZ.set_scale(1)
            transformedZ = transformedZ.get_matrix_inverse()

            projectedX = self.transform * localTransform.get_value("xp")
            projectedY = self.transform * localTransform.get_value("yp")

            projectedX.set_scale(1)
            projectedY.set_scale(1)

            projectedX = projectedX * transformedZ
            projectedY = projectedY * transformedZ

    def render3d(self):
        for block in self.registry.currentScene.blocks:
            print("block found")
            for num, vertex in block.obj["Verticies"]:
                pygame.draw.circle(self.registry.currentWindow, (50, 50, 50))

        self.tmatrix_to_position(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 100, 200))
        pygame.draw.polygon(self.registry.currentWindow, (50, 50, 50), ())
