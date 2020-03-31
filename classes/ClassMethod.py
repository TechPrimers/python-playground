class ClassMethod:
    count = 0
    def __init__(self):
        ClassMethod.count += 1

    @classmethod
    def print(cls):
        print(f"Number of objects: {cls.count}")

    @staticmethod
    def printLog():
        print("Static Method: ", ClassMethod.count)

    def normal(self):
        print("normal")