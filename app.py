#The inputes and assigning values to variables
name = input("What is the user's name? ")
age = int(input("What is the user's age? "))
country = input("What is the user's county of birth? ")
knowing = input("What is the user known for? ")

# Assigning variables to keys in dictionaries
user = {"name": name, "age": age, "country": country, "knowing for": knowing}

# Output keys and values
for k, v in user.items():
    print(f"{k}:{v}")
