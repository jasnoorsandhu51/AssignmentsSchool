def main():
    import random
    money = int(input('Your net worth:  '))
    count = 0
    maxf = money
    while money > 0:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if maxf > money:
            max = money
        if d1 + d2 == 7:
            money += 4
        else:
            money -= 1
        count += 1
    print('You played for ',count,'times and ended up being broke')
    print(max)
main()