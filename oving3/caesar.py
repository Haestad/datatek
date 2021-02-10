import random
from cipher import Cipher

__project__ = 'Crypto'


class Caesar(Cipher):

    def encode(self, message, key):
        """ encodes the message with the Caesar cipher and given key

        :param message: String (message to encode)
        :param key: Integer (key to encode with)
        :return: String (encoded message) """
        encoded_message = ''
        print('encoding message...')

        for letter in message:
            # using "- 32" because the first letter in Cipher.alphabet has the value 32
            letter_num = (ord(letter) + key - 32) % Cipher.alphabet_size
            encoded_message += Cipher.alphabet[letter_num]
        return encoded_message

    def decode(self, message, key):
        """ decodes the message with the Caesar cipher and given key

        :param message: String (message to decode)
        :param key: Integer (key to decode with)
        :return: String (decode message) """
        decoded_message = ''
        print('decoding message...')

        inverse_key = Cipher.alphabet_size - key
        for letter in message:
            # using "- 32" because the first letter in Cipher.alphabet has the value 32
            # reverts the key value from the encrypted message
            letter_num = (ord(letter) + inverse_key - 32) % Cipher.alphabet_size
            decoded_message += Cipher.alphabet[letter_num]
        return decoded_message

    def generate_keys(self):
        """ generates a key to encrypt/decrypt with

        :return: random integer between 1 and the size of the alphabet"""
        return random.randint(1, Cipher.alphabet_size)
