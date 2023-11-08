print('''
    PIZZA TOPPING SIMULATOR  
      ''')
while True:
    start = input("Shall we begin? ")
    if start.upper() == "YES":
        print('''
        TOPPINGS
  Pepperoni  Pineapple    
      ''')
        topping = input("Which one do you want to add onto your pizza? ")
        if topping.upper() == "PEPPERONI": 
            confirm = input("Pepperoni added! Do you want to add Pineapple too or QUIT? ")
            if confirm.upper() == "QUIT":
                print("Your order of Pepperoni Pizza is ready! Thank you for using our service!")
                break
            elif confirm.upper() == "YES":
                print("Pineapple added! Thank you for using our service!")
                break
        elif topping.upper() == "PINEAPPLE": 
            confirm = input("Pineapple added! Do you want to add Pepperoni too or QUIT? ")
            if confirm.upper() == "QUIT":
                print("Your order of Pineapple Pizza is ready! Thank you for using our service!")
                break
            elif confirm.upper() == "YES":
                print("Pepperoni added! Thank you for using our service!")
                break
        else:
            print("That's not a topping in our menu, try again!")
    elif start.upper() == "NO":
        print("Oh... ok.")
        break







              

    