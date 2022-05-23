#tip calculator
print("Welcome to tip calculator")
bill=float(input("what was the total bill ?: $"))
tip=int(input("What porcentage tip would you like to give? 10, 12 or 15?: "))
people_for_bill=int(input("how many people to split the bill ?: "))
total_bill=bill+(bill*(tip/100))
bill_for_each=round(total_bill/people_for_bill,2)
print(f"Each person should pay ${bill_for_each}")
