'''
Sophie Mangum
IS 303
# final version

Tip Splitter
This program splits a restaurant bill among friends including tip.

Inputs:
- Restaurant name (string)
- Bill amount (float)
- Tip percentage (float)
- Number of people (int)

Processes:
- Convert inputs to numbers
- Calculate total with tip
- Divide total by number of people

Outputs:
- Print formatted bill summary and cost per person
'''

restaurant_name = input("What is the restaurant name? ")
bill_amount = float(input("What is the bill amount? "))
tip_percent = float(input("What is the tip percentage? "))
people = int(input("How many people are splitting the bill? "))

total_with_tip = bill_amount * (1 + tip_percent / 100)
cost_per_person = total_with_tip / people

print("---")
print(f"{restaurant_name} bill: ${bill_amount}")
print(f"Total with tip: ${total_with_tip}")
print(f"Each person pays: ${cost_per_person}")