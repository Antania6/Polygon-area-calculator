# Define a base class for all shapes
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")

# Define a Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Define a Square class that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)

# Create objects for a circle, rectangle, and square
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)
square = Square("Square", 3)

# Compute and print the area and perimeter of each shape
print(f"Circle: area={circle.area():.2f}, perimeter={circle.perimeter():.2f}")
print(f"Rectangle: area={rectangle.area():.2f}, perimeter={rectangle.perimeter():.2f}")
print(f"Square: area={square.area():.2f}, perimeter={square.perimeter():.2f}")