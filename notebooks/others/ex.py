# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad


# key = b'youareth' # 8 bits password

# # ciber, algorith and mode
# cipher = DES.new(key, DES.MODE_CBC)

# #plain text variable that converts all text to byte format 'b, all doc type will be treated the same
# with open("file.txt","rb") as file:
# 	message = file.read()

# #create variable for our encrypted text, taking in our predefined cipher and pad
# encrypt_result = cipher.encrypt(pad(message,DES.block_size))

# print(encrypt_result)

# #write the result to a file (both the ciphertext an initialization vector used to randomize the cipher text)
# with open('encrypted_file', 'wb')as enc_file:
# 	enc_file.write(cipher.iv)
# 	enc_file.write(encrypt_result)

# #################################################

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

#same key used in the encrypt
key = b'youareth'

# load in the encrypted file
with open('encrypted_file', 'rb') as enc_file:

# to pull out the auto generated initialization vector used to randomize the cipher text
	iv = enc_file.read(8)
# pull the encrypted text
	encrypt_result = enc_file.read()

#create variable for our encrypted text, taking in our predefined cipher and initialization vector
cipher = DES.new(key, DES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(encrypt_result), DES.block_size)

#decode to get the text in it original format, not bytes
print(plaintext.decode())

#print out the result
with open('decrypted_file.txt', 'wb')as dec_file:
	dec_file.write(plaintext)