class Block:
    def __init__(self, transform, scene):
        self.transform = transform

        scene.register_block(self)
