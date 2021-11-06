import binascii

# read in the text file and store strings in list
flags = []
file = open('flags.txt', 'r')
for line in file:
    flags.append(line.strip('\n'))

# xor every string with all possible characters
for line in flags:
    hexString = line.rstrip()
    nums = binascii.unhexlify(hexString)
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))

    # print the flag
    for str in strings:
        if str[0:4] == 'dam{':
            print(str)