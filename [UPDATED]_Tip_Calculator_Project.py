print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_amt= (round(bill,2)*(tip/100))+bill
each_share=total_amt/people

print(f"Each person should pay: ${each_share}")
