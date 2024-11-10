import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del sistema Lotka-Volterra
alpha = 0.1  # Tasa de crecimiento de las presas
beta = 0.02  # Tasa de depredación
delta = 0.01 # Eficiencia de conversión de una presa a depredador
gamma = 0.1  # Tasa de mortalidad de los depredadores 
numero_de_p = 40  # Número de presas
numero_de_d = 10  # Número de depredadores

# Definir las ecuaciones diferenciales del modelo Lotka-Volterra
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    x, y = y
    dx_dt = x * (alpha - (beta * y))
    dy_dt = y * (delta * x - gamma)
    return [dx_dt, dy_dt]

# Condiciones iniciales y rango de tiempo
y0 = [numero_de_p, numero_de_d]
t = np.linspace(0, 200, 1000)

# Definir la clase Presa
class Presa:
    def __init__(self, vel, pos, masa, f):
        self.vel = vel  # Velocidad (vx, vy)
        self.pos = pos  # Posición (x, y)
        self.masa = masa  # Masa
        self.f = f  # Fuerza

    def cinematica(self, dt):
        # Calcular la aceleración (a = F / m)
        aceleracion = (self.f / self.masa, self.f / self.masa)

        # Actualizar la velocidad: v = v + a * dt
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Actualizar la posición: pos = pos + v * dt
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

# Definir la clase Depredador
class Depredador:
    def __init__(self, vel, pos, masa, f):
        self.vel = vel  # Velocidad (vx, vy)
        self.pos = pos  # Posición (x, y)
        self.masa = masa  # Masa
        self.f = f  # Fuerza

    def cinematica(self, dt):
        # Calcular la aceleración (a = F / m)
        aceleracion = (self.f / self.masa, self.f / self.masa)

        # Actualizar la velocidad: v = v + a * dt
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Actualizar la posición: pos = pos + v * dt
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

# Creación de presas y depredadores con parámetros aleatorios
v_aleatorias_p = [(np.random.uniform(1, 5), np.random.uniform(1, 5)) for _ in range(numero_de_p)]
v_aleatorias_d = [(np.random.uniform(1, 5), np.random.uniform(1, 5)) for _ in range(numero_de_d)]

pos_aleatorias_p = [(np.random.uniform(1, 50), np.random.uniform(1, 50)) for _ in range(numero_de_p)]
pos_aleatorias_d = [(np.random.uniform(1, 50), np.random.uniform(1, 50)) for _ in range(numero_de_d)]

masa_aleatorias_p = [np.random.uniform(5, 20) for _ in range(numero_de_p)]
masa_aleatorias_d = [np.random.uniform(20, 50) for _ in range(numero_de_d)]

fuerza_aleatorias_p = [np.random.uniform(0.1, 1) for _ in range(numero_de_p)]
fuerza_aleatorias_d = [np.random.uniform(0.5, 2) for _ in range(numero_de_d)]

presas = [Presa(v, p, m, f) for v, p, m, f in zip(v_aleatorias_p, pos_aleatorias_p, masa_aleatorias_p, fuerza_aleatorias_p)]
depredadores = [Depredador(v, p, m, f) for v, p, m, f in zip(v_aleatorias_d, pos_aleatorias_d, masa_aleatorias_d, fuerza_aleatorias_d)]

# Parámetro de paso de tiempo y distancia umbral
dt = 0.1
distancia_umbral = 5.0  # Aumenté el umbral para dar más espacio a la persecución

# Configuración de la visualización con Matplotlib
fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(0, 60)

presas_plot, = plt.plot([], [], 'bo', markersize=5, label='Presas')
depredadores_plot, = plt.plot([], [], 'ro', markersize=5, label='Depredadores')
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

            # Si la distancia es menor que el umbral, el depredador persigue a la presa
            if distancia < distancia_umbral:
                direccion_persecucion = (pos_presa - pos_depredador) / distancia  # Vector unitario hacia la presa
                fuerza_aplicada = depredador.f * direccion_persecucion  # Fuerza aplicada hacia la presa

                # Calcular la aceleración resultante (a = F / m)
                aceleracion = fuerza_aplicada / depredador.masa

                # Actualizar la velocidad del depredador
                depredador.vel = (
                    depredador.vel[0] + aceleracion[0] * dt,
                    depredador.vel[1] + aceleracion[1] * dt
                )

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

# Resolver el sistema de ecuaciones diferenciales Lotka-Volterra
solution = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
presas, depredadores = solution.T

# Graficar la evolución de las poblaciones de presas y depredadores
plt.figure(figsize=(10, 6))
plt.plot(t, presas, label='Presas', color='b')
plt.plot(t, depredadores, label='Depredadores', color='r')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Evolución de las poblaciones de presas y depredadores')
plt.legend()
plt.grid(True)
plt.show()
