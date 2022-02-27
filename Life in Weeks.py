# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = 90 * 365
weeks = 90 * 52
months = 90 * 12 

yourdays = int(age) * 365
yourweeks = int(age) * 52
yourmonths = int(age) * 12 

remainingdays = int(days) - int(yourdays)
remainingweeks = int(weeks) - int(yourweeks)
remainingmonths = int(months) - int(yourmonths)

print(f"You have {remainingdays} days, {remainingweeks} weeks and {remainingmonths} months left.")