from math import gcd

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    d = 0
    for i in range(1, 10):
        x = 1 + i * phi
        if x % e == 0:
            d = int(x / e)
            break

    return (e, n), (d, n)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = ' '.join([str((ord(char) ** key) % n) for char in plaintext])
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = ''.join([chr((int(char) ** key) % n) for char in ciphertext.split()])
    return plain


#in order to decrypt the encrypted message you should enter it with separating integers with space
p = 61
q = 53
public, private = generate_keypair(p, q)
print("Public key: ", public)
print("Private key: ", private)
message = input("Enter a message to encrypt: ")
encrypted_msg = encrypt(private, message)
print("Encrypted message: ")
print(encrypted_msg)
print("Decrypted message: ")
print(decrypt(public, encrypted_msg))

