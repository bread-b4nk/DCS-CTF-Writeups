# Mysterious Broadcast

**Author**: S|{oto

**CTF**:  Space Heroes CTF

**Description**: 

*There used to be 8 Models of humanoid cylon but now there are only 7. We've located one of their broadcast nodes but we can't decode it. Are you able to decipher their technologies?*

*http://173.230.134.127*

*Author: blakato*

**Hints**: n/a

When we navigate to the challenge website, we're presented with an blank website, apart from a single `~`.  Additionally, we see that the URL changed from http://173.230.134.127 to http://173.230.134.127/seq/some_char_sequence.  Each time we return to http://173.230.134.127, the seqence of characters after /seq/ is different.

If we try reloading the website, the tilde is replaced by a 1.  Subsequent reloads change the number to a 1 again, then a 0, and so on in a very long sequence of 1's and 0's.  Notably, each time you return to http://173.230.134.127 and get a new char sequence, the sequence restarts, and the sequence always remains the same.

Thus, it seems like this is a binary sequence being shown to the user one bit at a time.  To collect the binary sequence into a single string, I restarted the sequence by going to http://173.230.134.127 once again, and then I fed the generated URL into the following script.

```python
import urllib.request

link = "http://173.230.134.127/seq/3fbd1f9e-bc3e-45b2-bd1a-7963e62ffe11"
string = ""

# Reload the page 1000 times; since the length of the message is unknown,
# this excessive length should ensure that the whole message is captured.
for i in range(1000):
    # Get the HTML of each page (the bit) and append it to the string
    bit = urllib.request.urlopen(link).read().decode("utf8")
    string += bit

print(string)
```

This script outputs the following string:

```
1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110110001100001010101011001110100101101000110001011011011010010110100011000111101101101001001110011000011110011101111010111101~1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110110001100001010101011001110100101101000110001011011011010010110100011000111101101101001001110011000011110011101111010111101~1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110110001100001010101011001110100101101000110001011011011010010110100011000111101101101001001110011000011110011101111010111101~1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110
```

As we can see, this string is just multiple repetititions of the substring `~1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110110001100001010101011001110100101101000110001011011011010010110100011000111101101101001001110011000011110011101111010111101`.

We can assume that this repeated substring is the intended message.  Attempting to convert the bytes directly to ASCII fails to output meaningful characters.  However, if we consult the description of the problem, it implies that "7" should be used instead of "8" at some stage of problem.  Therefore, let's try separating this binary string into 7-bit segments, instead of normal 8-bit bytes.  Since we will want to feed the 7-bit segments into a binary-to-ascii converter, let's prepend a 0 to each segment, making each a full byte long.  We could do this by hand, or with the following simple script:

```
digits = "1100011011001011010001101010110010010001111011010011011110100011011000100111011010101100001101011111011001001010110001101100001000101011001110100011101101110110001100001010101011001110100101101000110001011011011010010110100011000111101101101001001110011000011110011101111010111101"
outputStr = ""
for i in range(len(digits)):
    # Copy each digit into the output string
    outputStr += digits[i]

    # After every seventh character, add a space
    if (i + 1) % 7 == 0:
        outputStr += " "

# Add a 0 before each 7-bit sequence, so that it can be translated by standard binary-to-ascii converters
outputStr = "0" + outputStr
outputStr.replace(" ", " 0")

print(outputStr)

```

This script outputs  `01100011 00110010 01101000 01101010 01100100 01000111 01011010 00110111 01010001 01011000 01001110 01101010 01100001 01010111 01101100 01001010 01100011 00110000 01000101 00110011 01010001 01101101 01101100 00110000 01010101 00110011 01010010 01101000 01100010 01101101 01010010 01101000 01100011 01101101 01010010 00111001 01000011 01100111 00111101 00111101`.  

If we feed these new bytes into a binary-to-ASCII converter, we get `c2hjdGZ7QXNjaWlJc0E3Qml0U3RhbmRhcmR9Cg==`, which looks like Base64.  A final conversion from Base64 to text gives us the flag: `shctf{AsciiIsA7BitStandard}`.

