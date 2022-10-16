# Grandmaster

**Author**: S|{oto

**CTF**: Deadface CTF 2022

**Description**:

*DEADFACE has written another challenge to test the skills of new recruits. White to move. (Please use Short Algebraic Notation)*

grandmaster.deadface.io:5000

*The flag will be in the format flag{.\*}.*

**Hints**: n/a


When we connect to the server using `nc grandmaster.deadface.io 5000`, we're immediately presented with:
```
Which move forces mate in 2?

. . . . . . . .
. . . . . . . .
. . R . . . . .
. . . . k . . .
. . . . . . P .
. . P . . K . .
. . . . P . . .
. . . . . B . .
```

Only moments later, the server adds:
```
Too slow! Git Good.
```

If we answer with a random move (since we don't have the time to determine the correct answer) we're met with:
```
Access Denied.
Connection Closed.
```

By connecting repeatedly, we can confirm that the board changes - without pattern - each time. Since we don't have nearly enough time to find the answer manually, we'll have to do so programmatically, using a chess engine.  To do this, I wrote the python script [grandmaster.py](grandmaster.py), which uses the library `python-chess` and the chess engine Stockfish to automatically find the next move.  The script also automatically handles interactions with the server.

Using the script, we can respond to the prompt in time.  This yields the flag: `flag{ch3ss-M@st3r-w0W-v3ry-g00d}`.
