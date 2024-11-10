import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del sistema Lotka-Volterra
alpha = 0.3  # Tasa de crecimiento de las presas
beta = 0.02  # Tasa de depredación
delta = 0.01 # Eficiencia de conversión de una presa a depredador
gamma = 0.1  # Tasa de mortalidad de los depredadores 
numero_de_p = 40  # Número inicial de presas
numero_de_d = 20  # Número inicial de depredadores

# Definir las ecuaciones diferenciales del modelo Lotka-Volterra
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    x, y = y
    dx_dt = x * (alpha - (beta * y))
    dy_dt = y * (delta * x - gamma)
    return [dx_dt, dy_dt]

# Condiciones iniciales y rango de tiempo
y0 = [numero_de_p, numero_de_d]
t = np.linspace(0, 200, 1000)

# Resolver el sistema de ecuaciones diferenciales Lotka-Volterra
solution = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
presas_lotka, depredadores_lotka = solution.T

# Definir la clase Presa
class Presa:
    def __init__(self, vel, pos, masa, f, energia):
        self.vel = vel  # Velocidad (vx, vy)
        self.pos = pos  # Posición (x, y)
        self.masa = masa  # Masa
        self.f = f  # Fuerza
        self.energia = energia  # Energía
        self.vel_max = 5  # Velocidad máxima

    def cinematica(self, dt):
        # Movimiento aleatorio para evitar un patrón muy rígido
        ruido = (np.random.uniform(-1, 1), np.random.uniform(-1, 1))
        self.vel = (self.vel[0] + ruido[0] * 0.1, self.vel[1] + ruido[1] * 0.1)

        # Limitar la velocidad para que no sea demasiado alta
        velocidad = np.linalg.norm(self.vel)
        if velocidad > self.vel_max:
            factor = self.vel_max / velocidad
            self.vel = (self.vel[0] * factor, self.vel[1] * factor)

        # Calcular la aceleración (a = F / m)
        aceleracion = (self.f / self.masa, self.f / self.masa)

        # Actualizar la velocidad: v = v + a * dt
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Actualizar la posición: pos = pos + v * dt
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

        # Reducir energía según la velocidad
        gasto_energia = 0.01 * (self.vel[0]**2 + self.vel[1]**2) * dt
        self.energia -= gasto_energia

# Definir la clase Depredador
class Depredador:
    def __init__(self, vel, pos, masa, f, energia):
        self.vel = vel  # Velocidad (vx, vy)
        self.pos = pos  # Posición (x, y)
        self.masa = masa  # Masa
        self.f = f  # Fuerza
        self.energia = energia  # Energía
        self.vel_max = 7  # Velocidad máxima para el depredador, normalmente mayor que la de la presa

    def cinematica(self, dt):
        # Calcular la aceleración (a = F / m)
        aceleracion = (self.f / self.masa, self.f / self.masa)

        # Actualizar la velocidad: v = v + a * dt
        self.vel = (self.vel[0] + aceleracion[0] * dt, self.vel[1] + aceleracion[1] * dt)

        # Limitar la velocidad para evitar movimientos irreales
        velocidad = np.linalg.norm(self.vel)
        if velocidad > self.vel_max:
            factor = self.vel_max / velocidad
            self.vel = (self.vel[0] * factor, self.vel[1] * factor)

        # Actualizar la posición: pos = pos + v * dt
        self.pos = (self.pos[0] + self.vel[0] * dt, self.pos[1] + self.vel[1] * dt)

        # Reducir energía según la velocidad
        gasto_energia = 0.02 * (self.vel[0]**2 + self.vel[1]**2) * dt
        self.energia -= gasto_energia

# Creación de presas y depredadores con parámetros aleatorios
def crear_presa():
    vel = (np.random.uniform(1, 3), np.random.uniform(1, 3))
    pos = (np.random.uniform(1, 100), np.random.uniform(1, 100))
    masa = np.random.uniform(5, 20)
    f = np.random.uniform(0.1, 1)
    energia = np.random.uniform(50, 100)  
    return Presa(vel, pos, masa, f, energia)

def crear_depredador():
    vel = (np.random.uniform(1, 4), np.random.uniform(1, 4))
    pos = (np.random.uniform(1, 100), np.random.uniform(1, 100))
    masa = np.random.uniform(20, 50)
    f = np.random.uniform(0.5, 2)
    energia = np.random.uniform(100, 150)  
    return Depredador(vel, pos, masa, f, energia)

presas = [crear_presa() for _ in range(numero_de_p)]
depredadores = [crear_depredador() for _ in range(numero_de_d)]

# Parámetro de paso de tiempo y distancia umbral
dt = 0.1
distancia_umbral = 5.0
distancia_captura = 1.0  

# Configuración de la visualización con Matplotlib
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Configuración del gráfico espacial (presas y depredadores)
ax[0].set_xlim(0, 100)
ax[0].set_ylim(0, 100)
ax[0].set_title('Movimiento de Presas y Depredadores')
presas_plot, = ax[0].plot([], [], 'bo', markersize=5, label='Presas')
depredadores_plot, = ax[0].plot([], [], 'ro', markersize=5, label='Depredadores')
ax[0].legend()

# Configuración del gráfico Lotka-Volterra (evolución de la población)
ax[1].set_xlim(0, 200)
ax[1].set_ylim(0, max(max(presas_lotka), max(depredadores_lotka)) * 1.1)
ax[1].set_title('Evolución de las Poblaciones de Presas y Depredadores')
ax[1].set_xlabel('Tiempo')
ax[1].set_ylabel('Población')
ax[1].grid(True)
presas_line, = ax[1].plot([], [], 'b-', label='Presas (Modelo Lotka-Volterra)')
depredadores_line, = ax[1].plot([], [], 'r-', label='Depredadores (Modelo Lotka-Volterra)')
ax[1].legend()

# Función para inicializar la animación
def init():
    presas_plot.set_data([], [])
    depredadores_plot.set_data([], [])
    presas_line.set_data([], [])
    depredadores_line.set_data([], [])
    return presas_plot, depredadores_plot, presas_line, depredadores_line

# Función para actualizar cada cuadro de la animación
def update(frame):
    # Eliminar presas y depredadores sin energía
    presas[:] = [presa for presa in presas if presa.energia > 0]
    depredadores[:] = [depredador for depredador in depredadores if depredador.energia > 0]

    # Actualizar el número de presas y depredadores según el modelo Lotka-Volterra
    cantidad_presas = int(presas_lotka[frame])
    cantidad_depredadores = int(depredadores_lotka[frame])

    # Ajustar la cantidad de presas en la simulación
    while len(presas) < cantidad_presas:
        presas.append(crear_presa())
    while len(presas) > cantidad_presas:
        presas.pop()

    # Ajustar la cantidad de depredadores en la simulación
    while len(depredadores) < cantidad_depredadores:
        depredadores.append(crear_depredador())
    while len(depredadores) > cantidad_depredadores:
        depredadores.pop()

    # Actualizar la posición de todas las presas
    for presa in presas:
        presa.cinematica(dt)

    # Actualizar la posición de todos los depredadores y simular la persecución
    presas_capturadas = []
    for depredador in depredadores:
        depredador.cinematica(dt)

        # Verificar la distancia con todas las presas para decidir la persecución
        for presa in presas:
            pos_presa = np.array(presa.pos)
            pos_depredador = np.array(depredador.pos)
            distancia = np.linalg.norm(pos_presa - pos_depredador)

            # Si la distancia es menor que la distancia de captura, eliminar la presa
            if distancia < distancia_captura:
                presas_capturadas.append(presa)
                depredador.energia += 20 


            elif distancia < distancia_umbral:
                direccion_persecucion = (pos_presa - pos_depredador) / distancia
                fuerza_aplicada = depredador.f * direccion_persecucion 
                aceleracion = fuerza_aplicada / depredador.masa  # a = F / m

                # Actualizar la velocidad del depredador
                depredador.vel = (
                    depredador.vel[0] + aceleracion[0] * dt,
                    depredador.vel[1] + aceleracion[1] * dt
                )

    # Eliminar las presas capturadas de la lista de presas
    for presa in presas_capturadas:
        if presa in presas:
            presas.remove(presa)

    # Obtener las posiciones actuales de presas y depredadores
    presas_x = [presa.pos[0] for presa in presas]
    presas_y = [presa.pos[1] for presa in presas]

    depredadores_x = [depredador.pos[0] for depredador in depredadores]
    depredadores_y = [depredador.pos[1] for depredador in depredadores]

    # Actualizar los datos de la gráfica espacial
    presas_plot.set_data(presas_x, presas_y)
    depredadores_plot.set_data(depredadores_x, depredadores_y)

    # Actualizar la gráfica de las poblaciones (Lotka-Volterra)
    presas_line.set_data(t[:frame], presas_lotka[:frame])
    depredadores_line.set_data(t[:frame], depredadores_lotka[:frame])

    return presas_plot, depredadores_plot, presas_line, depredadores_line

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=100)

# Mostrar la animación
plt.tight_layout()
plt.show()
