# Resources

## Terminal/Command Line

### Basics - Getting Used to Terminal

First, you want to be able to navigate the folders in your computer, here are some basics:

- `cd`
  - means change directory, you put `cd <folder>` and you will enter that folder
  - to go back to the home directory, do `cd .`
  - to go to the parent directory (go out of your current directory) do `cd ..`
- `ls`
  - means list directory, call `ls` and it'll print whatever's in the current directory
- `cat`
  - use this to print the contents of a file `cat <file>`
  - e.g. `cat hello.txt` will print whatever's in `hello.txt`
- `rm`
  - use this to remove a file `rm <file>`
  - you can delete everything in a directory (including the directory) by adding a *recursive switch*, `rm -r <directory>`

Here are a few terminal commands and corresponding [picoctf](https://picoctf.org/) problem names that'll help you get used to them.

- netcat - `nc <ip> <port>`
  - `what's a netcat?`
  - `Nice netcat...`
  - `glitchy cat`
- strings - `strings <file>`
  - `strings it`
  - `enhance!`
- grep - `grep <patterns> <file>` or `cat <file> | grep <pattern>`
  - `First Grep`
  - `plumbing`

The webshell on picoctf is a very convenient tool for those on windows.

Done with those? Get more familiar by doing these [bandit wargame challenges](https://overthewire.org/wargames/bandit/)

- we access the problems using a command called `ssh`, `ssh <host> -p <port>`

### More Useful Commands

- `man <command>` - probably the most important of all commands, use it to read the manual about any command, this is your goto if you want to know how a command works.
- `more` - fills screen with text from file, press spacebar for mroe
- `less - fills screen with text from file, press spacebar for less
- `nano` - text editor
- `file` - reveals file type
- `diff` - finds difference between 2 files
- `xxd` - produces hex dump
- `cmp` - compares two given files
- `fdisk` - manipulate a disk partition table
- `history` - gives the history of the commands used in that shell
- `ps` - prints current processes
- `iftop` - displays bandwidth usage on an interface

### Globbing Files

There are special characters when using shell commands, * (called a wildcard) matches 0 or more characters, ? matches 1 character, and [] matches one character from the set or range of characters listed within the brackets. Confusing? The examples will clarify it for you.

Let's say we have a directory storing this stuff:

```bash
$ ls
    game    game.o    README     test2.txt  test4.txt  test6.txt  test8.txt
    game.c  Makefile  test1.txt  test3.txt  test5.txt  test7.txt  test9.txt
```

We're going to "glob" files together using the special characters, you can apply this later when you want to view files in a directory that fit certain requirements.

```bash
$ ls game*
    game  game.c  game.o
$ ls game.*
    game.c  game.o
$ ls test*txt
    test1.txt  test3.txt  test5.txt  test7.txt  test9.txt
    test2.txt  test4.txt  test6.txt  test8.txt
$ ls test?.txt
    test1.txt  test3.txt  test5.txt  test7.txt  test9.txt
    test2.txt  test4.txt  test6.txt  test8.txt
$ ls test[2468].*
    test2.txt  test4.txt  test6.txt  test8.txt
$ ls test[7-9].*
    test7.txt  test8.txt  test9.txt
$ ls *.*
    game.c  test1.txt  test3.txt  test5.txt  test7.txt  test9.txt
    game.o  test2.txt  test4.txt  test6.txt  test8.txt
$ echo [a-z]*    
    game game.c game.o test1.txt test2.txt test3.txt test4.txt test5.txt test6.txt test7.txt test8.txt test9.txt
$ echo [A-Z]*
    Makefile README
```

