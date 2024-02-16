
class Container:

    # Singleton
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Container, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._data = {}

    def bind(self, key, value):
        self._data[key] = value

    def resolve(self, key):
        return self._data[key]
    
    def __getitem__(self, key):
        return self.resolve(key)
    
    def __setitem__(self, key, value):
        self.bind(key, value)

    def __getattr__(self, key):
        return self.resolve(key)
    
    def __setattr__(self, key, value):
        self.bind(key, value)