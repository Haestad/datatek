""" This module contains the Keypad class. """
import time
from GPIOSimulator_v5 import *


class Keypad:
    """ The keypad class uses GPIOSimulator to simulate a real keypad,
        and polls the keyboard for legal inputs. """
    GPIO = GPIOSimulator()

    KEYPAD_VALUES = {
        (PIN_KEYPAD_ROW_0, PIN_KEYPAD_COL_0): 1,
        (PIN_KEYPAD_ROW_0, PIN_KEYPAD_COL_1): 2,
        (PIN_KEYPAD_ROW_0, PIN_KEYPAD_COL_2): 3,
        (PIN_KEYPAD_ROW_1, PIN_KEYPAD_COL_0): 4,
        (PIN_KEYPAD_ROW_1, PIN_KEYPAD_COL_1): 5,
        (PIN_KEYPAD_ROW_1, PIN_KEYPAD_COL_2): 6,
        (PIN_KEYPAD_ROW_2, PIN_KEYPAD_COL_0): 7,
        (PIN_KEYPAD_ROW_2, PIN_KEYPAD_COL_1): 8,
        (PIN_KEYPAD_ROW_2, PIN_KEYPAD_COL_2): 9,
        (PIN_KEYPAD_ROW_3, PIN_KEYPAD_COL_0): '*',
        (PIN_KEYPAD_ROW_3, PIN_KEYPAD_COL_1): 0,
        (PIN_KEYPAD_ROW_3, PIN_KEYPAD_COL_2): '#'
    }

    def __init__(self):
        for row_pin in keypad_row_pins:
            self.GPIO.setup(row_pin, self.GPIO.OUT)
        for col_pin in keypad_col_pins:
            self.GPIO.setup(col_pin, self.GPIO.IN)

    def do_polling(self):
        """ Determines the key currently being pressed on the keypad. """
        for row_pin in keypad_row_pins:
            self.GPIO.output(row_pin, self.GPIO.HIGH)
            for col_pin in keypad_col_pins:
                if self.GPIO.input(col_pin) == self.GPIO.HIGH:
                    self.GPIO.output(row_pin, self.GPIO.LOW)
                    return self.KEYPAD_VALUES[row_pin, col_pin]
            self.GPIO.output(row_pin, self.GPIO.LOW)
        return None

    def get_next_signal(self):
        """" Initiate repeated calls to do_polling until a key press is detected. """
        signal = None
        released = False
        while signal is None or not released:
            signal = self.do_polling()
            if signal is None:
                released = True
            time.sleep(0.001)
        return signal


if __name__ == '__main__':
    k1 = Keypad()
    while True:
        print(f'registered key press: {k1.get_next_signal()}')
