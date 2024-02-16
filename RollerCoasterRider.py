print("Welcome to the roller coaster")

height = int(input("Enter your height in cm: \n"))
if height >= 120:
    bill = 0
    print("You can ride the roller coaster!")
    age = int(input("Enter your age: \n"))
    if age <= 3:
        print("Chotu ke bacche...go and sleep")
    elif age <= 12:
        bill = 5
        print("Child tickets are 5$ ")
    elif age <= 21:
        bill = 10
        print("Youth tickets are 10$ ")
    elif age >= 75:
        print("Do not dare to attempt adventure!! ")
        quit(1)
    else:
        bill = 20
        print("Adult tickets are 20$ ")

    want_photo = input("Do you want to take a picture? Y or N. ").capitalize()
    if want_photo == 'Y':
        bill += 3

    print(f"Your total bill is {bill}")

else:
    print("You need to grow taller before riding...")
