def make_shirt(size="Large", message="I love python!"): # Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
    print(f"Printing... {size}-sized shirt with the message '{message}' printed onto it")
make_shirt() # Make a large shirt with the default message.
make_shirt(size="medium") # Make a medium shirt with the default message.
make_shirt(message="Creative Computing is a fun course!") # Make a shirt of any size with a different message.