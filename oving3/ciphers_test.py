from multiplication import Multiplication
from affine import Affine
from oving3.cipher import Cipher
from rsa import RSA
from unbreakable import Unbreakable
from sender import Sender
from receiver import Receiver
from caesar import Caesar

if __name__ == '__main__':
    c1 = Caesar()
    c2 = Multiplication()
    c3 = Affine()
    c4 = Unbreakable()
    c5 = RSA()

    s1 = Sender()
    r1 = Receiver()

    MESSAGE = "what if i change the message?"

    # test Caesar
    key = c1.generate_keys()

    s1.set_cipher(c1)
    s1.set_key(key)

    r1.set_cipher(c1)
    r1.set_key(key)

    enc_melding = s1.operate_cipher(MESSAGE)
    dec_melding = r1.operate_cipher(enc_melding)

    if Cipher.verify(MESSAGE, dec_melding):
        print("verified melding 1")

    # test Multiplication
    key = c2.generate_keys()

    s1.set_cipher(c2)
    s1.set_key(key)

    r1.set_cipher(c2)
    r1.set_key(key)

    enc_melding = s1.operate_cipher(MESSAGE)
    dec_melding = r1.operate_cipher(enc_melding)

    if Cipher.verify(MESSAGE, dec_melding):
        print("verified melding 2")

    # test Affine
    key = c3.generate_keys()

    s1.set_cipher(c3)
    s1.set_key(key)

    r1.set_cipher(c3)
    r1.set_key(key)

    enc_melding = s1.operate_cipher(MESSAGE)
    dec_melding = r1.operate_cipher(enc_melding)

    if Cipher.verify(MESSAGE, dec_melding):
        print("verified melding 3")

    # test Unbreakable
    key = c4.generate_keys()

    s1.set_cipher(c4)
    s1.set_key(key)

    r1.set_cipher(c4)
    r1.set_key(key)

    enc_melding = s1.operate_cipher(MESSAGE)
    dec_melding = r1.operate_cipher(enc_melding)

    if Cipher.verify(MESSAGE, dec_melding):
        print("verified melding 4")

    # test RSA
    key = c5.generate_keys()

    s1.set_cipher(c5)
    s1.set_key((key[0], key[1]))

    r1.set_cipher(c5)
    r1.set_key((key[0], key[2]))

    enc_melding = s1.operate_cipher(MESSAGE)
    dec_melding = r1.operate_cipher(enc_melding)

    if Cipher.verify(MESSAGE, dec_melding):
        print("verified melding 5")
