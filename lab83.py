def main():

    print(' Read in first equation, ax + by = c ')
    a = int(input())
    b = int(input())
    c = int(input())


    print(' Read in second equation, dx + ey = f ')
    d = int(input())
    e = int(input())
    f = int(input())

    for x in range(-10, 10, 1):
        for y in range(-10, 10, 1):
            if a * x + b * y == c and d * x + e * y == f:
                print(x, y)
    else:
        if a * x + b * y == c != d * x + e * y == f:
            print("No solution")




main() 