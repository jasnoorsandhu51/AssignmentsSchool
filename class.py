'''
Prolong-
Name - Jasnoor Singh Sandhu
Section - 032
Panther ID - 002703837
Lab 6
'''
def main():
    row1 = str(input('Input Row 1:--'))
    row2 = str(input('Input Row 2:--'))
    row3 = str(input('Input Row 3:--'))

#for X
    #setting up diagonals
    if row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
        print('X is good in diagonal')
    elif row3[0] == 'X' and row2[1] == 'X' and row1[2] == 'X':
        print('X is good in diagonal')
    #setting up horizontals
    elif row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
        print('X is good in horizontal')
    elif row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
        print('X is good in horizontal')
    elif row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X':
        print('X is good in horizontal')
    #setting up verticals
    elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X':
        print('X is good in vertical')
    elif row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X':
         print('X is good in vertical')
    elif row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
        print('X is good in vertical')
    #for O
    #setting up diagonals
    elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
        print('O is good in diagonal')
    elif row3[0] == 'O' and row2[1] == 'O' and row1[2] == 'O':
        print('O is good in diagonal')
    #setting up horizontals
    elif row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
        print('O is good in horizontal')
    elif row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
        print('O is good in horizontal')
    elif row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O':
        print('O is good in horizontal')
    #setting up verticals
    elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O':
        print('O is good in vertical')
    elif row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O':
         print('O is good in vertical')
    elif row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
        print('O is good in vertical')
    else:
        print ('Game is tied.')

main()