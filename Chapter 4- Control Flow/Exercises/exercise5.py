# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

fav_fruits = ["bananas","mangos","watermelons"] # Make a list of your three favorite fruits and call it favorite_fruits.

if "bananas" in fav_fruits:
    print(f"You must really like {fav_fruits[0]}!")
if "mangos" in fav_fruits:
    print(f"You must really like {fav_fruits[1]}!")
if "watermelons" in fav_fruits:
    print(f"You must really like {fav_fruits[2]}!")
# If the fruit is in your list, the if block should print a statement,such as You really like bananas!
if "oranges" not in fav_fruits:
    print(f"You don't seem to have oranges in your list of favourite fruits.")
if "apples" not in fav_fruits:
    print(f"You don't seem to have apples in your list of favourite fruits.")
# Write five if statements. Each should check whether a certain kind of fruit is in your list.
