import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def get_row(matrix, row):
    """
    return the row
    :param matrix:
    :param row:
    :return:
    """
    return matrix[row]


def get_column(matrix, column_number):
    """
    return the column
    :param matrix:
    :param column:
    :return:
    """
    column = []
    for j in range(len(matrix)):
        column.append(matrix[j][column_number])

    return column


def dot_product(vector_one, vector_two):
    """
    return multiplication of row * column
    :param vector_one:
    :param vector_two:
    :return:
    """
    result = 0

    for i in range(len(vector_one)):
        result = result + (vector_one[i] * vector_two[i])

    return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        #This logis is for matrix 1x1
        if self.h == 1 and self.w == 1:
            determinant_matrix = self.g[0][0]
        #Begin logic for matric 2x2
        if self.h == 2 and self.w == 2:
            determinant_matrix = self.g[1][1] * self.g[0][0] - self.g[0][1]*self.g[1][0]
          
        return determinant_matrix

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        addition = 0
        
        for i in range(self.h):
            addition = addition + self.g[i][i]
        
        return addition

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        inverse = zeroes(self.h, self.w)
                
        # For Matrix 1x1
        if self.h == 1 and self.w == 1:
            inverse_determinant = 1 / self.determinant()
            inverse[0][0] = inverse_determinant
    
        # For Matrix 2x2
        if self.h == 2 and self.w == 2:
            #check if matrix has an inverse
            if self.determinant() == 0:
                raise(ZeroDivisionError, "This matrix is not invertible")
            
            else:
                inverse_determinant = 1 / self.determinant()
                inverse[0][1] = -self.g[0][1] * inverse_determinant
                inverse[1][0] = -self.g[1][0] * inverse_determinant
                inverse[1][1] = self.g[0][0] * inverse_determinant
                inverse[0][0] = self.g[1][1] * inverse_determinant
                
        return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        transpose_matrix = zeroes(self.w, self.h)
        
        for i in range(self.h):
            for j in range(self.w):
                transpose_matrix.g[j][i] = self.g[i][j]
                
             
        return transpose_matrix

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        new_matrix = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append( self[i][j] + other[i][j])
            new_matrix.append(new_row)
            
        return Matrix(new_matrix)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        new_matrix = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(-1 * self[i][j] )
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        new_matrix = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self[i][j] - other[i][j])
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        new_matrix = []
        
        for i in range(self.h):
            new_row = []
            for j in range(other.w):
                new_row.append(dot_product(get_row(self.g, i),get_column(other.g, j)))
            new_matrix.append(new_row)
        return Matrix(new_matrix)
    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
            new_matrix = Matrix(self.g)
            
            for i in range(self.h):
                for j in range(self.w):
                    new_matrix[i][j] = self.g[i][j] * other
            return (new_matrix)