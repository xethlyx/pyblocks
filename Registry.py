# Manages all data going in and out
import Util
import Enum as CEnum


class Registry():
    def __init__(self):
        self.entities = {}
        self.settings = {
            "ShowFps": {
                "DisplayName": "Show FPS Counter",
                "InputType": CEnum.InputFieldType.Switch,
                "Value": False
            },
            "ShowVer": {
                "DisplayName": "Show Version",
                "InputType": CEnum.InputFieldType.Switch,
                "Value": False
            },
            "FpsLimit": {
                "DisplayName": "FPS Limit",
                "Value": 10
            }
        }

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
