"""This module contains the function class """
import numbers


class Function:
    """ This class contains a function,
    given by the type specified in the constructor.
    """

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
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
