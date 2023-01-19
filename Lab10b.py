def swap_values(user_val1, user_val2, user_val3, user_val4):
    # swapping 1 and 4
    x = user_val1 
    user_val1 = user_val2
    user_val2 = x

    y = user_val3
    user_val3 = user_val4
    user_val4 = y
    print(user_val1, user_val2, user_val3, user_val4)
swap_values(8,3,4,2)