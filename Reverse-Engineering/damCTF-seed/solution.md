# seed

**Solution**: 

We see that in the code, we are getting a seed from the current time and then using that to seed Python's `random` function before generating a random number.

From there, the code hashes the random number, and if that hash contains a specific string, prints it out as the flag.

We know that when we give Python's random number generator the same seed, it will always produce the same random number.  This means that in order to get the flag, we just need to find the correct seed!  

The code runs `round(time.time())` to generate the seed.  Some googling tells us that `time.time()` returns a number of seconds from some arbitrary date and calling `round(time.time())` gives us `1636233235`.  

We set a global variable to `1630000000` (picked somewhat arbitrarily as a number that's less than the current time) and modify the `seed()` method so that instead of returning the current time, it increments our global variable and returns that.  Hopefully we will encounter the correct seed that turns into the correct flag when hashed.  Running this for a bit gives us our flag, using a seed of `1634187287`.