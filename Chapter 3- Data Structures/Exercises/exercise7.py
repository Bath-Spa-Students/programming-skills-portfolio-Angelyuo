places = ["Berlin","Paris","Doha","Inazuma"] # Store the locations in a list. Make sure the list is not in alphabetical order.

print("""
      Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
      """) 

print(places)

print("""
      Use sorted() to print your list in alphabetical order without modifying the actual list.
      Show that your list is still in its original order by printing it.
      """) 

sortplaces = sorted(places)
print(sortplaces)
print(places)

print("""
      Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
      Show that your list is still in its original order by printing it again.
      """) 

sortplaces = sorted(places, reverse=True)
print(sortplaces)
print(places)

print("""
      Use reverse() to change the order of your list. Print the list to show that its order has changed.
      """) 

places.reverse()
print(places)

print("""
      Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
      """)

places.reverse()
print(places)

print("""
      Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
      """) 
places.sort()
print(places)

print("""
      Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
      """)
places.reverse()
print(places)