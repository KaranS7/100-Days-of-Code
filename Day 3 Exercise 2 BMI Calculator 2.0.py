weight = input("Your weight in kg is: ")
height = input("Your height in meters is: ")
bmi = round(float(weight) / (float(height) ** 2), 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly over weight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically overweight")