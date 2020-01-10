class Block:
    def __init__(self, transform, scene):
        self.transform = transform

        self.obj = {
            "Vertices": {
                1: [-0.5, -0.5, -0.5],
                2: [0.5, -0.5, -0.5],
                3: [-0.5, 0.5, -0.5],
                4: [-0.5, -0.5, 0.5],
                5: [0.5, 0.5, -0.5],
                6: [-0.5, 0.5, 0.5],
                7: [0.5, -0.5, 0.5],
                8: [0.5, 0.5, 0.5]
            },
            "Faces": {
                1: [1, 2, 3, 4]

            }
        }

        scene.register_block(self)
