""" This module contains the Calculator class. """
import numbers
import re

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

    def shunting_yard(self, input_queue):
        """ Takes in an "normal" input queue, and converts it to RPN.
        The RPN output is pushed to the output queue in the right order.
        """
        operator_stack = Stack()
        for item in input_queue:
            if isinstance(item, numbers.Number):
                self.output_queue.push(item)

            elif isinstance(item, Function):
                operator_stack.push(item)

            elif item == '(':
                operator_stack.push(item)

            elif item == ')':
                while not operator_stack.peek() == '(':
                    self.output_queue.push(operator_stack.pop())
                operator_stack.pop()

            elif isinstance(item, Operator):
                while not (operator_stack.is_empty() or operator_stack.peek() == '(' or
                           operator_stack.peek().strength < item.strength):
                    self.output_queue.push(operator_stack.pop())
                operator_stack.push(item)

        while not operator_stack.is_empty():
            self.output_queue.push(operator_stack.pop())

    def text_parser(self, txt):
        """ Takes in a string,
        and parses it into a list that shunting_yard() can understand.
        """
        output_list = []
        txt = txt.replace(" ", "").upper()
        while txt:
            number = re.search("^[-0-9.]+", txt)
            parentheses = re.search("^[()]", txt)

            func_targets = '|'.join(["^" + func for func in calc.functions.keys()])
            function = re.search(func_targets, txt)

            op_targets = '|'.join(["^" + op for op in calc.operators.keys()])
            operator = re.search(op_targets, txt)

            text_index = 0
            if number:
                output_list.append(float(number.group(0)))
                text_index = number.end(0)
            elif parentheses:
                output_list.append((parentheses.group(0)))
                text_index = parentheses.end(0)
            elif function:
                output_list.append(self.functions[function.group(0)])
                text_index = function.end(0)
            elif operator:
                output_list.append((self.operators[operator.group(0)]))
                text_index = operator.end(0)

            txt = txt[text_index:]

        return output_list

    def calculate_expression(self, txt):
        """ Takes in an expressing in string form,
        and uses the other methods in Calculator to calculate a result.
        """
        self.shunting_yard(self.text_parser(txt))
        return self.RPN()


if __name__ == '__main__':
    print('Uses the calculator methods directly:')
    calc = Calculator()
    print('result: ' + str(calc.functions['EXP'].execute(
        calc.operators['ADD'].execute(1, calc.operators['MULTIPLY'].execute(2, 3)))))

    print('\nUses self.output_queue and RPN():')
    calc.output_queue.push(1)
    calc.output_queue.push(2)
    calc.output_queue.push(3)
    calc.output_queue.push(calc.operators['MULTIPLY'])
    calc.output_queue.push(calc.operators['ADD'])
    calc.output_queue.push(calc.functions['EXP'])
    print(f'result: {calc.RPN()}')

    print('\nUses shunting_yard() in combination with RPN():')
    list_input = [calc.functions['EXP'],
                  '(', 1, calc.operators['ADD'], 2,
                  calc.operators['MULTIPLY'], 3, ')']
    calc.shunting_yard(list_input)
    print(f'result: {calc.RPN()}')

    print('\nUses text_parser() to parse a string, then shunting_yard(), then RPN():')
    text = "exp (1 add 2 multiply 3)"
    calc.shunting_yard(calc.text_parser(text))
    print(f'result: {calc.RPN()}')

    print('\nUses calculate_expression() to calculate different expressions')
    s1 = 'EXP (1 add 2 multiply 3)'
    s2 = '((15 DIVIDE (7 SUBTRACT (1 ADD 1))) MULTIPLY 3)SUBTRACT (2 ADD (1 ADD 1))'
    print(f'result: {calc.calculate_expression(s1)}')
    print(f'result: {calc.calculate_expression(s2)}')
