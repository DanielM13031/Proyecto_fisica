import numpy as np
from scipy.integrate import odeint

# Parametros del sistema
alpha = 0.1  #Tasa de crecimiento de las presas
beta = 0.02 #Tasa de depredacion
delta = 0.01 #Eficiencia de conversion de una presa a depredador
gamma = 0.1 #Tasa de mortalidad de los depredadores 

def lotka_volterra(y, t, alpha, beta, delta, gamma):   #Sistema de ecucuaiones diferenciales del modelo lotka
    x,y = y
    dx_dt = x*(alpha - (beta*y))
    dy_dt = y*(delta - (gamma*x))
    return[dx_dt, dy_dt]

y0 =[40,9] # presas, depredadores 
t = np.linspace(0,200,1000) 


solution = odeint(lotka_volterra, y0, t, args=(alpha,beta,delta,gamma))