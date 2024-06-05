from Crypto.Util.number import long_to_bytes, getPrime, bytes_to_long
import random
from flag import FLAG

e = 3

i = 0
correct = 0
while i < 10:
    m = bytes_to_long(random.randbytes(32))
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    c = pow(m, e, n)
    print(f'n = {n}\n')
    print(f'e = {e}\n')
    print(f'c = {c}\n')
    response = input('Enter the plaintext: ')
    if m == int(response):
        correct += 1
        i += 1
    else :
        print('Wrong! Try again.')
        break

if correct == 10:
    print('Congrats! Here is your flag:')
    print(FLAG)