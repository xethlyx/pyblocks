# Manages all data going in and out
import Util


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
        generatedUuid = Util.generate_unique_uuid_retry(self.entities)

        print("[REGISTRY] Entity {} has been registered with UUID {}".format(entity, generatedUuid.hex))

        self.entities[generatedUuid.hex] = generatedUuid
