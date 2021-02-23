from person import Person


__project__ = 'Crypto'


class Receiver(Person):

    def operate_cipher(self, message):
        """ Takes in a encoded message and decodes it using the receivers cipher with the given key

        :param message: String (encoded message)
        :return: String (decoded message)
        """
        decoded_message = self.cipher.decode(message, self.key)
        print(f'decoded message: {decoded_message}')
        return decoded_message