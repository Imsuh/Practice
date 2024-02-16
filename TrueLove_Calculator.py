print("Welcome to ❤️Love~calculator❤️ \n")
my_name = input("Enter your name: \n")
partner_name = input("Enter your partner name: \n")
combined_names = my_name + partner_name
name_lower = combined_names.lower()
t = name_lower.count('t')
r = name_lower.count('r')
u = name_lower.count('u')
e = name_lower.count('e')
l = name_lower.count('l')
o = name_lower.count('o')
v = name_lower.count('v')
e = name_lower.count('e')

score = t + r + u + e + l + o + v + e
# if 10 < score >= 90:
if score < 10 or score > 90:
    print("Your score is :", score, " you both get along like mentos and coke")
