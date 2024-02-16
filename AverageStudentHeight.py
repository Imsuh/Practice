student_heights = [180, 124, 165, 173, 189, 169, 146]
# student_heights = [156, 178, 165, 171, 187]

sum = 0
count = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    count += 1

print("Total sum of heights is :", sum)
print("Average height is :", round((sum / count)))
print("Total number of students are :", count)
