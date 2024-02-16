line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

tMap = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? \n ")
if (len(position) <= 0 and len(position)) > 2:
    print("Enter correct position value")
else:
    letter = position[0].lower()
    abc = ['a', 'b', 'c']
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    tMap[letter_index][number_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")
