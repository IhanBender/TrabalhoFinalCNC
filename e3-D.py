def yd(y):
    return 2 * y * (92 - y)/92

def rk2(h, y0, x0, n):
    yi = y0
    xi = x0
    while xi < n:
        xi += h
        k1 = h * yd(yi)
        k2 = h * yd(yi + h * k1)
        yi = yi + h/2 * (k1 + k2)

    return yi

estudantes = rk2(1, 10, 0, 3)

print("Aproximadamente " + str(round(estudantes, 5)) + " estudantes tomaram conhecimento do boato após 3 horas.")