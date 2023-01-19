# Prolog
# Author:  Jasnoor Sandhu
# Email:  jsandhu2@student.gsu.edu
# Section: 032
'''
Purpose: 
calculate the change you are due when you buy an item in a store
Pre-conditions (input): 
money given to the cashier(cost of item)
Post-conditions (output): 
change user get back from the cashier(dollars, quarters, dimes, nickels and pennies)
'''
def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()

    #  2.  Input amount of change from user
    cost = float(input("Cost of the article: "))
    amt = float(input("Enter the given amount: "))

    #  3.  Calculate the change
    change = amt - cost
    dollars = int(change)
    decimals = (change - dollars)
    decimals_r = decimals * 100
    num_quaters = decimals_r // 25
    afterquarters = decimals_r % 25
    num_dimes = afterquarters // 10
    afterdimes = afterquarters % 10
    num_nickels = afterdimes // 5
    num_pennies = round(afterdimes % 5)

#  4. Output resulting change and given cost of an item
    print()
    print("Dollars:",dollars,  "Quaters:",int(num_quaters),  "Dimes:",int(num_dimes),  "Nickels:",int(num_nickels),  "Pennies:",int(num_pennies))

main()
# end of program file