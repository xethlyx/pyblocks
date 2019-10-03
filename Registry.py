# Manages all data going in and out
import uuid


class Registry():
    def __init__(self):
        self.entities = {}

    def __setattr__(self, attr, value):
        print("[REGISTRY] Attr {} has been changed to {}".format(attr, value))

    def registerEntity(self, entity):
        def generateUuid():
            return uuid.uuid4()

        generatedUuid = generateUuid()

        while generatedUuid.hex in self.entities:
            print("generated uuid")
            self.entities[generatedUuid] = generatedUuid

        print("done!")
