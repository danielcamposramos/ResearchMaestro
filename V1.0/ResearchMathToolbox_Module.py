
# ResearchMathToolbox Module
import sympy as sp
import numpy as np

class ResearchMathToolbox:
    def simplify_expression(self, expression):
        return sp.simplify(expression)

    def matrix_operations(self, matrix_a, matrix_b):
        return np.dot(matrix_a, matrix_b)
