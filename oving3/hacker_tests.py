from caesar import Caesar
from hacker import Hacker
from multiplication import Multiplication
from affine import Affine
from unbreakable import Unbreakable
from sender import Sender

if __name__ == '__main__':
    c1 = Caesar()
    c2 = Multiplication()
    c3 = Affine()
    c4 = Unbreakable()
    s1 = Sender()
    h1 = Hacker()

    MESSAGE = "test message for checking if the hack works"

    # testing Caesar hacking
    key = c1.generate_keys()
    s1.set_cipher(c1)
    s1.set_key(key)

    encrypted_caesar = s1.operate_cipher(MESSAGE)
    h1.crack_caesar(encrypted_caesar)

    # testing Multiplication hacking
    key = c2.generate_keys()
    s1.set_cipher(c2)
    s1.set_key(key)

    encrypted_multi = s1.operate_cipher(MESSAGE)
    h1.crack_multiplication(encrypted_multi)

    # testing Affine hacking
    key = c3.generate_keys()
    s1.set_cipher(c3)
    s1.set_key(key)

    encrypted_affine = s1.operate_cipher(MESSAGE)
    h1.crack_affine(encrypted_affine)

    # testing Unbreakable hacking
    key = c4.generate_keys()
    s1.set_cipher(c4)
    s1.set_key(key)

    encrypted_unbreakable = s1.operate_cipher(MESSAGE)
    h1.crack_unbreakable(encrypted_unbreakable)
