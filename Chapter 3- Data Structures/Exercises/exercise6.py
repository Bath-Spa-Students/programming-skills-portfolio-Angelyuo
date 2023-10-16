family = ["Lola","Lolo","Mama","Papa"]
    
for family in family:
    print(f"Hello {family}! I invite you to come to dinner! See you there :)")

family = ["Lola","Lolo","Mama","Papa"]
print(f"It seems that {family[0]} is not able to come, how unfortunate. Guess I will invite another person.")

family[0] = "Angelo"
for family in family:
    print(f"Hello {family}! I invite you to come to dinner! See you there :)")

# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
print("""
DISCLAIMER! You can only invite 2 people!
      """) # Add a new line that prints a message saying that you can invite only two people for dinner.
print("Oh, okay.")

family = ["Lola","Lolo","Mama","Papa"]
family[0] = "Angelo"
print(f"Sorry {family[0]} you can't come to dinner")
family.pop(0)
print(f"Sorry {family[0]} you can't come to dinner")
family.pop(0)
# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

print(f"{family[0]} you are still invited to dinner!")
print(f"{family[1]} you are still invited to dinner!")
# Print a message to each of the two people still on your list, letting them know they’re still invited.

del family[0]
del family[0]
print(family)
