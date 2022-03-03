# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

if position == "11":
  row1 = ["X","⬜️","⬜️"]
elif position == "12":
  row1 = ["⬜️","X","⬜️"]
elif position == "13":
  row1 = ["⬜️","⬜️","X"]
elif position == "21":
  row2 = ["X","⬜️","⬜️"]
elif position == "22":
  row2 = ["⬜️","X","⬜️"]
elif position == "23":
  row2 = ["⬜️","⬜️","X"]
elif position == "31":
  row3 = ["X","⬜️","⬜️"]
elif position == "32":
  row3 = ["⬜️","X","⬜️"]
else:
  row3 = ["⬜️","⬜️","X"]  



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")