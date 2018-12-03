import math
import matplotlib.pyplot as plt

def pow(x, n):
    return math.pow(x, n)

def y(x):
    return -0.1*pow(x, 4) - 0.15*pow(x, 3) - 0.5*pow(x, 2) - 0.25*x + 1.2

def yd(x):
    return -0.4*pow(x, 3) - 0.45*pow(x, 2) - x - 0.25

x = 0.5
h = 0.25
n = 10

def euler():
    yi = y(x)
    xi = x
    yValues = [yi]
    xValues = [xi]
    for i in range(0, n):
        yi = yi + h * y(xi)
        xi += h
        yValues.append(yi)
        xValues.append(xi)

    plt.plot(xValues, yValues)
    plt.plot(xValues, yValues, 'ro')
    plt.show()
    return zip(xValues, yValues)

def rk2():
    yi = y(x)
    xi = x
    yValues = [yi]
    xValues = [xi]
    for i in range(0, n):
        k1 = y(io)
        yi = yi + h/2 * (k1 + k2)

print("Euler")
print("(x, y)")
for p in euler():
    print(p)


