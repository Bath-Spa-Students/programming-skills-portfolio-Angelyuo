import math
print("""
AREA OF A CIRCLE CALCULATOR
""")
while True:
    rd = input("Do you want to input RADIUS or DIAMETER? ")
    if rd.upper() == "RADIUS" or "R":
        radius = float(input("Input the RADIUS: "))
        answer = radius ** 2 * math.pi
        print("The area of the circle is:",answer)
        break
    elif rd.upper() == "DIAMETER" or "D":
        diameter = float(input("Input the DIAMETER: "))
        answer = (diameter/2) ** 2 * math.pi
        print("The area of the circle is:",answer)
        break
    else:
        print("False input, try again!")