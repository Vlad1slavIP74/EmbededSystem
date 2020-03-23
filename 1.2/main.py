import math
import typing as t
from random import random
from operator import truediv

import numpy as np
from matplotlib import pyplot as plt

# Vlad Skrygun

n = 12
N = 1024
Wp = 2400
print(
    f'n = {n}, '
    f'N = {N}, '
    f'Wp = {Wp}'
)


def get_point(p, t, Ap, phi):
    wp = (Wp / n * (p + 1))
    return Ap * math.sin(wp * t + phi)


def get_graphs():
    graphs = []
    for p in range(n):
        Ap = random()
        phi = random()
        graphs.append([get_point(p, t, Ap, phi) for t in range(N)])

    return graphs


def get_correlation(
        x: t.Sequence[float],
        y: t.Sequence[float],
) -> t.Sequence[float]:
    res = [0] * N
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(N):
        for j in range(N):
            if i + j >= N:
                continue
            res[i] += (x[i] - x_mean) * (y[i + j] - y_mean)

        res[i] /= N

    return res


x_arr = np.sum(get_graphs(), axis=0)
y_arr = np.sum(get_graphs(), axis=0)

plt.figure(figsize=(14, 22))
plt.subplot(5, 1, 1)
plt.xlabel('N')
plt.ylabel('x')
plt.bar(range(N), x_arr)

plt.subplot(5, 1, 2)
plt.xlabel('N')
plt.ylabel('y')
plt.bar(range(N), y_arr)

plt.subplot(5, 1, 3)
plt.xlabel('N')
plt.ylabel('Rxy')
plt.bar(range(N), get_correlation(x_arr, y_arr))

plt.subplot(5, 1, 4)
plt.xlabel('N')
plt.ylabel('Rxx')
plt.bar(range(N), get_correlation(x_arr, x_arr))

plt.subplot(5, 1, 5)
plt.xlabel('N')
plt.ylabel('Ryy')
plt.bar(range(N), get_correlation(y_arr, y_arr))

plt.show()