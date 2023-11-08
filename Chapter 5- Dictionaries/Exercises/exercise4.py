river = {
'Nile':'Egypt',
'Amazon':'Brazil',
'Yangtze':'China'
}
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
for key, value in river.items():
    rivername = str(value)
    print(f"The {key} flows in {rivername}!") 
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for value in river:
    print(value)
# Use a loop to print the name of each river included in the dictionary.
for key in river.values():
    print(key)
# Use a loop to print the name of each country included in the dictionary.