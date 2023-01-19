def exact_change():
    change = int(input("Whats the change in cents: "))
    num_quarters = change // 25
    remain = change % 25
    num_dimes = remain // 10
    remain = remain % 10
    num_nickels = remain // 5
    remain = remain % 5
    num_pennies = remain 
    print("Quarters: ",num_quarters,"Dimes: ", num_dimes,"Nickels: ", num_nickels,"Pennies: ", num_pennies)
exact_change()
