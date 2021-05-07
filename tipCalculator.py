# This tip calculator will calculate tip and divide them into friends or colleague.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15, or 20?"))
split = int(input("how many people to split the bill?"))

tip_percentage = (tip / 100)
result = (bill * (1 + tip_percentage))
people = "{:.2f}".format(result / split)

print(f"Each person should pay: {people} ")
