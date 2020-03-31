class UserAnnotation:

    def __init__(self, input_name):
        self.private_name = input_name

    @property
    def name(self):
        return self.private_name;

    @name.setter
    def name(self, input_name):
        self.private_name = input_name

