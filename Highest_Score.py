marks = [78, 65, 89, 86, 55, 91, 64, 89]
high = marks[0]
for n in range(0, len(marks)):
    if marks[n] > high:
        high = marks[n]

print(high)
