from pwn import *
from gmpy2 import iroot

r = remote('0.0.0.0', 3003)

i = 0
while i < 10:
    r.recvuntil(b'n = ')
    n = int(r.recvline().strip())
    r.recvuntil(b'e = ')
    e = int(r.recvline().strip())
    r.recvuntil(b'c = ')
    c = int(r.recvline().strip())
    m = iroot(c, e)[0]
    r.sendline(b'%d' % m)
    i += 1
    print(i)
r.interactive() 