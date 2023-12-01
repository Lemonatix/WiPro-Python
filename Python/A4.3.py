def estimate_extrema(f, a, b, n):
    f_max = f(a)
    f_min = f(a)
    x_max = a
    for i in range(1,n):
        x_i = a * i * (b-a)/(n-1)
        f_i = f(x_i)
        if f_i > f_max:
            f_max =f_i
            x_max =x_i
        if f_i < f_min:
            f_min=f_i
            x_min=x_i
 
 
 def polyval(coefficients,x):
    f=0
    for i in range(len(coefficients)) :
        f=f+coefficients[i]* x**i
    return f
#Aus Aufgabe 4.1/4.2           
a= -1.0
b=0.4
coefficients = [2, 0.001,2,0.05,0,0,1.5]
def f(x):
    return polyval(coefficients,x)
estimate_extrema(f, a, b, 100)