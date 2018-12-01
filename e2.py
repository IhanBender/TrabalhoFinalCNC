def pow(x, n):
    return math.pow(x, n)

def y(x):
    return -0.1*pow(x, 4) - 0.15*pow(x, 3) - 0.5*pow(x, 2) - 0.25*x + 1.2

x = 0.5
h = 0.25

def euler(f, n):
    yi = y(x)
    # for i in range(0, n):
    #     yi =
