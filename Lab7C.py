'''
Prolong:
Name-Jasnoor Sandhu
Section-032
Panther ID-002703234 
'''



def main():
    num = int(input('Your number: '))
    n1 = 0
    num1 = 0
    while num1 < num:
        n1 += 1
        num1 = 2 ** n1
        if num1 == num:
            print ('2 **',n1)
        if num1 > num:
            n1 -= 1 
            num1 /= 2
            print (f'(2 ** {n1}) + ', end = "" )
            num = num - num1
            n1 = 0
            num1 = 0
            if num == 0:
                print('0')
                break
main()
