def key_gen():
    print("Key must be either plaintext at 32 max characters, or hexidecimal at 16 max bytes \n")
    user_input = input("Input a plaintext key [1] or a hexidecimal key [2]? \n")

    if user_input == '1':
        key = input("Input plaintext key: \n")

        key = ''.join(format(ord(i), '08b') for i in key) # convert to binary
        key = hex(int(key, 2))[2:] # convert to hex, remove 0x from start

        missing_bytes = str(int((32 - len(key))/2))
        if float(missing_bytes) < 10:
            pad_byte = '0'+ missing_bytes
        else:
            pad_byte = missing_bytes

        i = 0
        while i < float(pad_byte):
            key = key + pad_byte
            i = i + 1
        
        print("Key (hex) -> ", key)
        
    elif user_input == '2':
        key = input("Input hexadecimal key: \n")
        hexString = '0123456789abcdefABCDEF'
        check = all(c in hexString for c in key)
        if len(key) > 32 or check == False:
            print("Invalid hex, either above 16 bytes or contains invalid characters")

    else:
        "This is not an option"
    
    return key