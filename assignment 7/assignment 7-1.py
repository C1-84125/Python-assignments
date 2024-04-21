class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def accept(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(input(f"Enter element at position ({i+1},{j+1}): "))

    def print(self):
        for row in self.matrix:
            print(row)

    def addition(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return result
        else:
            raise Exception("Matrices should have the same dimensions for addition")

    def subtraction(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return result
        else:
            raise Exception("Matrices should have the same dimensions for subtraction")

    def multiplication(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            result.matrix = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
            return result
        else:
            raise Exception("Number of columns in the first matrix should be equal to the number of rows in the second matrix for multiplication")


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


matrix1 = Matrix(rows, cols)
matrix2 = Matrix(rows, cols)


print("Enter elements for matrix1:")
matrix1.accept()


print("Enter elements for matrix2:")
matrix2.accept()


print("Matrix1:")
matrix1.print()
print("Matrix2:")
matrix2.print()


addition_result = matrix1.addition(matrix2)
print("Addition Result:")
addition_result.print()


subtraction_result = matrix1.subtraction(matrix2)
print("Subtraction Result:")
subtraction_result.print()


multiplication_result = matrix1.multiplication(matrix2)
print("Multiplication Result:")
multiplication_result.print()
