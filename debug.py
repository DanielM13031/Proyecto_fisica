from manim import *
from proyecto import solution, t, presas, depredadores
import proyecto as p
template = TexTemplate()
template.add_to_preamble(r"\usepackage{amsmath}")

# Set the custom template in the config
config.tex_template = template
dt = 0.1
presas_lotka, depredadores_lotka = solution.T


def update(frame):
            global t, presas, depredadores, cantidad_presas, cantidad_depredadores
            presas[:] = [presa for presa in presas if presa.energia > 0]
            depredadores[:] = [depredadores for depredador in depredadores if depredador.energia > 0]
            print(f"Current Frame = {frame}, Depredadores type = {type(depredadores)}")
            cantidad_presas = int(presas_lotka[frame])
            cantidad_depredadores = int(depredadores_lotka[frame])

            #Ajustar la cantidad de presas y depredadores (viven o mueren)
            while len(presas) < cantidad_presas:
                presas.append(p.crear_presa())
            while len(presas) > cantidad_presas:
                presas.pop()

            while len(depredadores) < cantidad_depredadores:
                depredadores.append(p.crear_depredador())
            while len(depredadores) > cantidad_depredadores:
                depredadores.pop()
            for presa in presas:
                presa.cinematica(dt)
            
            presas_capturadas = [] 
            print(f"flag: {depredadores[0].pos}")
            for d in depredadores:
                print(d.energia)
            for depredador in depredadores:
                depredador.cinematica(dt)

                for presa in presas:
                    pos_presa = np.array(presa.pos)
                    pos_depredador = np.array(depredador.pos)
                    distancia = np.linalg.norm(pos_presa - pos_depredador)

                    if distancia < p.distancia_captura:
                        presas_capturadas.append(presa)
                        depredador.energia += 20
                    
                    elif distancia < p.distancia_umbral:
                        direccion_presecucion = (pos_presa - pos_depredador) / distancia
                        fuerza_aplicada = depredador.f * direccion_presecucion
                        aceleracion = fuerza_aplicada / depredador.maso

                        #Actualizar movimiento del depredador
                        depredador.vel = (
                            depredador.vel[0] + aceleracion[0] * dt,
                            depredador.vel[1] + aceleracion[1] * dt
                        )
            #Eliminar las presas cazadas
            for presa in presas_capturadas:
                if presa in presas:
                    presas.remove(presa)
            
            presas_coords = [presa.pos for presa in presas]
            depredadores_coords = [depredador.pos for depredador in depredadores]

            return presas_coords, depredadores_coords



for frame in range(len(t)):
    print(update(frame))