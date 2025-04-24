class Solid:
    def __init__(self):
        self.dimensions = {}
class Sphere(Solid):
    def dim(self):
        self.dimensions['radius'] = float(input("Enter the radius of the sphere: "))
    def area(self):
        radius = self.dimensions['radius']
        return (4 * 3.14 * (radius ** 2))
    def vol(self):
        radius = self.dimensions['radius']
        return ((4/3) * 3.14 * (radius ** 3))
class Cylinder(Solid):
    def dim(self):
        self.dimensions['radius'] = float(input("Enter the radius of the cylinder: "))
        self.dimensions['height'] = float(input("Enter the height of the cylinder: "))
    def area(self):
        radius = self.dimentions['radius']
        height = self.dimensions['height']
        return (2 * 3.14 * radius * (radius + height))
    def vol(self):
        radius = self.dimensions['radius']
        height = self.dimensions['height']
        return (3.14 * radius ** 2 * height)
    
print("Choose a solid to calculate:")
print("1. Sphere")
print("2. Cylinder")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
     solid = Sphere()
elif choice == 2:
    solid = Cylinder()
else:
    print("Invalid choice!")
    exit()
solid.dim()
print("Surface Area:",solid.area())
print("Volume:",solid.vol())