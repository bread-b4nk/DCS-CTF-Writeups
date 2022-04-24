# Solution

Okay let's start by looking at the source code and executable provided. Thank god they also provided the source code.

If there's a `main` function I like to start there, who knows if there are functions that are never run.

```c
int main(){
	setbuf(stdout, NULL);
	user = (cmd *)malloc(sizeof(user));
	while(1){
		printMenu();
		processInput();
		//if(user){
			doProcess(user);
		//}
	}
	return 0;
}
```

A nice and clean main function that calls a few user-written functions.

Let's look at them in order, starting with `printMenu()`

```c
void printMenu(){
 	puts("Welcome to my stream! ^W^");
 	puts("==========================");
 	puts("(S)ubscribe to my channel");
 	puts("(I)nquire about account deletion");
 	puts("(M)ake an Twixer account");
 	puts("(P)ay for premium membership");
	puts("(l)eave a message(with or without logging in)");
	puts("(e)xit");
}
```

This must be the options available to the user, we also notice that there are functions for each option: `s()`, `p()`, `i()`, etc.

The user input is processed and the appropriate function is called in `processInput()`

```c
void processInput(){
  scanf(" %c", &choice);
  choice = toupper(choice);
  switch(choice){
	case 'S':
	if(user){
 		user->whatToDo = (void*)s;
	}else{
		puts("Not logged in!");
	}
	break;
	case 'P':
	user->whatToDo = (void*)p;
	break;
	case 'I':
 	user->whatToDo = (void*)i;
	break;
	case 'M':
 	user->whatToDo = (void*)m;
	puts("===========================");
	puts("Registration: Welcome to Twixer!");
	puts("Enter your username: ");
	user->username = getsline();
	break;
   case 'L':
	leaveMessage();
	break;
	case 'E':
	exit(0);
	default:
	puts("Invalid option!");
	exit(1);
	  break;
  }
}
```

We are dealing with a struct called `cmd`, here's how it's defined. One is a pointer to a function and the other is a pointer to a string.

```c
typedef struct {
	uintptr_t (*whatToDo)();
	char *username;
} cmd;
```

Another very helpful function is `hahaexploitgobrrr`

```c
void hahaexploitgobrrr(){
 	char buf[FLAG_BUFFER];
 	FILE *f = fopen("flag.txt","r");
 	fgets(buf,FLAG_BUFFER,f);
 	fprintf(stdout,"%s\n",buf);
 	fflush(stdout);
}
```

It's never called, but it prints the flag for us, so we want to call this function.

Very helpfully: look at function `s()`

```c
void s(){
 	printf("OOP! Memory leak...%p\n",hahaexploitgobrrr);
 	puts("Thanks for subsribing! I really recommend becoming a premium member!");
}
```

We are provided the address of the function that we want to run!

Given this information, try running the program provided, see how it behaves, see if anything interesting pops up.

Have you played around with it? Something was interesting regarding the option to inquire about account deletion, function `i()`

```c
void i(){
	char response;
  	puts("You're leaving already(Y/N)?");
	scanf(" %c", &response);
	if(toupper(response)=='Y'){
		puts("Bye!");
		free(user);
	}else{
		puts("Ok. Get premium membership please!");
	}
}
```

If we say 'Y', the user variable (which is a `cmd struct`) is freed, BUT we continue running the program, we can keep doing stuff with `user` after it's freed. In fact, recall that in `main()` there's a function called `DoProcess(user)`, let's look at that:

```c
void doProcess(cmd* obj) {
	(*obj->whatToDo)();
}
```

We're passing in the variable `user` (recall that this is a struct called `cmd`), we're executing the variable `whatToDo` within the `cmd` struct.

This means there is a **use after free** vulnerability. We're using a variable that's already been freed.

If there is a malloc call that follows this free, it will use the section of memory that was most recently freed. So any subsequent `malloc` call will use the `user` struct, and then when we go to main, it will execute whatever's written there. If we input the address of the our desired function, we're good!

 Remember that malloc doesn't clear memory allocated, if there's something previously there, malloc behaves the same.

We find a function that mallocs here: 

```c
void leaveMessage(){
	puts("I only read premium member messages but you can ");
	puts("try anyways:");
	char* msg = (char*)malloc(8);
	read(0, msg, 8);
}
```

It's exactly 8 bytes too, the size of an address.

Which means if we

- leak the address of `hahaexploitgobrrr`
- create an account
- delete the account
- call leaveMessage and give the address of `hahaexploitgobrrr`
- do anything that doesn't mess what we've done up.

The program should go to `main` and go to `DoProcess` and jump to the address that we wrote!

We're trying to send an address in hex though, so we'll use the `pwn` python library to do so. `script.py` shows this.