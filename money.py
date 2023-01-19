quarters = int(input("How many quaters? "))
dimes = int(input("How many dimes? "))
nickels = int(input("how many nickles? "))
pennies = int(input("how many pennies? "))

sum = (quarters * 0.25) + (pennies * 0.01) + (dimes * 0.10) + (nickels * 0.05)
print(f'Amount: ${sum:.2f}')