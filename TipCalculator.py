print("Welcome to tip calculator...")
total_bill = float(input("What was the bill? \n"))
total_people = int(input("How many people should split the bill? \n"))
tip_percentage = float(input("What percent of tip you would like to give, 10,20,30? \n"))

total_bill += (total_bill * tip_percentage / 100)
average_per_person = total_bill / total_people

print("Each person should pay - " + str(round(average_per_person, 2)))
