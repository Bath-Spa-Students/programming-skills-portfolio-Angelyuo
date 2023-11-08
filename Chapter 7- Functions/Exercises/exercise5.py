def describe_city(place, country="Fontaine"): # Give the parameter for the country a default value.
    print(f"The {place} is at {country}!")
describe_city("Fountain of Lucile")
# Call your function for three different cities, at least one of which is not in the default country.
describe_city("Devantaka Mountain", "Sumeru")
describe_city("Wangshu Inn", "Liyue")
describe_city("Falcon Coast", "Mondstatd")