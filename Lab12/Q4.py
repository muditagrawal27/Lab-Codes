class RegShape:
    def __init__(self):
        self.dimensions = {}
class Circle(RegShape):
    def dim(self):
        self.dimensions['radius'] = float(input("Enter the radius of the circle: "))
    def area(self):
        radius = self.dimensions['radius']
        return (3.14 * (radius ** 2))
    def perimeter(self):
        radius = self.dimensions['radius']
        return (2 * 3.14 * radius)
class Rectangle(RegShape):
    def dim(self):
        self.dimensions['length'] = float(input("Enter the length of the rectangle: "))
        self.dimensions['width'] = float(input("Enter the width of the rectangle: "))
    def area(self):
        length = self.dimensions['length']
        width = self.dimensions['width']
        return (length * width)
    def perimeter(self):
        length = self.dimensions['length']
        width = self.dimensions['width']
        return (2 * (length + width))
class Square(RegShape):
    def dim(self):
        self.dimensions['side'] = float(input("Enter the side of the square: "))
    def area(self):
        side = self.dimensions['side']
        return (side ** 2)
    def perimeter(self):
        side = self.dimensions['side']
        return (4 * side)
class Triangle(RegShape):
    def dim(self):
        self.dimensions['base'] = float(input("Enter the base of the triangle: "))
        self.dimensions['height'] = float(input("Enter the height of the triangle: "))
        self.dimensions['side1'] = float(input("Enter the length of side 1: "))
        self.dimensions['side2'] = float(input("Enter the length of side 2: "))
    def area(self):
        base = self.dimensions['base']
        height = self.dimensions['height']
        return (0.5 * base * height)
    def perimeter(self):
        side1 = self.dimensions['side1']
        side2 = self.dimensions['side2']
        base = self.dimensions['base']
        return (side1 + side2 + base)

print("Choose a regular shape to calculate:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
choice = int(input("Enter your choice (1, 2, 3 or 4): "))
if choice == 1:
     shape = Circle()
elif choice == 2:
    shape = Rectangle()
elif choice == 3:
    shape = Square()
elif choice == 4:
    shape = Triangle()
else:
    print("Invalid choice!")
    exit()
shape.dim()
print("Area:",shape.area())
print("Perimeter:",shape.perimeter())
