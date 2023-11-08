print('''
    MOVIE THEATRE  
      ''')

while True:
    age = int(input("Welcome to the Movie Theatre! How old are you? "))
    if age > 12: # If they are over age 12, the ticket is $15.
        print(f"You're {age} years old? Alright! That'll be $15!")
    elif age >= 3: # If they are between 3 and 12, the ticket is $10.
        print(f"You're {age} years old? Alright! That'll be $10!")
    elif age < 3: # If a person is under the age of 3, the ticket is free.
        print(f"You're {age} years old? Alright! That ticket is free!!")

        