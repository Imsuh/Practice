given_range = int(input("Enter range to find all even numbers within.. \n"))
sum = 0
for x in range(1, given_range + 1):
    if x % 2 == 0:
        sum += x

print(sum)
