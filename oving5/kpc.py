""" This module contains the KeyPad Controller (KPC) class. """
from time import sleep
from typing import Callable
from keypad import Keypad
from led_board import LEDBoard


class KPC:
    """ Class that contains all the logic for operating the keypad. """

    def __init__(self):
        self.keypad = Keypad()
        self.led_board = LEDBoard()
        self.password_path = "password.txt"
        self.override_signal = None
        self.current_signal = None
        self.passcode_buffer = ""
        self.led_pin = 0
        self.led_duration = 0

    def reset_passcode_entry(self):
        """ Clear passcode_buffer and initiate 'power up' lighting sequence. """
        self.passcode_buffer = ""
        self.power_up_leds()

    def reset_agent(self):
        """ Resets the agent to a neutral state. """
        self.override_signal = None
        self.current_signal = None
        self.passcode_buffer = ""

    def append_next_password_digit(self):
        """ Adds the given digit to the passcode_buffer. """
        self.passcode_buffer += str(self.current_signal)

    def get_next_signal(self):
        """ return override signal if non-blank,
            else query keypad for next pressed key"""
        if self.override_signal is not None:
            override_signal = self.override_signal
            self.override_signal = None
            return override_signal
        self.current_signal = self.keypad.get_next_signal()
        return self.current_signal

    def verify_login(self):
        """ Compares the password in the password file to the password in passcode_buffer.
            If it matches, set override_signal to 'Y', else set it to 'N'. """
        with open(self.password_path, 'r') as pw_file:
            correct_pw = pw_file.read()
        if self.passcode_buffer == correct_pw:
            self.override_signal = 'Y'
            self.twinkle_leds()
        else:
            self.override_signal = 'N'
            self.flash_leds()

    def validate_password_change(self):
        """ Checks if the new password is legal. A legal password should be at least 4 digits long,
            and should only contain a combination of symbols 0-9.
            If the password is legal, save it to 'password.txt'. The LED board should also flash
            based on failure or success. """
        if len(self.passcode_buffer) >= 4:
            with open(self.password_path, 'w') as pw_file:
                pw_file.write(self.passcode_buffer)
            self.override_signal = 'Y'
            self.twinkle_leds()
        else:
            self.override_signal = 'N'
            self.flash_leds()

    def fully_activate_agent(self):
        """ Called when agent is activated. """
        self.reset_agent()

    def exit_action(self):
        """ Called when exiting agent. """
        self.reset_agent()
        self.power_down_leds()

    def select_pin(self):
        """ Selects a LED pin to light up. """
        self.led_pin = self.current_signal

    def append_dur(self):
        """ Selects how long the LED should light up. """
        self.led_duration += int(self.current_signal)

    @staticmethod
    def do_action(action: Callable[[], bool]):
        """ Executes the given action in KPC. """
        return action()

    def light_one_led(self):
        """ Lights the LED with the agents led pin and duration, and then clears the values. """
        self.led_board.turn_on_led(self.led_pin)
        sleep(self.led_duration)
        self.led_board.turn_off_led(self.led_pin)
        self.led_pin = None
        self.led_duration = 0

    def flash_leds(self):
        """ Flashes all LEDs for 1 seconds. """
        self.led_board.flash_all_leds(1)

    def twinkle_leds(self):
        """ Twinkles all LEDs for 1 seconds """
        self.led_board.twinkle_all_leds(1)

    def power_up_leds(self):
        """ The LED sequence for powering up. """
        leds = []
        for i in range(0, 5):
            leds.append(i)
            self.led_board.flash_all_leds(0.2, leds)

    def power_down_leds(self):
        """ The LED sequence for powering down. """
        leds = [0, 1, 2, 3, 4]
        for i in range(0, 5):
            self.led_board.flash_all_leds(0.2, leds)
            leds.pop()