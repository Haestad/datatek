import random
from cipher import Cipher
from crypto_utils import modular_inverse


class Multiplication(Cipher):

    @staticmethod
    def encode(message, key):
        """ encodes the message with the Multiplication cipher and given key

        :param message: String (message to encode)
        :param key: Integer (key to encode with)
        :return: String (encoded message) """
        encoded_message = ''
        print('encoding message...')

        for letter in message:
            letter_num = (ord(letter) * key - 32) % Cipher.alphabet_size
            encoded_message += Cipher.alphabet[letter_num]
        return encoded_message

    @staticmethod
    def decode(message, key):
        """ decodes the message with the Multiplication cipher and given key

        :param message: String (message to decode)
        :param key: Integer (key to decode with)
        :return: String (decoded message) """
        decoded_message = ''
        print('decoding message...')

        inverse_key = modular_inverse(key, Cipher.alphabet_size)
        for letter in message:
            letter_num = (ord(letter) * inverse_key - 32) % Cipher.alphabet_size
            decoded_message += Cipher.alphabet[letter_num]
        return decoded_message

    def generate_keys(self):
        """ generates a key to encrypt/decrypt with, makes sure that the key has a modular inverse

        :return: random integer between 1 and 999"""
        key = random.randint(1, 999)
        while True:
            if not modular_inverse(key, Cipher.alphabet_size):
                key = random.randint(1, 999)
            else:
                return key
