from person import Person


__project__ = 'Crypto'


class Sender(Person):

    def __init__(self):
        super().__init__()

    def operate_cipher(self, message, key):
        """ Takes in a message and encodes it using the senders cipher with the given key
        :param message: String (message)
        :param key: String (key)
        :return: String (encoded message)
        """
        encoded_message = self.cipher.encode(message, self.key)
        print(encoded_message)
        return encoded_message
