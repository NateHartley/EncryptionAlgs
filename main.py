from ECB import ecb_encrypt, ecb_decrypt
from keyGen import key_gen

def main():
    encrypt_mode = input("Choose an encyption mode {ECB, ...}: \n")
    enc_dec = input("Encrypt [1] or Decrypt [2]? \n")
    key_gen()
    
    if encrypt_mode == "ECB" or encrypt_mode == "ecb":
        if enc_dec == '1':
            ecb_encrypt()
        elif enc_dec == '2':
            ecb_decrypt()
        else:
            print("This is not an option")
    else:
        print("That is not an encryption mode")

if __name__ == "__main__":
    main()