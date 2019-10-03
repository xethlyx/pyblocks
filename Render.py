class Camera:
    def __init__(self, fov, vector3, rmatrix):
        self.fov = fov

        self.Position = vector3
        self.Rotation = rmatrix

    def render3d(self):
        pass
