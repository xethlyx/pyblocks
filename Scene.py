"""Handles all blocks in the world"""


from warnings import warn
import uuid

from Resources.Matrix4 import Matrix4


class Scene:
    def __init__(self):
        self.blocks = {}

    def register_block(self, block, transform):
        blankMatrix4 = Matrix4()

        if not (transform.x == blankMatrix4 and transform.y == blankMatrix4 and transform.z == blankMatrix4):
            warn("A block should be kept with 0 rotation!", UserWarning)

        block.registeredUuid = uuid.uuid4()

        self.blocks[block.registeredUuid] = block

    def remove_block(self, block):
        del self.blocks[block.registeredUuid]
        del block.registeredUuid
