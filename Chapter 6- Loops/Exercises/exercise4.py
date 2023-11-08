sandwhich_orders = ['Cheese Sandwhich', 'BLT Sandwhich', 'Ham Sandwhich'] 
# Make a list called sandwich_orders and fill it with the names of various sandwiches.
finished_sandwhiches = []
# Then make an empty list called finished_sandwiches.

while sandwhich_orders: # Loop through the list of sandwich orders and print a message for each order.
    print(f"Your {sandwhich_orders[0]} is ready!")
    finished_sandwhiches.append(sandwhich_orders[0])
    sandwhich_orders.pop(0)
print('''
List of finished sandwhiches:''')
for sandwhiches in finished_sandwhiches:
    print(sandwhiches) # Print a message listing each sandwich that was made.