print("Welcome to Python Pizza \n")

# size of the pizza , S, M, L
# want pepperoni? 5$
# for small pizza - 2$ & 3$ for medium and large
# want extra cheese? 3$
# TODO  count = print(input("How many pizzas do u want? "))

print("Small pizza price is 15$")
print("Medium pizza price is 20$")
print("Large pizza price is 25$ \n")

size = input("What size pizza do you want? S or M or L \n").capitalize()
total_price = 0

if size == "S":
    total_price += 15
    want_pepperoni = input("Do you want pepperoni? Y or N \n").capitalize()

    if want_pepperoni == 'Y':
        print("Pepperoni for small pizza is 2$")
        print("Pepperoni for medium & large pizza is 3$ \n")
        total_price += 2
        print("current bill value:", total_price, "\n")

    want_extra_cheese = input("Do you want extra cheese, price 1$ ? Y or N \n").capitalize()
    if want_extra_cheese == "Y":
        total_price += 1

elif size == 'M':
    total_price += 20
    want_pepperoni = input("Do you want pepperoni? Y or N \n").capitalize()

    if want_pepperoni == 'Y':
        print("Pepperoni for small pizza is 2$")
        print("Pepperoni for medium & large pizza is 3$ \n")
        total_price += 3
        print("current bill value:", total_price, "\n")

    want_extra_cheese = input("Do you want extra cheese, price 1$ ? Y or N \n").capitalize()
    if want_extra_cheese == "Y":
        total_price += 1

elif size == "L":
    total_price += 25
    want_pepperoni = input("Do you want pepperoni? Y or N \n").capitalize()

    if want_pepperoni == 'Y':
        print("Pepperoni for small pizza is 2$")
        print("Pepperoni for medium & large pizza is 3$ \n")
        total_price += 3
        print("current bill value:", total_price, "\n")

    want_extra_cheese = input("Do you want extra cheese, price 1$ ? Y or N \n").capitalize()
    if want_extra_cheese == "Y":
        total_price += 1

else:
    print("Choose your pizza size accordingly...")

print("Your Total bill is :", total_price)
