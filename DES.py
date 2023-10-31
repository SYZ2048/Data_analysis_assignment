from Crypto.Cipher import DES
import time
from itertools import product
from re import search
from binascii import b2a_uu

key_true = b'\x10\x00\x00\x00\x00\x01\x00\x00'  # 密钥 8位或16位,必须为bytes 00000000 b = b'\x01'
chars = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))  # 0-9 A-Z a-z
broken = False
plaintext = '123'
counter = 0


def pad(text):
    # 如果text不是8的倍数【加密文本text必须为8的倍数！】，补足为8的倍数
    while len(text) % 8 != 0:
        text += ' '
    return text


# key: bytes
def decrypt(key):
    global counter
    global broken
    global encrypted_text
    global plaintext
    # print(counter)
    des_brute = DES.new(key, DES.MODE_ECB)
    if des_brute.decrypt(encrypted_text).decode(errors='ignore').rstrip(' ') == plaintext:
        broken = True
        print(des_brute.decrypt(encrypted_text).decode().rstrip(' '))
        print(plaintext)
        print("Password found: %s" % key)
    counter += 1
    return


def test_passwords(width, position, base_string):
    for char in chars:
        if not broken:
            if position < width:
                test_passwords(width, position + 1, base_string + "%c" % char)
                key = (base_string + "%c" % char).encode().zfill(8)
                decrypt(key)


def bruteforce_des():
    global broken
    for keyGen in product(range(256), repeat=8):
        key = bytearray(
            (keyGen[0], keyGen[1], keyGen[2], keyGen[3], keyGen[4], keyGen[5], keyGen[6], keyGen[7])
        )
        if not broken:
            decrypt(key)
        if counter >= 0x1000000:
            break
        # cipher = DES.new(key, DES.MODE_ECB)
        # plaintext = cipher.decrypt(bytes.fromhex("ce126d2ddf2d1e64"))
        # match = search("[A-Z]{4} [A-Z]{4}", b2a_uu(plaintext).decode())
        # DEBUG
        # print(f"{key.hex()} {b2a_uu(plaintext).decode()}")
        # if match:
        #     with open("plaintext", "w") as file:
        #         file.write(str(key.hex()) + " " + str(match) + "\n")


des = DES.new(key_true, DES.MODE_ECB)  # 创建DES实例
padded_text = pad(plaintext)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密

time_start_2 = time.clock()
# brute force code
# test_passwords(8, 0, '')
# decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00')
bruteforce_des()
time_end_2 = time.clock()

print("Brute force took %.2f s" % (time_end_2 - time_start_2))
print("Tested ", counter, " times")
print("Tested %.2f per second" % (counter / (time_end_2 - time_start_2)))

# decrypt with Crypto
# plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')
# print(plain_text)
