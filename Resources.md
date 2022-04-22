# Resources

## Getting Used to Terminal

First, you want to be able to navigate the folders in your computer, here are some basics:

- `cd`
  - means change directory, you put `cd <folder>` and you will enter that folder
  - to go back to the home directory, do `cd .`
  - to go to the parent directory (go out of your current directory) do `cd ..`
- `cat`
  - use this to print the contents of a file `cat <file>`
  - e.g. `cat hello.txt` will print whatever's in `hello.txt`

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

Done with those? Get more familiar by doing these [bandit wargame challenges](https://overthewire.org/wargames/bandit/)

- we access the problems using a command called `ssh`, `ssh <host> -p <port>`