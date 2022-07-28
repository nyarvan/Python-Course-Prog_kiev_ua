class InputErrorPrice(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class InputErrorGroup(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return f"{self.message}"