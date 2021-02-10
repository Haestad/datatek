from person import Person


__project__ = 'Crypto'


class Sender(Person):

    def operate_cipher(self, message):
        """ Takes in a message and encodes it using the senders cipher and key

        :param message: String (message)
        :return: String (encoded message)
        """
        encoded_message = self.cipher.encode(message, self.key)
        print(f'encoded message: {encoded_message}')
        return encoded_message
