print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
t = lower_case_name1.count('t')
r = lower_case_name1.count('r')
u = lower_case_name1.count('u')
e = lower_case_name1.count('e')
l = lower_case_name1.count('l')
o = lower_case_name1.count('o')
v = lower_case_name1.count('v')
e = lower_case_name1.count('e')

sum1 = t + r + u + e
sum2 = l + o + v + e

t = lower_case_name2.count('t')
r = lower_case_name2.count('r')
u = lower_case_name2.count('u')
e = lower_case_name2.count('e')
l = lower_case_name2.count('l')
o = lower_case_name2.count('o')
v = lower_case_name2.count('v')
e = lower_case_name2.count('e')

sum3 = t + r + u + e
sum4 = l + o + v + e

sum5 = sum1 + sum3
sum6 = sum2 + sum4

yy = str(sum5) + str(sum6)
zz = int(yy)
if zz < 10 and zz > 90:
  print(f"Your score is {zz}, you go together like coke and mentos.")
elif zz >= 40 and zz <=50:
  print(f"Your score is {zz}, you are alright together.")
else:
  print(f"Your score is {zz}")