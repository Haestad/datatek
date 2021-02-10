from cipher import Cipher


class Unbreakable(Cipher):

    def encode(self, message, key):
        encoded_message = ''
        print('encoding message...')
        matching_keystring = self.generate_matching_keystring(message, key)
        for letter in enumerate(message):
            message_letter = ord(message[letter[0]]) - 32
            keystring_letter = ord(matching_keystring[letter[0]]) - 32
            encoded_message += \
                Cipher.alphabet[(message_letter + keystring_letter) % Cipher.alphabet_size]
        return encoded_message

    def decode(self, message, key):
        decoded_message = ''
        print('decoding message...')

        decoding_key = self.generate_decoding_key(key)
        matching_keystring = self.generate_matching_keystring(message, decoding_key)
        for letter in enumerate(message):
            message_letter = ord(message[letter[0]]) - 32
            keystring_letter = ord(matching_keystring[letter[0]]) - 32
            decoded_message += \
                Cipher.alphabet[(message_letter + keystring_letter) % Cipher.alphabet_size]
        return decoded_message

    def generate_keys(self):
        key = input("Key for encoding:\n>> ").lower()
        return key

    @staticmethod
    def generate_matching_keystring(message, key):
        """ generates a keystring from the given key that's the same length as the message

        :param message: String (message to encode/decode)
        :param key: String (the key to decode/encode with)
        :return: String (a string of same length as message consisting of the given key) """
        matching_keystring = ''
        for message_letter in range(len(message)):
            key_letter = message_letter % len(key)
            matching_keystring += key[key_letter]
        return matching_keystring

    @staticmethod
    def generate_decoding_key(key):
        """ generates a decoding key that matches the encoding key given

        :param key: String (encoding key)
        :return: String (matching decoding key) """
        decoding_key = ''
        for letter in key:
            letter_num = Cipher.alphabet_size - (ord(letter) - 32) % Cipher.alphabet_size
            decoding_key += Cipher.alphabet[letter_num]
        return decoding_key
