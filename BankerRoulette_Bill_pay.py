import random

# names_string = "Angela", 'Suhas', "Sanvi", "Nayana", "Chotu"
# names = names_string.split(", ")

names = ["Angela", 'Suhas', "Sanvi", "Nayana", "Chotu"]
random_person = names[random.randint(0, len(names) - 1)]
print(f"{random_person} has to pay the bill")
