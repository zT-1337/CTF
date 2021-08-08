from pwn import *
import warnings
warnings.filterwarnings("ignore")

def main():
  rem = remote("mercury.picoctf.net", 41934)

  encrypted_flag = get_encrypted_flag(rem)
  bytes_of_encrypted_flag = get_bytes_of_binary_hex_string(encrypted_flag) 

  #move current key_location back to the start of the key file
  length_of_flag = len(encrypted_flag) // 2
  remaining_key_length = 50000 - length_of_flag #length of otp is 50000
  send_string_for_encryption(rem, "A" * remaining_key_length)
  
  #start known plain text attack on one time pad
  plain_text = "A" * length_of_flag
  bytes_of_plain_text = bytearray(plain_text, "ascii")
  encrypted_known_plain_text = send_string_for_encryption(rem, plain_text)
  bytes_of_encrypted_known_plain_text = get_bytes_of_binary_hex_string(encrypted_known_plain_text)

  #Calculate Key from plain text and encrypted plain text
  bytes_of_key = xorBytearrays(bytes_of_plain_text, bytes_of_encrypted_known_plain_text) 

  #Decrypt flag with key
  decrypted_flag = xorBytearrays(bytes_of_encrypted_flag, bytes_of_key)
  print(decrypted_flag)

def get_encrypted_flag(rem):
  rem.recvuntil("This is the encrypted flag!\n")
  return rem.recvline(keepends=False) 

def get_bytes_of_binary_hex_string(binary_hex_string):
  return bytearray.fromhex(binary_hex_string.decode())

def send_string_for_encryption(rem, val):
  rem.recvuntil("What data would you like to encrypt?")
  rem.sendline(val)
  rem.recvuntil("Here ya go!\n")
  return rem.recvline(keepends=False)

def xorBytearrays(aBytes, bBytes):
  return bytearray(list(map(lambda aByte, bByte: aByte ^ bByte, aBytes, bBytes)))


if __name__ == "__main__":
  main()