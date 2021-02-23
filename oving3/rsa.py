import random
from cipher import Cipher
from oving3.crypto_utils import blocks_from_text, text_from_blocks, generate_random_prime, modular_inverse


class RSA(Cipher):
    no_bits = 16

    def encode(self, message, key):
        text_blocks = blocks_from_text(message, 3)
        encoded_message = []
        for block in text_blocks:
            encoded_message.append(pow(block, key[1], key[0]))
        return encoded_message

    def decode(self, message, key):
        text_blocks = []
        for block in message:
            text_blocks.append(pow(block, key[1], key[0]))
        return text_from_blocks(text_blocks, self.no_bits)

    def generate_keys(self):
        """ generates a public and private key

        :return: n, e, d; public key = (n, e), private key = (n, d) """
        prime1 = generate_random_prime(self.no_bits)
        prime2 = generate_random_prime(self.no_bits)
        while prime1 == prime2:
            prime2 = generate_random_prime(self.no_bits)
        primes = prime1 * prime2
        phi = (prime1 - 1) * (prime2 - 1)
        public = random.randint(3, phi - 1)
        private = modular_inverse(public, phi)

        if not private:
            primes, public, private = self.generate_keys()

        return primes, public, private
