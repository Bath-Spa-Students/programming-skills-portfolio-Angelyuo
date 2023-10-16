vehicles = ["Toyota Innova", "Range Rover"] # Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list

while True:
    question = input("I'm thinking of getting a new SUV. Do I want a normal one or an expensive one? ")
    if question.upper() == "NORMAL":
        print(f"I am going to get a {vehicles[0]}")
        break
    elif question.upper() == "EXPENSIVE":
        print(f"I am going to get a {vehicles[1]}")
        break
    else:
        print("That's not the kind of SUV I'm looking for!")
# to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”