class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def sub(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def mul(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    def div(self, other):
        d= other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag)/d
        imag = (self.imag * other.real - self.real * other.imag)/d
        return Complex(real, imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = Complex(4, 5)
c2 = Complex(2, 3)
print("Complex Number 1:", c1.__str__())
print("Complex Number 2:", c2.__str__())    
print("Addition:",c1.add(c2))
print("Subtraction:",c1.sub(c2))
print("Multiplication:",c1.mul(c2))
print("Division:",c1.div(c2))
