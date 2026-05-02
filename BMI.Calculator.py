'''
Sophie Mangum
IS 303

BMI Calculator
This program calculates a person's BMI using height and weight.

Inputs:
- Name (string)
- Height in inches (float)
- Weight in pounds (float)

Processes:
- Convert height and weight to numbers
- Calculate BMI using formula

Outputs:
- Print name and BMI in a formatted message
'''

name = input("What is your name? ")
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = (weight / (height ** 2)) * 703

print("---")
print(f"{name}, your BMI is {bmi}")