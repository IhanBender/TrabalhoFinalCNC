import math

def f(x, a):
    return math.exp(a*x)/x

def fdd(x, a):
    return (math.exp(a*x) * (a*a*x*x - 2 * (a*x - 1)))/x*x*x
def I(a):
    Et  = 0.05
    n = 0
    x0 = 1
    x1 = 2
    while Et >= 0.05:
        n += 1
        h = (x1 - x0)/n
        Et = 0
        for i in range(0, n):
            Et += -(h*h*h)/12 * fdd(x0, a)
        Et = abs(Et)
    result = f(x0, a) + f(x1, a)
    for i in range(1, n):
        result += 2 * f(x0 + h*i, a)

    return [n, Et, h/2 * result]

subintervalos, erro, integral = I(1)

print("Subintervalos:\t" + str(subintervalos))
print("Erro estimado:\t" + str(erro))
print("Resultado I(1):\t" + str(integral))