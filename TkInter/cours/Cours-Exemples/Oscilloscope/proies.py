# -*- coding: utf-8 -*-
# José OUIN : algorithmique et calcul numérique, ellipses 2013
import matplotlib.pyplot as plt
import numpy as np


def proies_variation(u, v, a, b):
    return u*(a - b*v)


def predateurs_variation(u, v, c, d):
    return v*(-c + d*u)

if __name__ == "__main__":
    a, b = 0.8, 0.4
    c, d = 0.6, 0.2
    u0, v0 = 3, 5
    t_debut, t_fin = 0.0, 20.0
    n = 200

    h = (t_fin - t_debut)/n
    t = np.zeros(n+1)
    proies = np.zeros(n+1)
    predateurs = np.zeros(n+1)

    t[0], proies[0], predateurs[0] = t_debut, u0, v0
    for i in range(n):
        t[i+1] = t[0] + h*(i+1)
        proies[i+1] = proies[i] + h*proies_variation(proies[i], predateurs[i], a, b)
        predateurs[i+1] = predateurs[i] + h*predateurs_variation(proies[i], predateurs[i], a, b)

    plt.plot(t, proies, "+b")
    plt.plot(t, predateurs, "*r")
    plt.plot(proies, predateurs, "-g")
    plt.show()
