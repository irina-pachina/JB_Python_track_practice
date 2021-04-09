# 1
# class Matrix:
#     def __init__(self, rows, columns):
#         self.matrix = []
#         self.rows = int(rows)
#         self.columns = int(columns)
#
#     def __add__(self, other):
#         addition = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
#             addition.append(row)
#         return addition
#
#     def print_matrix(self):
#         print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))
#
#     def append(self, row):
#         self.matrix.append(row)
#
#
# rows_1, columns_1 = input().split()
# matrix_1 = Matrix(rows_1, columns_1)
# for _i in range(matrix_1.rows):
#     row = [int(x) for x in input().split()]
#     matrix_1.append(row)
#
# rows_2, columns_2 = input().split()
# matrix_2 = Matrix(rows_2, columns_2)
# for _i in range(matrix_2.rows):
#     row = [int(x) for x in input().split()]
#     matrix_2.append(row)
#
# if rows_1 == rows_2 and columns_1 == columns_2:
#     addition = matrix_1 + matrix_2
#     addition.print_matrix()
# else:
#     print("ERROR")

# 2
# class Matrix:
#     def __init__(self, rows, columns):
#         self.matrix = []
#         self.rows = int(rows)
#         self.columns = int(columns)
#
#     def __add__(self, other):
#         addition = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
#             addition.append(row)
#         return addition
#
#     def __mul__(self, multiplier):
#         mul = multiply(multiplier)
#         for i in range(self.rows):
#             row = list(map(lambda x: mul(x), self.matrix[i]))
#             multi.append(row)
#         return multi
#
#     def print_matrix(self):
#         print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))
#
#     def append(self, row):
#         self.matrix.append(row)
#
#
# def multiply(multiplier):
#     return lambda x: multiplier * x
#
#
# rows_1, columns_1 = input().split()
# matrix_1 = Matrix(rows_1, columns_1)
# for _i in range(matrix_1.rows):
#     row = [int(x) for x in input().split()]
#     matrix_1.append(row)
#
# multiplier = int(input())
# multi = Matrix(rows_1, columns_1)
# multi = matrix_1 * multiplier
# multi.print_matrix()

# 3
# def multiply(multiplier):
#     return lambda x: multiplier * x
#
#
# class Matrix:
#     def __init__(self, rows, columns):
#         self.matrix = []
#         self.rows = int(rows)
#         self.columns = int(columns)
#
#     def __add__(self, other):
#         addition = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
#             addition.append(row)
#         return addition
#
#     def __mul__(self, multiplier):
#         mul = multiply(multiplier)
#         multi = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x: mul(x), self.matrix[i]))
#             multi.append(row)
#         return multi
#
#     def multi_matrices(self, other):
#         multi = Matrix(self.rows, other.columns)
#
#         # iterate through rows of X
#         for i in range(self.rows):
#             # iterate through columns of Y
#             row = []
#             for j in range(other.columns):
#                 # iterate through rows of Y
#                 total = 0
#                 for k in range(other.rows):
#                     total += self.matrix[i][k] * other.matrix[k][j]
#                 row.append(total)
#             multi.append(row)
#
#         return multi
#
#     def print_matrix(self):
#         print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))
#
#     def append(self, row):
#         self.matrix.append(row)
#
#
# def add():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_1 == rows_2 and columns_1 == columns_2:
#         addition = matrix_1 + matrix_2
#         print("The result is:")
#         addition.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# def scalar():
#     rows, columns = input("Enter size of matrix:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#
#     multiplier = float(input("Enter constant:"))
#     multi = matrix * multiplier
#     print("The result is:")
#     multi.print_matrix()
#
#
# def multi_matrices():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_2 == columns_1:
#         multi = matrix_1.multi_matrices(matrix_2)
#         print("The result is:")
#         multi.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# while 1:
#     print("""1. Add matrices
# 2. Multiply matrix by a constant
# 3. Multiply matrices
# 0. Exit""")
#     action = int(input("Your choice:"))
#     if action == 0:
#         break
#     elif action == 1:
#         add()
#     elif action == 2:
#         scalar()
#     elif action == 3:
#         multi_matrices()

# 4
# def multiply(multiplier):
#     return lambda x: multiplier * x
#
#
# class Matrix:
#     def __init__(self, rows, columns):
#         self.matrix = []
#         self.rows = int(rows)
#         self.columns = int(columns)
#
#     def __add__(self, other):
#         addition = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
#             addition.append(row)
#         return addition
#
#     def __mul__(self, multiplier):
#         mul = multiply(multiplier)
#         multi = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x: mul(x), self.matrix[i]))
#             multi.append(row)
#         return multi
#
#     def multi_matrices(self, other):
#         multi = Matrix(self.rows, other.columns)
#
#         # iterate through rows of X
#         for i in range(self.rows):
#             # iterate through columns of Y
#             row = []
#             for j in range(other.columns):
#                 # iterate through rows of Y
#                 total = 0
#                 for k in range(other.rows):
#                     total += self.matrix[i][k] * other.matrix[k][j]
#                 row.append(total)
#             multi.append(row)
#
#         return multi
#
#     def transpose(self, diagonal):
#
#         if diagonal == 1:
#             transposed = Matrix(self.columns, self.rows)
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed.append(row)
#             return transposed
#         elif diagonal == 2:
#             transposed = Matrix(self.columns, self.rows)
#             self.matrix.reverse()
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed.append(row)
#             transposed.matrix.reverse()
#             return transposed
#         elif diagonal == 3:
#             transposed = Matrix(self.rows, self.columns)
#             for i in range(self.rows):
#                 row = self.matrix[i][::-1]
#                 transposed.append(row)
#             return transposed
#         elif diagonal == 4:
#             transposed = Matrix(self.rows, self.columns)
#             transposed_assist_1 = Matrix(self.columns, self.rows)
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed_assist_1.append(row)
#             transposed_assist_2 = Matrix(self.columns, self.rows)
#             for i in range(transposed_assist_1.rows):
#                 row = transposed_assist_1.matrix[i][::-1]
#                 transposed_assist_2.append(row)
#             for i in range(transposed_assist_2.rows):
#                 row = []
#                 for j in range(transposed_assist_2.columns):
#                     row.append(transposed_assist_2.matrix[j][i])
#                 transposed.append(row)
#             return transposed
#
#
#     def print_matrix(self):
#         print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))
#
#     def append(self, row):
#         self.matrix.append(row)
#
#
# def add():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_1 == rows_2 and columns_1 == columns_2:
#         addition = matrix_1 + matrix_2
#         print("The result is:")
#         addition.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# def scalar():
#     rows, columns = input("Enter size of matrix:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#
#     multiplier = float(input("Enter constant:"))
#     multi = matrix * multiplier
#     print("The result is:")
#     multi.print_matrix()
#
#
# def multi_matrices():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_2 == columns_1:
#         multi = matrix_1.multi_matrices(matrix_2)
#         print("The result is:")
#         multi.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# def transpose():
#     print("""1. Main diagonal
# 2. Side diagonal
# 3. Vertical line
# 4. Horizontal line""")
#     diagonal = int(input("Your choice:"))
#     rows, columns = input("Enter matrix size:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#     transposed = matrix.transpose(diagonal)
#     transposed.print_matrix()
#
#
# while 1:
#     print("""1. Add matrices
# 2. Multiply matrix by a constant
# 3. Multiply matrices
# 4. Transpose matrix
# 0. Exit""")
#     action = int(input("Your choice:"))
#     if action == 0:
#         break
#     elif action == 1:
#         add()
#     elif action == 2:
#         scalar()
#     elif action == 3:
#         multi_matrices()
#     elif action == 4:
#         transpose()

# 5
# def multiply(multiplier):
#     return lambda x: multiplier * x
#
#
# class Matrix:
#     def __init__(self, rows, columns):
#         self.matrix = []
#         self.rows = int(rows)
#         self.columns = int(columns)
#
#     def __add__(self, other):
#         addition = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
#             addition.append(row)
#         return addition
#
#     def __mul__(self, multiplier):
#         mul = multiply(multiplier)
#         multi = Matrix(self.rows, self.columns)
#         for i in range(self.rows):
#             row = list(map(lambda x: mul(x), self.matrix[i]))
#             multi.append(row)
#         return multi
#
#     def multi_matrices(self, other):
#         multi = Matrix(self.rows, other.columns)
#
#         # iterate through rows of X
#         for i in range(self.rows):
#             # iterate through columns of Y
#             row = []
#             for j in range(other.columns):
#                 # iterate through rows of Y
#                 total = 0
#                 for k in range(other.rows):
#                     total += self.matrix[i][k] * other.matrix[k][j]
#                 row.append(total)
#             multi.append(row)
#
#         return multi
#
#     def transpose(self, diagonal):
#
#         if diagonal == 1:
#             transposed = Matrix(self.columns, self.rows)
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed.append(row)
#             return transposed
#         elif diagonal == 2:
#             transposed = Matrix(self.columns, self.rows)
#             self.matrix.reverse()
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed.append(row)
#             transposed.matrix.reverse()
#             return transposed
#         elif diagonal == 3:
#             transposed = Matrix(self.rows, self.columns)
#             for i in range(self.rows):
#                 row = self.matrix[i][::-1]
#                 transposed.append(row)
#             return transposed
#         elif diagonal == 4:
#             transposed = Matrix(self.rows, self.columns)
#             transposed_assist_1 = Matrix(self.columns, self.rows)
#             for i in range(self.rows):
#                 row = []
#                 for j in range(self.columns):
#                     row.append(self.matrix[j][i])
#                 transposed_assist_1.append(row)
#             transposed_assist_2 = Matrix(self.columns, self.rows)
#             for i in range(transposed_assist_1.rows):
#                 row = transposed_assist_1.matrix[i][::-1]
#                 transposed_assist_2.append(row)
#             for i in range(transposed_assist_2.rows):
#                 row = []
#                 for j in range(transposed_assist_2.columns):
#                     row.append(transposed_assist_2.matrix[j][i])
#                 transposed.append(row)
#             return transposed
#
#     def get_minor(self, i, j):
#         return [row[:j] + row[j+1:] for row in (self.matrix[:i] + self.matrix[i+1:])]
#
#     def get_determinant(self):
#         if len(self.matrix) == 2:
#             return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
#         elif len(self.matrix) == 1:
#             return self.matrix[0][0]
#
#         determinant = 0
#         for c in range(len(self.matrix)):
#             minor = Matrix(self.rows - (c + 1), self.columns - (c + 1))
#             minor.matrix = self.get_minor(0,c)
#             determinant += ((-1) ** c) * self.matrix[0][c] * minor.get_determinant()
#         return determinant
#
#     def print_matrix(self):
#         print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))
#
#     def append(self, row):
#         self.matrix.append(row)
#
#
# def add():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_1 == rows_2 and columns_1 == columns_2:
#         addition = matrix_1 + matrix_2
#         print("The result is:")
#         addition.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# def scalar():
#     rows, columns = input("Enter size of matrix:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#
#     multiplier = float(input("Enter constant:"))
#     multi = matrix * multiplier
#     print("The result is:")
#     multi.print_matrix()
#
#
# def multi_matrices():
#     rows_1, columns_1 = input("Enter size of first matrix:").split()
#     print("Enter first matrix:")
#     matrix_1 = Matrix(rows_1, columns_1)
#     for _i in range(matrix_1.rows):
#         row = [float(x) for x in input().split()]
#         matrix_1.append(row)
#
#     rows_2, columns_2 = input("Enter size of second matrix:").split()
#     print("Enter second matrix:")
#     matrix_2 = Matrix(rows_2, columns_2)
#     for _i in range(matrix_2.rows):
#         row = [float(x) for x in input().split()]
#         matrix_2.append(row)
#
#     if rows_2 == columns_1:
#         multi = matrix_1.multi_matrices(matrix_2)
#         print("The result is:")
#         multi.print_matrix()
#     else:
#         print("The operation cannot be performed.")
#
#
# def transpose():
#     print("""1. Main diagonal
# 2. Side diagonal
# 3. Vertical line
# 4. Horizontal line""")
#     diagonal = int(input("Your choice:"))
#     rows, columns = input("Enter matrix size:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#     transposed = matrix.transpose(diagonal)
#     transposed.print_matrix()
#
#
# def calc_determinant():
#     rows, columns = input("Enter matrix size:").split()
#     print("Enter matrix:")
#     matrix = Matrix(rows, columns)
#     for _i in range(matrix.rows):
#         row = [float(x) for x in input().split()]
#         matrix.append(row)
#     print(matrix.get_determinant())
#
#
# while 1:
#     print("""1. Add matrices
# 2. Multiply matrix by a constant
# 3. Multiply matrices
# 4. Transpose matrix
# 5. Calculate a determinant
# 0. Exit""")
#     action = int(input("Your choice:"))
#     if action == 0:
#         break
#     elif action == 1:
#         add()
#     elif action == 2:
#         scalar()
#     elif action == 3:
#         multi_matrices()
#     elif action == 4:
#         transpose()
#     elif action == 5:
#         calc_determinant()

# 6
class Matrix:
    def __init__(self, rows, columns):
        self.matrix = []
        self.rows = int(rows)
        self.columns = int(columns)

    def __add__(self, other):
        addition = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            row = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
            addition.append(row)
        return addition

    def __mul__(self, multiplier):
        mul = multiply(multiplier)
        multi = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            row = list(map(lambda x: mul(x), self.matrix[i]))
            multi.append(row)
        return multi

    def entry(self):
        for _i in range(self.rows):
            row = [float(x) for x in input().split()]
            self.append(row)

    def multiply_matrices(self, other):
        multi = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                total = 0
                for k in range(other.rows):
                    total += self.matrix[i][k] * other.matrix[k][j]
                row.append(total)
            multi.append(row)
        return multi

    def transpose(self, diagonal):
        if diagonal == 1:
            transposed = Matrix(self.columns, self.rows)
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    row.append(self.matrix[j][i])
                transposed.append(row)
            return transposed
        elif diagonal == 2:
            transposed = Matrix(self.columns, self.rows)
            self.matrix.reverse()
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    row.append(self.matrix[j][i])
                transposed.append(row)
            transposed.matrix.reverse()
            return transposed
        elif diagonal == 3:
            transposed = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                row = self.matrix[i][::-1]
                transposed.append(row)
            return transposed
        elif diagonal == 4:
            transposed = Matrix(self.rows, self.columns)
            transposed_assist_1 = Matrix(self.columns, self.rows)
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    row.append(self.matrix[j][i])
                transposed_assist_1.append(row)
            transposed_assist_2 = Matrix(self.columns, self.rows)
            for i in range(transposed_assist_1.rows):
                row = transposed_assist_1.matrix[i][::-1]
                transposed_assist_2.append(row)
            for i in range(transposed_assist_2.rows):
                row = []
                for j in range(transposed_assist_2.columns):
                    row.append(transposed_assist_2.matrix[j][i])
                transposed.append(row)
            return transposed

    def get_minor(self, i, j):
        return [row[:j] + row[j+1:] for row in (self.matrix[:i] + self.matrix[i+1:])]

    def determinant(self):
        if len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        elif len(self.matrix) == 1:
            return self.matrix[0][0]

        determinant = 0
        for c in range(len(self.matrix)):
            minor = Matrix(self.rows - (c + 1), self.columns - (c + 1))
            minor.matrix = self.get_minor(0,c)
            determinant += ((-1) ** c) * self.matrix[0][c] * minor.determinant()
        return determinant

    def get_cofactors(self):
        cofactors = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            cofactors_row = []
            for j in range(self.columns):
                minor = Matrix(self.rows - (i + 1), self.columns - (i + 1))
                minor.matrix = self.get_minor(i, j)
                cofactors_row.append(((-1) ** (i+j)) * minor.determinant())
            cofactors.matrix.append(cofactors_row)
        return cofactors

    def inverse(self):
        inverted = Matrix(self.rows, self.columns)
        det = self.determinant()
        if det != 0:
            cofactors = self.get_cofactors()
            adj = cofactors.transpose(1)
            multiplier = 1 / det
            inverted = adj * multiplier
        else:
            print("This matrix doesn't have an inverse.")
        return inverted

    def print_matrix(self):
        print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in self.matrix]))

    def append(self, row):
        self.matrix.append(row)


def multiply(multiplier):
    return lambda x: multiplier * x


def add():
    rows_1, columns_1 = input("Enter size of first matrix:").split()
    print("Enter first matrix:")
    matrix_1 = Matrix(rows_1, columns_1)
    matrix_1.entry()

    rows_2, columns_2 = input("Enter size of second matrix:").split()
    print("Enter second matrix:")
    matrix_2 = Matrix(rows_2, columns_2)
    matrix_2.entry()

    if rows_1 == rows_2 and columns_1 == columns_2:
        addition = matrix_1 + matrix_2
        print("The result is:")
        addition.print_matrix()
    else:
        print("The operation cannot be performed.")


def constant():
    rows, columns = input("Enter size of matrix:").split()
    print("Enter matrix:")
    matrix = Matrix(rows, columns)
    matrix.entry()

    multiplier = float(input("Enter constant:"))
    multi = matrix * multiplier
    print("The result is:")
    multi.print_matrix()


def multiply_matrices():
    rows_1, columns_1 = input("Enter size of first matrix:").split()
    print("Enter first matrix:")
    matrix_1 = Matrix(rows_1, columns_1)
    matrix_1.entry()

    rows_2, columns_2 = input("Enter size of second matrix:").split()
    print("Enter second matrix:")
    matrix_2 = Matrix(rows_2, columns_2)
    matrix_2.entry()

    if rows_2 == columns_1:
        multi = matrix_1.multiply_matrices(matrix_2)
        print("The result is:")
        multi.print_matrix()
    else:
        print("The operation cannot be performed.")


def transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    diagonal = int(input("Your choice:"))
    rows, columns = input("Enter matrix size:").split()
    print("Enter matrix:")
    matrix = Matrix(rows, columns)
    matrix.entry()
    transposed = matrix.transpose(diagonal)
    transposed.print_matrix()


def calc_determinant():
    rows, columns = input("Enter matrix size:").split()
    print("Enter matrix:")
    matrix = Matrix(rows, columns)
    matrix.entry()
    print(matrix.determinant())


def inverse():
    rows, columns = input("Enter matrix size:").split()
    print("Enter matrix:")
    matrix = Matrix(rows, columns)
    matrix.entry()
    inverted = matrix.inverse()
    inverted.print_matrix()


while 1:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    action = int(input("Your choice:"))
    if action == 1:
        add()
    elif action == 2:
        constant()
    elif action == 3:
        multiply_matrices()
    elif action == 4:
        transpose()
    elif action == 5:
        calc_determinant()
    elif action == 6:
        inverse()
    elif action == 0:
        break


# Program can read and output matrices, do operations on them - addition, multiplying by a constant, multiplying 2 matrices,
# compute the determinant of a square matrix, transpose and inverse them.