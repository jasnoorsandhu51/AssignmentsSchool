def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
  cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
  print('Answer is: ',cost)
x = float(input('Miles per gallon: '))
y = float(input('Dollars per gallon: '))
z = float(input('Number of miles driven: '))
driving_cost(x,y,z)
