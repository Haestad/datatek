"""This module contains the Function and Operator class,
 which are used for calculating the results when operating the calculator.
 """
import numbers
import numpy


class Function:
    """ This class contains a function,
    given by the type specified in the constructor.
    """

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=False):
        """ Executes self.func with the given element, and returns the result.
        If debug == True, prints the function and calculation in console.
        """
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.func(element)

        if debug:
            print(f'Function: {self.func.__name__}\n'
                  f'{element} = {result}')

        return result


class Operator:
    """ This class contains an operator,
        given by the type specified in the constructor.
        The operators strength is also specified.
        """

    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, element1, element2, debug=False):
        """ Executes self.operation with the given elements, and returns the result.
               If debug == True, prints the function and calculation in console.
               """
        if not isinstance(element1 and element2, numbers.Number):
            raise TypeError("The elements must be numbers")
        result = self.operation(element1, element2)

        if debug:
            print(f'Operator: {self.operation.__name__}\n'
                  f'{element1}, {element2} = {result}')

        return result


if __name__ == '__main__':
    # Checks that the Function class works as intended
    exponential_func = Function(numpy.exp)
    sin_func = Function(numpy.sin)
    print(exponential_func.execute(sin_func.execute(0)))
    # Checks that the Operator class works as intended
    add_op = Operator(numpy.add, 0)
    multiply_op = Operator(numpy.multiply, 1)
    print(add_op.execute(1, multiply_op.execute(2, 3)))
