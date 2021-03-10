""" This module contains the class for the LED board """
import sys
from time import time, sleep

from GPIOSimulator_v5 import GPIOSimulator, charlieplexing_pins


class LEDBoard:
    """ This class contains the LED Board. """
    GPIO = GPIOSimulator()
    # (high, low)
    LED_MAP = [(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)]

    def get_pin_values(self, led_index):
        """ Returns the value the charlieplexed pins need to turn on a specific LED. """
        c_pin_high = charlieplexing_pins[(self.LED_MAP[led_index])[0]]
        c_pin_low = charlieplexing_pins[(self.LED_MAP[led_index])[1]]

        c_pin_inactive = None
        for i in range(len(charlieplexing_pins)):
            if i not in (self.LED_MAP[led_index][0], self.LED_MAP[led_index][1]):
                c_pin_inactive = charlieplexing_pins[i]
                break

        return c_pin_high, c_pin_low, c_pin_inactive

    def turn_on_led(self, led_index):
        """ Lights the LED on the given index. """
        pins = self.get_pin_values(led_index)
        self.GPIO.setup(pins[0], self.GPIO.OUT)
        self.GPIO.output(pins[0], self.GPIO.HIGH)
        self.GPIO.setup(pins[1], self.GPIO.OUT)
        self.GPIO.output(pins[1], self.GPIO.LOW)
        self.GPIO.setup(pins[2], self.GPIO.IN)

        self.GPIO.show_leds_states()

    def turn_off_led(self, led_index):
        pins = self.get_pin_values(led_index)
        self.GPIO.setup(pins[0], self.GPIO.IN)
        self.GPIO.setup(pins[1], self.GPIO.IN)

        self.GPIO.show_leds_states()

    def flash_all_leds(self, k, leds=[led for led in range(len(LED_MAP))]):
        """ Flashes all LEDs on and off for k seconds. """
        self.twinkle_all_leds(k, leds, sleep_time=0.03)

    def twinkle_all_leds(self, k, leds=[led for led in range(len(LED_MAP))], sleep_time=0.3):
        """ Turn all LEDs on and off in a sequence for k seconds. """
        start_time = time()
        while time() < start_time + k:
            for led in leds:
                self.turn_on_led(led)
                sleep(sleep_time)
                self.turn_off_led(led)


if __name__ == '__main__':
    led = LEDBoard()
    led.flash_all_leds(3)
