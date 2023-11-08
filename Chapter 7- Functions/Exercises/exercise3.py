def make_shirt(size, message): # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    print(f"Printing... {size}-sized shirt with the message '{message}' printed onto it") # The function should print a sentence summarizing the size of the shirt and the message printed on it.
make_shirt("Small", "Welcome!") # Call the function once using positional arguments to make a shirt.
make_shirt(size="Large", message="Goodbye!") # Call the function a second time using keyword arguments.