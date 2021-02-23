""" This module contains the Calculator class. """
import numbers

import numpy

from function_operator import Function, Operator
from containers import Queue, Stack


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

    def RPN(self):
        """ Goes through the output queue,
         and calculates and answer based on RPN.
         This is achieved by using a stack to store the results,
         and checking each item in output queue. """
        stack = Stack()
        while not self.output_queue.is_empty():
            item = self.output_queue.pop()
            if isinstance(item, numbers.Number):
                stack.push(item)
            elif isinstance(item, Function):
                stack.push(item.execute(stack.pop()))
            elif isinstance(item, Operator):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(item.execute(num1, num2))
        return stack.pop()


if __name__ == '__main__':
    print('Uses the calculator methods directly:')
    calc = Calculator()
    print(calc.functions['EXP'].execute(
        calc.operators['ADD'].execute(1,
                                      calc.operators['MULTIPLY'].execute(2, 3))))

    print('\nUses the output_queue and RPN()_')
    calc.output_queue.push(1)
    calc.output_queue.push(2)
    calc.output_queue.push(3)
    calc.output_queue.push(calc.operators['MULTIPLY'])
    calc.output_queue.push(calc.operators['ADD'])
    calc.output_queue.push(calc.functions['EXP'])
    print(calc.RPN())
