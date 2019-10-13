"""A .py file containing assets required for 3D rendering the scene"""

from Resources.TMatrix import TMatrix
from Resources.FSize import FSize


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

        if localTransform.get_value("zp") < 1:
            projectedX = (self.transform * localTransform.get_value("xp")) * (self.transform * localTransform.get_value("zp")).get_matrix_inverse()
            projectedY = (self.transform * localTransform.get_value("yp")) * (self.transform * localTransform.get_value("zp")).get_matrix_inverse()

            print(projectedX)
            print(projectedY)

    def render3d(self):
        self.tmatrix_to_position(TMatrix())
