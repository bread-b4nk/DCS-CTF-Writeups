# Solution

Go to the url provided (http://142.93.209.130:8000), I hope it's still up by the time you read this.

By viewing source, there seems to a be a script, and some text that we can't see. I'm talking about

```html
<h3>Sup3r S3cr3t H4ck3r F0rum5</h3>
</div>

<div class='center'>
  <h3>Enter your invite code to continue</h3>
</div>
<div class='center'>
<form action="/invite" method="POST">
  <label for="code">Invite code :</label><br>
  <input type="text" id="code" name="code" placeholder="invite code"><br><br>
  <input type="submit" value="Submit">
</form>
</div>
```
It's obfuscated by the scripts and css styling. So if you delete those in inspect element, you can actually see the form!

Hmmm, ok we need an invite code, I did do an nmap scan to see if any other ports were open

```bash
$ nmap 142.93.209.130
Starting Nmap 7.80 ( https://nmap.org ) at 2022-04-23 13:10 EDT
Nmap scan report for 142.93.209.130
Host is up (0.31s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
19/tcp   filtered chargen
22/tcp   open     ssh
646/tcp  filtered ldp
6389/tcp filtered clariion-evr01
8000/tcp open     http-alt
8001/tcp open     vcom-tunnel
8002/tcp open     teradataordbms
8193/tcp filtered sophos
```
And I tried accessing these ports, only 8000, 8001, and 8002 worked, there was a meme in 8001. These turned out to be other problems. Inputting random invite codes would give you a link to Rick Astley's Never Gonna Give You Up, which was very entertaining.

But let's think this through, we're trying to think of a code for a hacker forum, what would someone setting this up set the code to be? I gave a blind guess and put in `admin`, which just so happened to work. Yay! Giving me the flag: `ictf{w41t_y0u_4r3_1nv1t3d??_29983213}`