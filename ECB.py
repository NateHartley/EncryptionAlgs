from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from keyGen import key_gen
# cant import key_gen from main because we are also importing this file in main, just need to put keygen in another file

def ecb_encrypt():
    user_input = input("Ciphertext ouput in base64 [1] or hexadecimal [2]? \n")
    plainText = input("Input message: \n")

    key=bytes.fromhex("00112233445566778899aabbccddeeff")
    ### implement key_gen alg here from keyGen ###

    # Encryption #
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    cipherText = b64encode(cipher.encrypt(pad(plainText.encode('utf-8'), AES.block_size))).decode("utf-8") # Format is hex

    if user_input == '1':
        print("Ciphertext (in base64) --> ", cipherText) # e.g. hello = nYbIYS4IXpOiNXlKcIr3qQ==
    elif user_input == '2':
        print("Ciphertext (in hex) --> ", b64decode(cipherText).hex()) # e.g. hello = 9d86c8612e085e93a235794a708af7a9



def ecb_decrypt():
    user_input = input("Input ciphertext as base64 [1] or in hexadecimal [2]? \n")
    key=bytes.fromhex("00112233445566778899aabbccddeeff")

    if user_input == '1':
        cipherText = input("Input ciphertext: \n") # e.g. nYbIYS4IXpOiNXlKcIr3qQ== = hello
    elif user_input == '2':
        cipherText = input("Input ciphertext: \n") # e.g. 9d86c8612e085e93a235794a708af7a9 = hello
        cipherText = b64encode(bytes.fromhex(cipherText)).decode() # Turns hex into base64
    else:
        print("This is not an option")

    # Decryption #
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    decodedText = unpad(cipher.decrypt(b64decode(cipherText)), AES.block_size).decode("utf-8")

    print("Message --> ", decodedText)