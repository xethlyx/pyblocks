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

        self.blockScale = 20

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
        frameSize = max(canvasHeight, canvasHeight)

        localTransform = transform * self.transform.get_matrix_inverse()
        localTransform *= self.blockScale
        localTransform.set_scale(1)

        if localTransform.get_value("zp") > 0:
            zScreen = -localTransform.get_value("zp")

            screenPosition = TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     localTransform.get_value("xp") * zScreen,
                                     localTransform.get_value("yp") * zScreen,
                                     0)

            if abs((screenPosition.get_value("xp") > canvasWidth) or (screenPosition.get_value("yp") > canvasHeight)):
                return False

            # Normalize screen pos

            screenPosition.set_value("xp", (screenPosition.get_value("xp") + frameSize / 2) / frameSize)
            screenPosition.set_value("yp", (screenPosition.get_value("yp") + frameSize / 2) / frameSize)

            return([abs(int(screenPosition.get_value("xp") * frameSize)), abs(int(screenPosition.get_value("yp") * frameSize))])

        return False

    def render3d(self):
        def get_vertex_screen_pos(x, y, z):
            vertexPosition = TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, x, y, z)

            vertexPosition *= self.registry.currentScene.blocks[blockUuid].transform
            vertexPosition = self.tmatrix_to_position(vertexPosition)

            return vertexPosition

        # Reset scene
        self.registry.currentWindow.fill((0, 0, 0))

        for blockUuid in self.registry.currentScene.blocks:
            print("found block")
            for vertexNumber in self.registry.currentScene.blocks[blockUuid].obj["Vertices"]:
                vertexPosition = get_vertex_screen_pos(self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][0],
                                                       self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][1],
                                                       self.registry.currentScene.blocks[blockUuid].obj["Vertices"][vertexNumber][2])

                print("Drawing point at " + str(vertexPosition))

                if vertexPosition:
                    pygame.draw.circle(self.registry.currentWindow, (50, 50, 50), vertexPosition, 2)

                    # Draw secondary vertex pos with line
                    for secondaryVertexNumber in self.registry.currentScene.blocks[blockUuid].obj["Vertices"]:
                        secondaryVertexPosition = get_vertex_screen_pos(self.registry.currentScene.blocks[blockUuid].obj["Vertices"][secondaryVertexNumber][0],
                                                                        self.registry.currentScene.blocks[blockUuid].obj["Vertices"][secondaryVertexNumber][1],
                                                                        self.registry.currentScene.blocks[blockUuid].obj["Vertices"][secondaryVertexNumber][2])

                        if secondaryVertexPosition:
                            pygame.draw.line(self.registry.currentWindow, (255, 255, 255), vertexPosition, secondaryVertexPosition)

        self.tmatrix_to_position(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 100, 200))
