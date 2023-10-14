#!/usr/bin/env python
#coding: utf-8
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
N = 100 # число точек в реализации
dt = 0.15 # шаг интегрирования
y_true=[]
mas=[]
y_pred=[]
Q=[]
x = np.zeros(N)
y = np.zeros(N)
# Задание начальных условий и параметров
x[0] = 100
y[0] = 0
a=3/2
b=1/2
c=1/10000
#Построение координат методом Адамса
for i in range(1, N):
    x[i] = x[i-1] + dt * (a*y[i-1]-b*y[i-1])
    y[i] = y[i-1] + dt * (a*(c*(1-pow(x[i-1],2))*y[i-1]-x[i-1])-b*(c*(1-pow(x[i-2],2))*y[i-2]-x[i-2]))
print(y)
print(len(y))
# Построение массива рандомных чисел-ожидаемые значения
import random
for i in range(0, N):
    y_pred.append(random.uniform(min(y),max(y)))
print(y_pred)
print(len(y_pred))
# Среднеквадратичная ошибка
import sklearn
from sklearn.metrics import mean_squared_error
p=mean_squared_error(y, y_pred)
print(p)
# Формирование массива среднеквадратичной ошибки
for i in range(0, N):
    Q.append(random.uniform(0,p))
print(Q)
print(len(Q))
# Задание времени построения точек по шагу интегрирования, построение графика
t = np.arange(0, N*dt, dt)
print(t)
print(len(t))
plt.plot(t, Q)
plt.show()