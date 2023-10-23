print("""
      Welcome to the stage of life!
      """)

age = int(input("How old are you? "))
if age >= 65: # If the person is age 65 or older, print a message that the person is an elder.
    print(f"At the age of {age}, you are an elder!") 
elif age >= 20: # •If the person is at least 20 years old but less than 65, print a message that the person is an adult.
    print(f"At the age of {age}, you are an adult!") 
elif age >= 13: # If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
    print(f"At the age of {age}, you are a teenager!") 
elif age >= 4:  # If the person is at least 4 years old but less than 13, print a message that the person is a kid.
    print(f"At the age of {age}, you are a kid!") 
elif age >= 2:  # If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
    print(f"At the age of {age}, you are a toddler!") 
elif age < 2:   # If the person is less than 2 years old, print a message that the person is a baby.
    print(f"At the age of {age}, you are a baby!") 
else:
    print("I don't think this is a valid age number...")