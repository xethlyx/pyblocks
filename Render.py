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

        self.blockScale = 40

        if isinstance(transform, TMatrix):
            self.transform = transform
        else:
            raise Exception("Transform must be of type TMatrix!")

    def tmatrix_to_position(self, transform):
        """Transforms a TMatrix into screen coordinates.

        Arguments:
            transform (TMatrix) -- A TMatrix created using the TMatrix constructor.
        """

        canvasWidth, canvasHeight = self.registry.currentWindow.get_size()

        localTransform = transform * self.transform.get_matrix_inverse()

        if localTransform.get_value("zp") > 0:
            zScreen = -localTransform.get_value("zp")

            screenPosition = TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     localTransform.get_value("xp") * zScreen,
                                     localTransform.get_value("yp") * zScreen,
                                     0)

            if abs((screenPosition.get_value("xp") > canvasWidth) or (screenPosition.get_value("yp") > canvasHeight)):
                return False

            # Normalize screen pos

            screenPosition.set_value("xp", (screenPosition.get_value("xp") + canvasWidth / 2) / canvasWidth)
            screenPosition.set_value("yp", (screenPosition.get_value("yp") + canvasWidth / 2) / canvasWidth)

            return([abs(int(screenPosition.get_value("xp") * canvasWidth)), abs(int(screenPosition.get_value("yp") * canvasHeight))])

        return False

    def render3d(self):
        # Reset scene
        self.registry.currentWindow.fill((0, 0, 0))

        for blockUuid in self.registry.currentScene.blocks:
            print("found block")
            for vertexNumber in self.registry.currentScene.blocks[blockUuid].obj["Vertices"]:
                vertexPosition = TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][0] * self.blockScale,
                                         self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][1] * self.blockScale,
                                         self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][2] * self.blockScale)

                vertexPosition *= self.registry.currentScene.blocks[blockUuid].transform
                vertexPosition = self.tmatrix_to_position(vertexPosition)

                print("Drawing point at " + str(vertexPosition))

                if vertexPosition:
                    pygame.draw.circle(self.registry.currentWindow, (50, 50, 50), vertexPosition, 2)

        self.tmatrix_to_position(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 100, 200))
