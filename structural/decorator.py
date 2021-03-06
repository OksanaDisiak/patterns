def decorator(cls):
    class Wrapper:
        def __init__(self, x):
            self.wrap = cls(x)

        def get_name(self):
            return self.wrap.name

    return Wrapper


@decorator
class C:
    def __init__(self, y):
        self.name = y

x = C("Geeks")
print(x.get_name())