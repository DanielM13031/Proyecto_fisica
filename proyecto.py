import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Parametros del sistema
alpha = 0.1  #Tasa de crecimiento de las presas
beta = 0.02 #Tasa de depredacion
delta = 0.01 #Eficiencia de conversion de una presa a depredador
gamma = 0.1 #Tasa de mortalidad de los depredadores 
numero_de_p = 40 #numero de presas
numero_de_d = 20 #numero de depredadores

def lotka_volterra(y, t, alpha, beta, delta, gamma):   #Sistema de ecucuaiones diferenciales del modelo lotka
    x,y = y
    dx_dt = x*(alpha - (beta*y))
    dy_dt = y*(delta - (gamma*x))
    return[dx_dt, dy_dt]

y0 =[numero_de_p, numero_de_d] # presas, depredadores 
t = np.linspace(0,200,1000) 



#Clase presa
class presa:
    def __init__(self, vel, pos, masa, f):
        self.vel = vel
        self.pos = pos
        self.masa = masa
        self.f = f
    def cinematica(self, dt):
        self.dt = dt

        #Aceleracion
        aceleracion = (self.f/self.masa , self.f/self.masa)

        # Actualizar la velocidad
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Actualizar la posición
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

#Clase depredador
class depredador:
    def __init__(self,vel, pos, masa, f):
        self.vel = vel
        self.pos = pos
        self.masa = masa
        self.f = f 
    
    def cinematica(self, dt):
        self.dt = dt

        #Aceleracion
        aceleracion = (self.f/self.masa , self.f/self.masa)

        # Actualizar la velocidad
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Actualizar la posición
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

#creacion de los parametros para cada invidiuo del sistema
v_aleatorias_p = [(np.random.uniform(1,10),np.random.uniform(1,10)) for _ in range(numero_de_p)]
v_aleatorias_d = [(np.random.uniform(1,10),np.random.uniform(1,10)) for _ in range(numero_de_d)]

pos_aleatorias_p = [(np.random.uniform(1,50),np.random.uniform(1,50)) for _ in range(numero_de_p)]
pos_aleatorias_d = [(np.random.uniform(1,50),np.random.uniform(1,50)) for _ in range(numero_de_d)]

masa_aleatorias_p = [np.random.uniform(1,100) for _ in range(numero_de_p)]
masa_aleatorias_d = [np.random.uniform(1,100) for _ in range(numero_de_d)]

fuerza_aleatorias_p = [np.random.uniform(0.1,1) for _ in range(numero_de_p)]
fuerza_aleatorias_d = [np.random.uniform(0.1,1) for _ in range(numero_de_d)]

#Creacion de presas
presas = []
depredadores = []
for i, j, h, g in zip(v_aleatorias_p, pos_aleatorias_p, masa_aleatorias_p, fuerza_aleatorias_p):
    presas.append(presa(i, j, h, g))
#Creacion de depredadores
for i, j, h, g in zip(v_aleatorias_d, pos_aleatorias_d, masa_aleatorias_d, fuerza_aleatorias_d):
    depredadores.append(depredador(i, j, h, g))

dt = 0.1
distancia_umbral = 2.0
# Configuración de la visualización con Matplotlib
fig, ax = plt.subplots()
ax.set_xlim(0, 60)  # Ajustar los límites del espacio
ax.set_ylim(0, 60)

presas_plot, = plt.plot([], [], 'bo', markersize=5, label='Presas')  # Presas como puntos azules
depredadores_plot, = plt.plot([], [], 'ro', markersize=5, label='Depredadores')  # Depredadores como puntos rojos
plt.legend()

# Función para inicializar la animación
def init():
    presas_plot.set_data([], [])
    depredadores_plot.set_data([], [])
    return presas_plot, depredadores_plot

# Función para actualizar cada cuadro de la animación
def update(frame):
    # Actualizar la posición de todas las presas
    for presa in presas:
        presa.cinematica(dt)

    # Actualizar la posición de todos los depredadores y simular la persecución
    for depredador in depredadores:
        depredador.cinematica(dt)

        # Verificar la distancia con todas las presas para decidir la persecución
        for presa in presas:
            pos_presa = np.array(presa.pos)
            pos_depredador = np.array(depredador.pos)
            distancia = np.linalg.norm(pos_presa - pos_depredador)

            # Persecución si la distancia es menor que el umbral
            if distancia < distancia_umbral:
                direccion_persecucion = (pos_presa - pos_depredador) / distancia  # Vector unitario hacia la presa
                velocidad_persecucion = 2.0  # Velocidad de persecución fija

                # Actualizar la velocidad del depredador hacia la presa
                depredador.vel = (velocidad_persecucion * direccion_persecucion[0], velocidad_persecucion * direccion_persecucion[1])

    # Obtener las posiciones actuales de presas y depredadores
    presas_x = [presa.pos[0] for presa in presas]
    presas_y = [presa.pos[1] for presa in presas]

    depredadores_x = [depredador.pos[0] for depredador in depredadores]
    depredadores_y = [depredador.pos[1] for depredador in depredadores]

    # Actualizar los datos de la gráfica
    presas_plot.set_data(presas_x, presas_y)
    depredadores_plot.set_data(depredadores_x, depredadores_y)

    return presas_plot, depredadores_plot

# Crear la animación
ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, interval=100)

# Mostrar la animación
plt.show()

# Resolver el sistema de ecuaciones diferenciales
solution = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
presas, depredadores = solution.T  # Extraer soluciones para presas y depredadores

# Graficar la evolución de las poblaciones a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(t, presas, label='Presas', color='b')
plt.plot(t, depredadores, label='Depredadores', color='r')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Evolución de las poblaciones de presas y depredadores')
plt.legend()
plt.grid(True)
plt.show()
