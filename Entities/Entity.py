class DefaultEntity():
    def __init__(self, name, registry):
        self.name = name

        registry.register_entity(self)

    def __str__(self):
        return self.name
