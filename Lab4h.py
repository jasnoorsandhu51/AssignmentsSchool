# Prolog
# Author: Jasnoor Sandhu
# Email: jsandhu2@student.gsu.edu
# Section: 032
'''
Purpose:
Phone number breakdown
Pre-conditions (input):
(Enter the 10-digit phone number)
Post-conditions (output):
Breakdown of phone number (area code, prefix, line number)
'''
''' all of the code was out of the function perimeter(tab), fixed it.'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, line number")
    print()
    # 2. Input the 10-digit phone number
    '''made the variables same for input and print statement'''
    phone_int = int(input ('Enter Phone Number:--'))
    '''converted integer into string'''
    phone_str = str(phone_int)
    # 3. Breakdown the phone number
    # 4. Output breakdown to area code, prefix, line number
    '''print statement was incorrect, corrected it.'''
    print()
    '''print statement was missing the closing bracket'''
    print('Area Code: ',phone_str[0:3], 'Prefix: ',phone_str[3:6], 'Line Number: ',phone_str[6:11])
main()
# end of program file