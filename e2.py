import math
import matplotlib.pyplot as plt

def pow(x, n):
    return math.pow(x, n)

def yf(x):
    return -0.1*pow(x, 4) - 0.15*pow(x, 3) - 0.5*pow(x, 2) - 0.25*x + 1.2

def f(x, y):
    return yf(x)/y

x = 0.5
h = 0.25
n = 10

def euler():
    yi = yf(x)
    xi = x
    yValues = [yi]
    xValues = [xi]
    for i in range(0, n):
        yi += h * f(xi, yi)
        xi += h
        yValues.append(yi)
        xValues.append(xi)

    plt.plot(xValues, yValues)
    plt.plot(xValues, yValues, 'ro')
    plt.show()
    return zip(xValues, yValues)

def rk2():
    yi = yf(x)
    xi = x
    yValues = [yi]
    xValues = [xi]
    for i in range(0, n):
        k1 = f(xi, yi)
        xi += h
        k2 = f(xi, yi + h * k1)
        yi += h/2 * (k1 + k2)
        yValues.append(yi)
        xValues.append(xi)

    plt.plot(xValues, yValues)
    plt.plot(xValues, yValues, 'ro')
    plt.show()
    return zip(xValues, yValues)

def rk4():
    yi = yf(x)
    xi = x
    yValues = [yi]
    xValues = [xi]
    for i in range(0, n):
        k1 = f(xi, yi)
        k2 = f(xi + h/2, yi + h/2 * k1)
        k3 = f(xi + 1/2, yi + h/2 * k2)
        k4 = f(xi + h, yi + h * k3)
        yi += h/6 * (k1 + 2*k2 + 2*k3 + k4)
        xi += h
        yValues.append(yi)
        xValues.append(xi)

    plt.plot(xValues, yValues)
    plt.plot(xValues, yValues, 'ro')
    plt.show()
    return zip(xValues, yValues)

print("Euler")
print("(x, y)")
for p in euler():
    print(p)

print("\nRunge Kutta 2ª Ordem")
print("(x, y)")
for p in rk2():
    print(p)

print("\nRunge Kutta 4ª Ordem")
print("(x, y)")
for p in rk4():
    print(p)


