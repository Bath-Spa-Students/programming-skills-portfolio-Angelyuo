favnum = 2
# My favourite number

question = input("Do you want to know my favourite number? ")
if question.upper() == "YES":
    print("Great! My favourite number is",str(favnum)+"! :)")
elif question.upper() == "NO":
    print("Wrong answer. Say yes.")
else:
    print("I don't seem to understand. Can you try again?")