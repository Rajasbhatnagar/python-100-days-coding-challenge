print("Welcome to the tip calculator!")
bill = float(input("what is the total bill amount?\n₹:"))
tip = int(input("How much tip would you like to give?\n percent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total =("{:.2f}".format(((bill*(tip/100))+bill)/split))
print(f"Each person should pay: ₹{total}")
