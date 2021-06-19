from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key = b'youareth' # 8 bits password

cipher = DES.new(key, DES.MODE_CBC)

def to_write( enc_res, flag):
    if flag == 'enc':
        with open('encrypted_file', 'wb')as enc_file:
            
            enc_file.write(cipher.iv)
            enc_file.write(enc_res)
    else:
        with open('decrypted_file.txt', 'wb')as dec_file:
            dec_file.write(enc_res)


def encrpytion(filename):
    "function to perform encryption"
    
    flag = 'enc'
    # ciber, algorith and mode
    #cipher = DES.new(key, DES.MODE_CBC)

    with open(filename,"rb") as file:
        message = file.read()
        print(message)

        #create variable for our encrypted text, taking in our predefined cipher and pad
        encrypt_result = cipher.encrypt(pad(message,DES.block_size))
        print(encrypt_result)
        to_write( encrypt_result, flag)
    
    return 'file encrypted'


def decrpytion(filename, key ):

    flag = 'dcy'
    with open(filename, 'rb') as enc_file:
        # to pull out the auto generated initialization vector used to randomize the cipher text
        iv = enc_file.read(8)
        # pull the encrypted text
        encrypt_result = enc_file.read()
        #create variable for our encrypted text, taking in our predefined cipher and initialization vector
        cipher = DES.new(key, DES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(encrypt_result), DES.block_size)
        #decode to get the text in it original format, not bytes
        print("Decoded messafe", plaintext.decode())
        to_write( plaintext, flag)

    return 


# filename = 'encrypted_file'
# # filename = 'file.txt'
# # encrpytion(filename)
# decrpytion(filename,key)


i = input("Please type a number \n 1-encrypt \n 2-decrypt \n")
#print(type(i))

if i == '1':
    filename=input("enter a file name \n")
    encrpytion(filename)
elif i =='2':
    filename=input("enter a file name \n")
    decrpytion(filename,key)

