"""Handles all blocks in the world"""


from Util import generate_unique_uuid_retry


class Scene:
    def __init__(self):
        self.blocks = {}

    def register_block(self, block):
        block.registeredUuid = generate_unique_uuid_retry(self.blocks)

        self.blocks[block.registeredUuid] = block

    def remove_block(self, block):
        del self.blocks[block.registeredUuid]
        del block.registeredUuid
