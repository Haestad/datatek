__project__ = 'Crypto'


class Person:

    def __init__(self):
        self.key = ''
        self.cipher = None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self, message, key):
        """dummy method for operating the cipher"""
        pass
