import numpy as np
import matplotlib.pyplot as plt
#definir el plonomio:P(x) = a*X^4 + b*x^3 + c*x^2 d*x * e
def P(x, a, b, c, d, e):
    return a*x**4 b*x**3 + c*x**2 d*x + e
    #coeficientes del polinomio (puedes cambiarlos)
    a, b, c, d, e = 1, -3, 2, 5, -4
    #rango de valores de x
    x_vals = np.linspace(-5, 5, 400)
    # evaluar el polinomio en cada x
    y_vals = P(x_vals, a, b, c, d, e)
    #crear la grafica
    plt.plot(x_vals, lebel=f'P(x) = {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e}')
    plt.anxhline(0, color='black', linewidth=1) # linea horisontal en y=0
    plt.axvline(0, color='black', linewidth=1) 3# linea vertical e3n x=0
    plt.grid(true, linestyle'--', alpha=0.6)
    plt.legend()
    plt.xlabel("x")
    plt.xlabel("p(x)")
    plt.title("grafico del polinomio de grado 4")
    plt.show()