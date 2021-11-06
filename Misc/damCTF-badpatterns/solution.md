# bad-patterns

**Solution**: 

We compare the original text and the encoded text and see that they are the same length.  This tells us that each character in the original text is probably getting mapped to some character in the encoded text.  

Comparing these texts letter by letter, we see that the first word in the original text, `Lorem`, gets mapped to `Lpthq` in the encoded text.  Comparing these letter by letter, we see the following correspondence:
```
L -> L
o -> p
r -> t
e -> h
m -> q
```
We notice that `L` is mapped to itself, and `o` is mapped to `p`, which is the letter after it in the alphabet.  For the next characters, we see that `t` is 2 letters after `r` in the alphabet, `h` is 3 letters after `e` and `q` is 4 letters after `m` in the alphabet.  At this point, we already have an idea about how this encoding works, but just to confirm, we write a quick Python program to compare all the characters and tell us how far apart they are from each other in the alphabet.  Here's what the first bit of this output looks like.
``` 
L -> L 0 
o -> p 1
r -> t 2
e -> h 3
m -> q 4
  ->   0
i -> j 1
p -> r 2
s -> v 3
u -> y 4
m -> m 0
  -> ! 1
d -> f 2
o -> r 3
l -> p 4
```

We see that there's a repeating sequence from 0 - 4 mapping each letter in the original text to a letter a certain amount after it in the alphabet.  Now that we know how to get from the original text to the encoded text, we can replicate this for the flag.

I wrote some more python to help me encode the flag, `bagelarenotwholewheatsometimes`.  

Note that this encoding is the same as a Vigenere cipher with a key of `abcde`, and this last part could also have been solved by doing a [Vigenere cipher](https://cryptii.com/pipes/vigenere-cipher) with plaintext `bagelarenotwholewheatsometimes` and a key of `abcde`.