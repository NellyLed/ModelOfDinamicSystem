#!/usr/bin/env python
#coding: utf-8
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
N = 20000 # число точек в реализации
dt = 0.15 # шаг интегрирования
# Задание функции уравнения
def ode(z,t,c):
    x,y=z
    dydt=[y,c*(1-pow(x,2))*y-x]
    return dydt
# Задание времени построения точек по шагу интегрирования и построение вектора отображения координат
def calcODE(args,x0,y0,N=20000,dt=0.15):
    x0=[x0,y0]
    t=np.arange(0,N*dt,dt)
    sol=odeint(ode,x0,t,args)
    return sol
# Задание функции для вывода фазового портрета на основании введенной функции
def drawPhasePortrait(args, deltaX = 1, deltaDX = 1, startX = 0, stopX = 5, startDX = 0, stopDX = 5, N=20000, dt=0.15):
    for x0 in range(startX, stopX, deltaX):
        for y0 in range(startDX, stopDX, deltaDX):
            sol = calcODE(args, x0, y0, N, dt)
            plt.plot(sol[:, 1], sol[:, 0], 'b')
    plt.xlabel('x')
    plt.ylabel('dx/dt')
    plt.grid()
    plt.show()
# Начальные параметры
c = 0.00001
args=(c,)
drawPhasePortrait(args)
drawPhasePortrait(args, 1, 1, -10,10,-5,5, N=20000, dt=0.15)