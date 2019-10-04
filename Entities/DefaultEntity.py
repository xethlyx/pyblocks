class DefaultEntity():
    def __init__(self, name, registry):
        self.name = name

        registry.registerEntity(self)
