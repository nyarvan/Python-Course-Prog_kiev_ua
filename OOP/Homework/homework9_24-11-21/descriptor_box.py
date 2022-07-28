class BoxDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("Field is read only")

    def __delete__(self, instance_self):
        raise AttributeError("Cannot delete field")

