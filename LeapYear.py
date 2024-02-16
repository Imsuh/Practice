givenYear = int(input("Enter the year to check leap year or not: \n"))

# year % 4
if givenYear % 4 == 0:
    if givenYear % 100 == 0:
        if givenYear % 400 == 0:
            print(f"year {givenYear} is leap")
        else:
            print("Not a leap year")
    else:
        print(f"year {givenYear} is leap")
else:
    print(f"year {givenYear} is not leap")
