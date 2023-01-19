#Name- Jasnoor Sandhu 002703837
Age = int(input("Whats your age? "))
Weight = int(input("How much do you weigh? "))
Heart_Rate = int(input("What is the heart rate? "))
Time = int(input("How much time? "))

Calories = ( (Age * 0.2757) + (Weight * 0.03295) + (Heart_Rate * 1.0781) - 75.4991 ) * Time / 8.368
print(f'{Calories:.2f} calories')