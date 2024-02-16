# bmi = weight(kg)/ height(m^2)
height = float(input("Enter your height in meters: \n"))
weight = float(input("Enter your weight in kilograms: \n"))

bmi = weight / (height ** 2)

# print("Your BMI is :" + str(round(bmi, 2)))
print(f"Your BMI is :{(round(bmi, 2))}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are slightly over-weight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
