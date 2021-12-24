class Rectangle:
    lenght = None
    weight = None
    @staticmethod
    def area_static(a, b):
        return a * b

    @classmethod
    def area_class(cls, a, b):
        cls.lenght = a
        cls.weight = b
        return cls.area_static(cls.lenght, cls.weight)


class Square(Rectangle):
    lenght = None

    @staticmethod
    def area_static(a):
        return a ** 2

    @classmethod
    def area_class(cls, a):
        cls.lenght = a
        return cls.area_static(cls.lenght)


a = Square()
print(a.area_class(4))

print(Square.area_static(5))

b = Rectangle()
print(b.area_class(3, 4))

print(Rectangle.area_static(5, 6))
