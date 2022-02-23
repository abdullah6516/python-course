light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("Proceed with caution")
print("This code executes no matter what")

age = 0
if age < 18:
    beverage = "kid"
elif age >= 18 and age < 60:
    beverage = "Young"
else:
    beverage = "Old"
print("You are  " + beverage)