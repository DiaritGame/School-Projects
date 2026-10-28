class Shape:
    def __init__(self, area, info):
        self.area = area
        self.info = info
    def square(self):
        pass
    def info(self):
        print(f"Информация о фигуре: {self.info}")
class Rectangle(Shape):
    height = 5
    width = 6
    def square(self):
        self.area = self.height * self.width
class Triangle(Shape):
    height = 7
    base = 8
    def square(self):
        self.area = 0.5 * self.height * self.base
class Circle(Shape):
    radius = 9
    def square(self):
        self.area = 3.14 * self.radius ** 2
rectangle = Rectangle(0, "Прямоугольник")
triangle = Triangle(0, "Треугольник")
circle = Circle(0, "Круг")
rectangle.square()
triangle.square()
circle.square()
print(f"Площадь прямоугольника: {rectangle.area}")
print(f"Площадь треугольника: {triangle.area}")
print(f"Площадь круга: {circle.area}")
rectangle.info()
triangle.info()
circle.info()