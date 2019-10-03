# Manages all data going in and out


class Registry():
    def __init__(self):
        pass

    def __setattr__(self, attr, value):
        print("[REGISTRY] Attr {} has been changed to {}".format(attr, value))
