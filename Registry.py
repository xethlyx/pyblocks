# Manages all data going in and out
import uuid


class Registry():
    def __init__(self):
        self.entities = {}

    def __setattr__(self, attr, value):
        print("[REGISTRY] Attr {} has been changed to {}".format(attr, value))
        super(Registry, self).__setattr__(attr, value)

    def registerEntity(self, entity):
        """Register an entity in the Registry

        Parameters:
        entity (DefaultEntity): The default entity

        Returns:
        uuid: Generated UUID
        """
        def generateUuid():
            return uuid.uuid4()

        generatedUuid = generateUuid()

        while generatedUuid.hex in self.entities:
            generatedUuid = generateUuid()
            break

        self.entities[generatedUuid.hex] = generatedUuid
