import sys
import random
import hashlib

# our seed
x = 1630000000

# increments seed and returns it
def seed():
    global x
    x += 1
    return x

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    while True:
        s = seed()
        random.seed(s, version=2)

        x = random.random()
        flag = hash(x)

        # print flag if we found it
        if 'b9ff3ebf' in flag:
            print('dam{' + flag + '}')
            print('seed was:', s)
            break
    print("Good job <3")

if __name__ == "__main__":
    sys.exit(main())