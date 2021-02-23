from cipher import Cipher
from oving3.crypto_utils import modular_inverse
from caesar import Caesar
from multiplication import Multiplication


class Affine(Cipher):

    def encode(self, message, key):
        """ encodes the message with the Affine cipher and given keys

        :param message: String (message to encode)
        :param key: Integer (key to encode with)
        :return: String (encoded message) """
        encoded_message = ''
        print('encoding message...')

        for letter in message:
            letter_first = (ord(letter) * key[1] - 32) % Cipher.alphabet_size
            letter_second = (ord(Cipher.alphabet[letter_first])
                             + key[0] - 32) % Cipher.alphabet_size
            encoded_message += Cipher.alphabet[letter_second]
        return encoded_message

    def decode(self, message, key):
        """ decodes the message with the Affine cipher and given keys

        :param message: String (message to decode)
        :param key: Integer (key to decode with)
        :return: String (decode message) """
        decoded_message = ''
        print('decoding message...')

        inverse_caesar = Cipher.alphabet_size - key[0]
        inverse_multi = modular_inverse(key[1], Cipher.alphabet_size)
        for letter in message:
            letter_first = (ord(letter) + inverse_caesar - 32) % Cipher.alphabet_size
            letter_second = (ord(Cipher.alphabet[letter_first])
                             * inverse_multi - 32) % Cipher.alphabet_size
            decoded_message += Cipher.alphabet[letter_second]
        return decoded_message

    def generate_keys(self):
        c_key = Caesar.generate_keys()
        m_key = Multiplication.generate_keys()
        return c_key, m_key
