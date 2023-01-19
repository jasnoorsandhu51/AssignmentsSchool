def main():
    x = int(input("Input a Number: "))
    while x >= 1:
        y = x % 2
        x = x / 2
        print(int(y))
main()