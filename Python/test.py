# Datei: test.py

import math
import numpy as np
from Integrals import Midpoint, Trapezoidal

# Testfunktionen
f_sin = math.sin
f_poly = lambda x: np.polyval([2.0, 0, 0.1], x)

# Testen der Funktionen
print("Midpoint mit Sinusfunktion:", Midpoint(f_sin))
print("Trapezoidal mit Sinusfunktion:", Trapezoidal(f_sin))

print("Midpoint mit Polynom:", Midpoint(f_poly))
print("Trapezoidal mit Polynom:", Trapezoidal(f_poly))
from Integrals import Midpoint, Trapezoidal
import math

def exact_integral():
    return 2  # Exaktes Integral von sin(x) von 0 bis pi

def analyze_error(f, a, b, N):
    exact = exact_integral()
    midpoint_error = abs(exact - Midpoint(f, a, b, N))
    trapezoidal_error = abs(exact - Trapezoidal(f, a, b, N))
    return midpoint_error, trapezoidal_error

# Testen der Funktionen für verschiedene N
a, b = 0, math.pi
N_values = [10, 20, 40, 80, 160]  # Verschiedene Werte für N

print("N\tMidpoint Error\tTrapezoidal Error")
for N in N_values:
    midpoint_error, trapezoidal_error = analyze_error(math.sin, a, b, N)
    print(f"{N}\t{midpoint_error:.6f}\t{trapezoidal_error:.6f}")
