#!/usr/bin/env python
#coding: utf-8
import numpy as np
from matplotlib import pyplot as plt
N = 100 # число точек в реализации
dt = 0.15 # шаг интегрирования
x = np.zeros(N)
y = np.zeros(N)
# Задание начальных условий
x[0] = 100
y[0] = 0
a=3/2
b=1/2
c=1/10000
# Нахождение координат методом Адамса
for i in range(1, N):
    x[i] = x[i-1] + dt * (a*y[i-1]-b*y[i-1])
    y[i] = y[i-1] + dt * (a*(c*(1-pow(x[i-1],2))*y[i-1]-x[i-1])-b*(c*(1-pow(x[i-2],2))*y[i-2]-x[i-2]))
# Задание времени построения точек по шагу интегрирования, построение графика
t = np.arange(0, N*dt, dt)
plt.plot(t, x, t, y)
plt.show()