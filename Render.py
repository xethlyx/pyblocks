"""A .py file containing assets required for 3D rendering the scene"""


from Resources.TMatrix import TMatrix


class Camera:
    def __init__(self, fov, transform):
        self.fov = fov

        if isinstance(transform, TMatrix):
            self.transform = transform
        else:
            raise Exception("Transform must be of type TMatrix!")

    def render3d(self):
        pass
