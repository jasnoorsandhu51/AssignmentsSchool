# Author: Jasnoor Sandhu
# Email: jsandhu2@studentgsu.edu
# Section: 032
'''
Purpose:
convert meters to inches, using fact that there are 39.37
inches in 1 meter
Pre-conditions (input):
number of meters (floating point)
Post-conditions (output):
number of inches, floating point with 2 decimals rounded
'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print("Conversion of meters to inches")
    # 2. Input amount of meters from user
    meters = float(input("How many meters? "))
    # 3. Calculate number of inches
    # 39.37 inches in one-meter
    inches = meters * 39.37
    # 4. Output resulting inches and given number of meters
    print(meters, "meters is {:.2f} inches".format(inches))




main()
# end of program file