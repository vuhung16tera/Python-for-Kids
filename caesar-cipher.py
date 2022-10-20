def caesar_encrypt(plainText, key):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + key
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print("Encrypted text is: ", cipherText)
  return cipherText

def caesar_decrypt(plainText, key):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) - key
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print("Decrypted text is: ", cipherText)
  return cipherText

my_secret_msg = "vuhung"
my_private_key = 2
encrypted_to_send = caesar_encrypt(my_secret_msg, my_private_key)
caesar_decrypt(encrypted_to_send, my_private_key)

