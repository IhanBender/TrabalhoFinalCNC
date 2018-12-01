import math

def f(x):
    return 6 + 3 * math.cos(x)

def analytical(a, b):
    return (6*b + 3*math.sin(b)) - (6*a + 3*math.sin(a))

def trapezio(a, b, n):
    h = (b - a)/n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + h*i)

    return h/2 * result

def simp1_3(a, b, n):
    h = (b - a)/n

    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            t = 2
        else:
            t = 4
        result += t * f(a + h * i)

    return h/3 * result

def simp3_8(a, b, n):
    h = (b - a)/n

    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            t = 2
        else:
            t = 3
        result += t * f(a + h * i)

    return 3*h/8 * result

a = 0
b = math.pi/2
s = analytical(a, b)
print("Solução analítica:\t" + str(round(s, 5)))

it = 10
print("\nTrapézio Repetida")
trap = trapezio(a, b, it)
er = abs(s - trap)
print("\tSubintervalos:\t" + str(it))
print("\tResultado:    \t" + str(round(trap, 5)))
print("\tErro relativo:\t" + str(round(er, 5)))

print("\n1/3 de Simpson Repetida")
s13 = simp1_3(a, b, it)
er = abs(s - s13)
print("\tSubintervalos:\t" + str(it))
print("\tResultado:    \t" + str(round(s13, 5)))
print("\tErro relativo:\t" + str(round(er, 5)))

print("\n3/8 de Simpson Repetida")
s38 = simp3_8(a, b, it)
er = abs(s - s38)
print("\tSubintervalos:\t" + str(it))
print("\tResultado:    \t" + str(round(s38, 5)))
print("\tErro relativo:\t" + str(round(er, 5)))
