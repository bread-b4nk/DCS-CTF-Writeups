#!/usr/bin/env python3
import sys
import time
import random
import hashlib

# returns a seed, based on the current time
def seed():
    return round(time.time())

# hash function
def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    while True:
        # gets a random seed
        s = seed()
        random.seed(s, version=2)

        # generates random number based on seed and hashes it
        x = random.random()
        flag = hash(x)

        # gives the flag if string is in hash
        if 'b9ff3ebf' in flag:
            with open("./flag", "w") as f:
                f.write(f"dam{{{flag}}}")
            f.close()
            break

        print(f"Incorrect: {x}")
    print("Good job <3")

if __name__ == "__main__":
   sys.exit(main())
