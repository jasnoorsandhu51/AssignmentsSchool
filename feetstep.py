def feet_to_steps(user_feet):
    steps = int(2.5 * user_feet)
    print (steps)
def main(user_feet):
    feet_to_steps(user_feet)
main(int(input('Feet: ')))