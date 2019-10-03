from Run import gameRegistry


class DefaultEntity():
    def __init__(self, name):
        self.name = name

        gameRegistry.registerEntity(self)
