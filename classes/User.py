class User() :

    def __init__(self, input_name):
        self.private_name = input_name

    def get_name(self):
        return self.private_name;

    def set_name(self, input_name):
        self.private_name = input_name

    name = property(get_name, set_name)

