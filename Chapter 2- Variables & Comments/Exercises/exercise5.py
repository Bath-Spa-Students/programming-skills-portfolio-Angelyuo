print("""USB SHOP

USB STICK - £6
USB-C CABLE - £10
USB HUB - £20
Samsung Galaxy Z Fold - £2000

You have: £50
      
""")
# USB Shop selection and our current money
while True:
    selection = input("Do you want to BUY or CALCULATE? ")
    if selection.upper() == "CALCULATE":
        # Calculate route
        calculation = input("Which item do you want to calculate your £50 with? ")

        if calculation.upper() == "USB STICK":
            # USB Stick calculation route
            usbstick_amount = 50//6
            usbstick_totalprice = usbstick_amount * 6
            change = 50 - usbstick_totalprice
            print(f"With £50, you can buy {str(usbstick_amount)} USB Sticks amounting to £{str(usbstick_totalprice)} in total leaving you £"+str(change))
            confirmation = input("Do you want to buy the USB Stick? ")
            if confirmation.upper() == "YES":
                usbstick_buy = float(input("Send the proper amount of money to buy 8 USB Sticks: "))
                if usbstick_buy > 50:
                    print("You only have £50 in your hand!")
                # Over the budget
                elif usbstick_buy >= 48:
                    change2 = usbstick_buy - 48
                    print(f"USB Stick obtained! Now you have £{str(change2)} in change. Happy shopping!")
                    break
                # Correct amount of money
                elif usbstick_buy < 48:
                    print("That's not enough! Input more money!")
                # Not enough money
            elif confirmation.upper() == "NO":
                pass
            else:
                print("Invalid input!! Try again.")
        if calculation.upper() == "USB-C CABLE":
            print("This is not the item we need to buy. Try again!")
            break
        # USB-C Cable calculation route        
        if calculation.upper() == "USB HUB":
            print("This is not the item we need to buy. Try again!")
            break 
        # USB-C Hub calculation route             
        if calculation.upper() == "SAMSUNG GALAXY Z FOLD":
            print("Are you crazy?! Not only is it not what we need but it's way over our budget! Try again!")
            break  
        # Samsung Galaxy Z Fold calculation route
        else:
            print("Invalid Input!!! Try again.")  

    if selection.upper() == "BUY":    
        # Buy route
        buy = input("Which item do you want to buy? ")
        if buy.upper() == "USB STICK":
            amount = int(input("How much do you want to buy? "))
            usbstickprice = 6 * amount
            money = 50 
            if amount > 8:
                print("That is over your budget! Try again!")
            elif amount == 8:
                eight = float(input(f"That will be £{str(usbstickprice)}. Please input the right amount of cash: "))
                if eight > 50:
                    print("You only have £50 in your hand!")
                # Over the budget
                elif eight >= 48:
                    change = eight - usbstickprice
                    print(f"USB Stick obtained! Now you have £{str(change)} in change. Happy shopping!")
                    break
                # Correct amount of money
                elif eight < 48:
                    print("That's not enough! Input more money!")
                # Not enough money
            elif amount < 8:
                print(f"We need 8 USB Sticks! Not {str(amount)}! Try again!")
            else:
                print("Invalid input! Try again!")
                # Buy USB Stick route
        elif buy.upper() == "USB-C CABLE":   
            print("That's not what we need!")
            # Buy USB-C Cable route
        elif buy.upper() == "USB Hub":   
            print("That's not what we need!")    
            # Buy USB Hub route
        elif buy.upper() == "SAMSUNG GALAXY Z FOLD":   
            print("That's not what we need! And it's too expensive!")
            # Buy Samsung Galaxy Z Fold route
        else:
            print("That's not one of the options. Try again!")