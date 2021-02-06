from person import Person


__project__ = 'Crypto'


class Receiver(Person):

    def __init__(self):
        super().__init__()

    def operate_cipher(self, message, key):
        """ Takes in a encoded message and decodes it using the receivers cipher with the given key
        :param message: String (encoded message)
        :param key: String (key)
        :return: String (decoded message)
        """
        decoded_message = self.cipher.decode(message, self.key)
        print(decoded_message)
        return decoded_message
