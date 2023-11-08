cat = {
'Breed':'Siamese',
'Owner':'Brigitte Lindholm',
}
dog = {
'Breed':'Golden Retriever',
'Owner':'Mark Fischbach',
}
bird = {
'Breed':'Conure',
'Owner':'Jaiden Dittfach',
}
# Make several dictionaries. In each dictionary, include the kind of animal and the owner’s name.
pets = [cat, dog, bird]
# Store these dictionaries in a list called pets.
for pet in pets:
    print("PET INFO")
    print(f"Animal Breed: {pet['Breed']}")
    print(f"Owner's name: {pet['Owner']}")
    print() # separation