from cipher import Cipher
from caesar import Caesar
from multiplication import Multiplication
from crypto_utils import modular_inverse
from affine import Affine
from unbreakable import Unbreakable
from person import Person


class Hacker(Person):

    @property
    def words(self):
        file = open('english_words.txt')
        words = []
        for line in file.readlines():
            words.append(line.split()[0])
        file.close()
        return words

    def word_in_dictionary(self, word):
        """ Helper method to see if a word is in the hackers dictionary

        :param word: The word to check """
        if word in self.words:
            return True
        return False

    def crack_caesar(self, message):
        caesar = Caesar()
        for cracked_key in range(Cipher.alphabet_size):
            decoded_message = caesar.decode(message, cracked_key)
            decoded_words = decoded_message.split()
            if self.check_words(decoded_words):
                print(f'Cracked message "{message}" with key "{cracked_key}"')
                print(f'The decoded message is "{decoded_message}"')
                return decoded_message
        print("Couldn't crack the message")
        return None

    def crack_multiplication(self, message):
        multi = Multiplication()
        for cracked_key in range(1, 999):
            if modular_inverse(cracked_key, Cipher.alphabet_size):
                decoded_message = multi.decode(message, cracked_key)
                decoded_words = decoded_message.split()
                if self.check_words(decoded_words):
                    print(f'Cracked message "{message}" with key "{cracked_key}"')
                    print(f'The decoded message is "{decoded_message}"')
                    return decoded_message
        print("Couldn't crack the message")
        return None

    def crack_affine(self, message):
        affine = Affine()
        for multi_key in range(1, 999):
            if modular_inverse(multi_key, Cipher.alphabet_size):
                for caesar_key in range(Cipher.alphabet_size):
                    decoded_message = affine.decode(message, (caesar_key, multi_key))
                    decoded_words = decoded_message.split()
                    if self.check_words(decoded_words):
                        print(f'Cracked message "{message}" with key "({caesar_key}, {multi_key})"')
                        print(f'The decoded message is "{decoded_message}"')
                        return decoded_message
        print("Couldn't crack the message")
        return None

    def crack_unbreakable(self, message):
        unbreakable = Unbreakable()
        for word in self.words:
            decoded_message = unbreakable.decode(message, word)
            decoded_words = decoded_message.split()
            if self.check_words(decoded_words):
                print(f'Cracked message "{message}" with key "{word}"')
                print(f'The decoded message is "{decoded_message}"')
                return decoded_message
        print("Couldn't crack the message")
        return None

    def check_words(self, words):
        """ Helper method that checks if the given words are real words

        :param words: List of words to check """
        correct_words = 0
        for word in words:
            if self.word_in_dictionary(word):
                correct_words += 1
            elif len(word) == 1:
                correct_words += 1
        if correct_words == len(words):
            return True
        return False
