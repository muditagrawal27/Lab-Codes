class Matrix:
    def __init__(self,data):
        if len(data)!=3 or any(len(row)!=3 for row in data):
            raise ValueError("Matrix must be 3x3")
        self.data = data
    def add(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])
    def sub(self, other):
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(3)] for i in range(3)])
    def mul(self, other):
        return Matrix([[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)])
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])
mat1= Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2= Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:\n", mat1.__str__())
print("Matrix 2:\n", mat2.__str__())
print("Addition:\n", mat1.add(mat2))
print("Subtraction:\n", mat1.sub(mat2))
print("Multiplication:\n", mat1.mul(mat2))
print("Transpose of Matrix 1:\n", mat1.transpose())
print("Transpose of Matrix 2:\n", mat2.transpose())