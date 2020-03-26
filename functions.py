class Functions:

    def __init__(self):
        self._cache = []

    def __call__(self, name):
        if name not in self._cache:
            self._cache.append(name)
        return self._cache