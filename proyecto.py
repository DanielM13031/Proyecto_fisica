import numpy as np
from scipy.integrate import odeint


# Parametros del sistema
alpha = 0.1  #Tasa de crecimiento de las presas
beta = 0.02 #Tasa de depredacion
delta = 0.01 #Eficiencia de conversion de una presa a depredador
gamma = 0.1 #Tasa de mortalidad de los depredadores 
numero_de_p = 40
numero_de_d = 9

def lotka_volterra(y, t, alpha, beta, delta, gamma):   #Sistema de ecucuaiones diferenciales del modelo lotka
    x,y = y
    dx_dt = x*(alpha - (beta*y))
    dy_dt = y*(delta - (gamma*x))
    return[dx_dt, dy_dt]

y0 =[numero_de_p, numero_de_d] # presas, depredadores 
t = np.linspace(0,200,1000) 

#Clase presa
class presa:
    def __init__(self, vel, pos):
        self.vel = vel
        self.pos = pos
#Clase depredador
class depredador:
    def __init__(self,vel, pos):
        self.vel = vel
        self.pos = pos

v_aleatorias_p = [(np.random.uniform(1,10),np.random.uniform(1,10)) for _ in range(numero_de_p)]
v_aleatorias_d = [(np.random.uniform(1,10),np.random.uniform(1,10)) for _ in range(numero_de_d)]

pos_aleatorias_p = [(np.random.uniform(1,50),np.random.uniform(1,50)) for _ in range(numero_de_p)]
pos_aleatorias_d = [(np.random.uniform(1,50),np.random.uniform(1,50)) for _ in range(numero_de_d)]

presas = []
depredadores = []

#Creacion de presas
for i, j in zip(v_aleatorias_p, pos_aleatorias_p):
    presas.append(presa(i, j))
#Creacion de depredadores
for i, j in zip(v_aleatorias_d, pos_aleatorias_d):
    depredadores.append(depredador(i, j))

solution = odeint(lotka_volterra, y0, t, args=(alpha,beta,delta,gamma))
