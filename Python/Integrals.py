# Datei: Integrals.py

import math

def Midpoint(f, a=0, b=1, n=100):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + (i + 0.5) * h)
    return result * h

def Trapezoidal(f, a=0, b=1, n=100):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h
