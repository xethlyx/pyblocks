# Manages all data going in and out
import uuid


class Registry():
    def __init__(self):
        self.entities = {}

    def __setattr__(self, attr, value):
        print("[REGISTRY] Attr {} has been changed to {}".format(attr, value))
        super(Registry, self).__setattr__(attr, value)

    def register_entity(self, entity):
        """Register an entity in the Registry

        Parameters:
        entity (DefaultEntity): The default entity

        Returns:
        uuid: Generated UUID
        """
        def generate_uuid():
            return uuid.uuid4()

        generatedUuid = generate_uuid()

        while generatedUuid.hex in self.entities:
            generatedUuid = generate_uuid()
            break

        self.entities[generatedUuid.hex] = generatedUuid
