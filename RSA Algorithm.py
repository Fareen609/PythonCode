def gcd(a,b):
    while b!=0:
        a,b = b, a % b
    return a
def mod_inverse(e, phi):
    for d in range(1, phi):
        if(e * d) % phi == 1:
            return d
    return None
def encrypt(num, e, n):
    return (num ** e) % n
def decrypt(cipher,d,n):
    return (cipher ** d) % n
p= 3
q = 11
n = p * q
phi = (p - 1) * ( q - 1)
e = 7
d = mod_inverse(e, phi)
number = int(input("Enter a number to encrypt :"))
ciphertext = encrypt(number, e ,n)
print(f"Enrypted: {ciphertext}")
decryption = decrypt(ciphertext, d, n)
print(f"Decryption: {decryption}")
