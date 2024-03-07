def decode_vigenere(ciphertext, key):
  # Convert the ciphertext and key to lists of characters
  ciphertext = list(ciphertext)
  key = list(key)

  key_length = len(key)

  # Create a list to store the decrypted message
  plaintext = []

  # Iterate through the ciphertext and decrypt each character
  for i, c in enumerate(ciphertext):
    key_index = i % key_length
    plaintext.append(chr((ord(c) - ord(key[key_index]) + 26) % 26 + ord('A')))

  return ''.join(plaintext)

ciphertext = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
key = "MATHEMATICS"
print(decode_vigenere(ciphertext, key))