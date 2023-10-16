family = ["Lola","Lolo","Mama","Papa"]
    
for family in family:
    print(f"Hello {family}! I invite you to come to dinner! See you there :)")

"""You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite."""

family = ["Lola","Lolo","Mama","Papa"]
print(f"It seems that {family[0]} is not able to come, how unfortunate. Guess I will invite another person.") 
# Add a print() call at the end of your program stating the name of the guest who can’t make it.


family[0] = "Angelo" 
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
for family in family:
    print(f"Hello {family}! I invite you to come to dinner! See you there :)")
# Print a second set of invitation messages, one for each person who is still in your list.