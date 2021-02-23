""" This module contains the Calculator class. """
import numpy

from function_operator import Function, Operator
from containers import Queue


class Calculator:
    """ This class contains a calculator,
    that can use its functions and operators
     to calculate an output from the given input. """

    def __init__(self):
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt)}

        self.operators = {'ADD': Operator(numpy.add, 0),
                          'MULTIPLY': Operator(numpy.multiply, 1),
                          'DIVIDE': Operator(numpy.divide, 1),
                          'SUBTRACT': Operator(numpy.subtract, 0)}

        self.output_queue = Queue()


if __name__ == '__main__':
    calc = Calculator()
    print(calc.functions['EXP'].execute(
        calc.operators['ADD'].execute(1,
                                      calc.operators['MULTIPLY'].execute(2, 3))))
