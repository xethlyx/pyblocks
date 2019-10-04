class DefaultEntity():
    def __init__(self, name, registry):
        self.name = name

        registry.register_entity(self)
