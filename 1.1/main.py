from math import sin
import numpy as np
import matplotlib.pyplot as plt
from random import random
from datetime import datetime
import time

# IP 7424
# Skrygun Vlad
n = 12
N = 1024
Wгрm = 2400
Wгрp_step = Wгрm / n
Ap = random()
φ = random()
print(f'n = {n}, N = {N}, Wгрm = {Wгрm}, Ap = {Ap}, φ = {φ}')
start_time = datetime.now()
count = 0
def generate_point(i, t):
    global count
    count+=1
    wp = (Wгрp_step * (i + 1))
    return Ap * sin(wp * t + φ)
array = np.fromfunction(np.vectorize(generate_point), (n, N))
x = np.sum(array, axis=0)
print(x)
deviation = np.std(x)
mean = np.mean(x)
#print(datetime.now() - start_time)
print(f'mean = {mean:.3f}, st deviation = {deviation:.3f}')
plt.plot(np.arange(1, N + 1), x)
plt.xlabel('N')
plt.ylabel('x')
plt.title(rf'$\mu = {mean:.3f}, \sigma = {deviation:.3f}$')
plt.show()
#print(f'count = {count}')