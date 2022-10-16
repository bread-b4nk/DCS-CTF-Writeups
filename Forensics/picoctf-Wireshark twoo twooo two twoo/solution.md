# Solution

Okay! Download the pcap of the problem. 

Just by scrolling or word-searching 'flag' we see that there are a lot of HTTP `GET /flag HTTP/1.1`, each of which get a different flag returned e.g. 

- `picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}`  at packet 744
- `picoCTF{bda69bdf8f570a9aaab0e4108a0fa5f64cb26ba7d2269bb63f68af5d98b98245}` at packet 1550
- and many more

What we found is probably not the case then. Let's keep looking.

There are some standard queries to `redshrimpandherring.com`, at first I thought this could just be a red herring but there was something off about some of these DNS queries. Look at the url being searched:

`cGljb0NU.reddshrimpandherring.com`

What's up with the sub-domain `cGljb0NU`? If we keep looking at other DNS queries for `redshrimpandherring.com` we find

- `RntkbnNf.reddshrimpandherring.com`
- `M3hmMWxf.reddshrimpandherring.com`

- `ZnR3X2Rl.reddshrimpandherring.com`
- `YWRiZWVm.reddshrimpandherring.com`
- `fQ==.reddshrimpandherring.com`

The `fQ==` is what gave it away for me, this is base64 encoding! Recall that we can often identify something encoded with base64 by the last two characters being `==` (not always). `fQ==` is way too short to be something substantial encoded in base64 on its own... we can try combining the previous sub-domains too.

This gives us `cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==`, base64 decoding this gives us the flag:

**picoCTF{dns_3xf1l_ftw_deadbeef}**