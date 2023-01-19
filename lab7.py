#prolog
#AUTHOR: Jasnoor Sandhu
#EMAIL: jsandhu2@student.gsu.edu
#SECTION: 032

'''
Purpose: offer the user a choice of food items, calculate total bill

Pre-conditions: user enters 5 or 6 y's or n's depending on desired items (strings)

Post-conditions: prompts for choices, total bill before (float) and after tip, (float)
and parting message.
'''

print("Welcome to Dairy King")
print("Please answer each question with y or n")

bill = 0

gcs = input("Do you want a grilled cheese sandwich? ")
if gcs == "y":
    bill += 7
elif gcs == "n":
    bill += 0

nach = input("Do you want a serving of nachos? ")
if nach == "y":
    bill += 5
elif nach == "n":
    bill += 0

sw = input("Do you want a chicken sandwich? ")
if sw == "y":
    bill += 8
elif sw == "n":
    bill += 0
hb = input("Do you want hamburger? ")
if hb == "y":

    cheese = input("Do you want cheese on that? ")
    if cheese == "y":
        bill += 10
    elif cheese == "n":
        bill += 8
elif hb == "n":
    bill += 0

doggy = input("Do you want a hot dog? ")
if doggy == "y":
    bill += 6
elif doggy == "n":
    bill += 0

bill = float(bill)
print(f"Your total for your food is ${bill:.2f}")

tip = (bill * 1.2)
tip = float(tip)
print(f"The total with 20% tip is ${tip:.2f}")

print("Thank you for your business!")
