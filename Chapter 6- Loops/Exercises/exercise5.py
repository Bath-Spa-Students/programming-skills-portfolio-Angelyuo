sandwhich_orders = ['Cheese Sandwhich', 'Pastrami Sandwhich', 'BLT Sandwhich', 'Pastrami Sandwhich', 'Ham Sandwhich', 'Pastrami Sandwhich']
finished_sandwhiches = []
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
print('''The deli has ran out of Pastramis!
      ''') # Spacing
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami.
while 'Pastrami Sandwhich' in sandwhich_orders:
    remove_pastrami = sandwhich_orders.index('Pastrami Sandwhich')
    sandwhich_orders.pop(remove_pastrami)
# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
while sandwhich_orders: 
    print(f"Your {sandwhich_orders[0]} is ready!")
    finished_sandwhiches.append(sandwhich_orders[0])
    sandwhich_orders.pop(0)
print('''
List of finished sandwhiches:''')
for sandwhiches in finished_sandwhiches:
    print(sandwhiches) # Make sure no pastrami sandwiches end up in finished_sandwiches.