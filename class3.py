#Jasnoor Sandhu 002703837
import math
x = float(input(" First number: "))
y = float(input(" Second number: "))
z = float(input(" Third number: "))
y_z = y ** z
x_z = x ** z

a = x ** z
b = x ** y_z
c = abs(x - y)
d = math.sqrt(x ** z )


print(f'{a:.2f} {b:.2f} {c:.2f} {d:.2f}')