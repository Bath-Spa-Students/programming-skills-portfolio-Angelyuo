print("""
      WEATHER TEMPERATURE INDICATOR
      """) # title of our process
temperature = input("Do you want to use celsius or farenheit or kelvin? ")
if temperature.upper() == "CELSIUS":
 weather = float(input("What's the temperature for today? "))
 if weather >= 37:
  print(f"{weather} degrees celsius is very hot!!!")
 elif weather >= 30:
  print(f"{weather} degrees celsius is pretty hot!!")
 elif weather >= 25:
  print(f"{weather} degrees celsius is hot!")
 elif weather >= 20:
  print(f"{weather} degrees celsius is warm.")
 elif weather < 20:
  print(f"{weather} degrees celsius is cold.")
 else:
  print("Invalid number output, try again!")
elif temperature.upper() == "FARENHEIT":
 weather = float(input("What's the temperature for today? "))
 if weather >= 98.6:
  print(f"{weather} degrees celsius is very hot!!!")
 elif weather >= 86:
  print(f"{weather} degrees celsius is pretty hot!!")
 elif weather >= 77:
  print(f"{weather} degrees celsius is hot!")
 elif weather >= 68:
  print(f"{weather} degrees celsius is warm.")
 elif weather < 68:
  print(f"{weather} degrees celsius is cold.")
 else:
  print("Invalid number output, try again!")
elif temperature.upper() == "KELVIN":
 weather = float(input("What's the temperature for today? "))
 if weather >= 310.15:
  print(f"{weather} degrees celsius is very hot!!!")
 elif weather >= 303.15:
  print(f"{weather} degrees celsius is pretty hot!!")
 elif weather >= 298.15:
  print(f"{weather} degrees celsius is hot!")
 elif weather >= 293.15:
  print(f"{weather} degrees celsius is warm.")
 elif weather < 293.15:
  print(f"{weather} degrees celsius is cold.")
 else:
  print("Invalid number output, try again!")
else:
 print("That's not a recognized form of temperature measurement, try again.")