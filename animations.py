from manim import *
from proyecto import solution, t, presas, depredadores
import proyecto as p
template = TexTemplate()
template.add_to_preamble(r"\usepackage{amsmath}")

# Set the custom template in the config
config.tex_template = template
dt = 0.1
presas_lotka, depredadores_lotka = solution.T

class LotkaVolterra1(Scene):
    def construct(self):
        title = Text("Lotka-Volterra", font_size= 72, color = RED).shift(UP * 0.4)
        subtitle = Text("Presas y Depredadores").shift(DOWN * 0.4)

        self.play(Write(title))
        self.play(Write(subtitle))

class LotkaVolterra2(Scene):
    def construct(self):
        title = Text("Lotka-Volterra", font_size= 72, color = RED).shift(UP * 0.4)
        subtitle = Text("Presas y Depredadores").shift(DOWN * 0.4)

        self.add(title)
        self.add(subtitle)
        self.play(FadeOut(title),FadeOut(subtitle))

class Equations(Scene):
    def construct(self):
        
        eq_presas = MathTex(r"\frac{dx}{dt} = \alpha x - \beta xy")
        eq_depred = MathTex(r"\frac{dy}{dt} = \delta xy - \gamma y")
        eq_presas.shift(UP * 1)
        eq_depred.next_to(eq_presas, DOWN * 3)

        equations = VGroup(eq_presas,eq_depred)
        equations.shift(RIGHT * 4)

        presas = Tex("Ecuación para presas")
        presas.set_color(BLUE)
        presas.shift(UP * 1)
        depredadores = Tex("Ecuación para depredadores")
        depredadores.set_color(RED)
        depredadores.next_to(presas, DOWN * 5)

        eq_desc = VGroup(presas,depredadores)
        


        self.play(Write(presas))
        self.play(presas.animate.shift(LEFT*3))
        self.play(Write(eq_presas))
        #agregar primera flecha


        self.play(Write(depredadores))
        self.play(depredadores.animate.shift(LEFT * 3))
        self.play(Write(eq_depred))
        #agregar segunda flecha
        
        flecha_presa = Arrow(start = presas.get_edge_center(RIGHT), end = eq_presas.get_edge_center(LEFT))
        flecha_depredadores = Arrow(start = depredadores.get_edge_center(RIGHT), end = eq_depred.get_edge_center(LEFT))

        
        self.play(eq_presas.animate.set_color(BLUE),Create(flecha_presa), run_time = 2)
        self.play(eq_depred.animate.set_color(RED),Create(flecha_depredadores), run_time = 3)
        self.wait(1)

        #self.play(FadeOut(eq_desc,eq_depred,eq_presas,flecha_depredadores,flecha_presa))

class Intermediate(Scene):
    def construct(self):
        eq_presas = MathTex(r"\frac{dx}{dt} = \alpha x - \beta xy")
        eq_presas.set_color(BLUE)
        eq_depred = MathTex(r"\frac{dy}{dt} = \delta xy - \gamma y")
        eq_depred.set_color(RED)
        eq_presas.shift(UP * 1)
        eq_depred.next_to(eq_presas, DOWN * 3)
        equations = VGroup(eq_presas,eq_depred)
        equations.shift(RIGHT * 4)
        presas = Tex("Ecuación para presas")
        presas.set_color(BLUE)
        presas.shift(UP * 1)
        depredadores = Tex("Ecuación para depredadores")
        depredadores.set_color(RED)
        texto = VGroup(presas,depredadores)
        texto.shift(LEFT * 3)
        depredadores.next_to(presas, DOWN * 5)
        flecha_presa = Arrow(start = presas.get_edge_center(RIGHT), end = eq_presas.get_edge_center(LEFT))
        flecha_depredadores = Arrow(start = depredadores.get_edge_center(RIGHT), end = eq_depred.get_edge_center(LEFT))

        eq_desc = VGroup(presas,depredadores)    
        self.add(eq_presas,eq_depred, eq_desc, flecha_depredadores, flecha_presa)
        self.play(FadeOut(texto),FadeOut(flecha_depredadores),FadeOut(flecha_presa))

class Equations2(Scene):
    def construct(self):
        eq_presas = MathTex(r"\frac{dx}{dt} = \alpha x - \beta xy")
        eq_presas.set_color(BLUE)
        eq_depred = MathTex(r"\frac{dy}{dt} = \delta xy - \gamma y")
        eq_depred.set_color(RED)
        eq_presas.shift(UP * 1)
        eq_depred.next_to(eq_presas, DOWN * 3)

        equations = VGroup(eq_presas,eq_depred)
        equations.shift(RIGHT * 4)

        self.add(equations)
        self.play(eq_presas.animate.move_to(ORIGIN), FadeOut(eq_depred), run_time=4)
        self.play(eq_presas.animate.shift(LEFT * 5))
        self.play(eq_presas.animate.set_color(WHITE))

        #Descripción eq 1
        x = Tex("x: Número de presas")
        alpha = MathTex(r"\alpha")
        alpha_d = Tex(": Tasa de crecimiento de las presas")
        alpha_d.next_to(alpha, RIGHT)
        alphas = VGroup(alpha,alpha_d)
        alphas.next_to(x, DOWN)
        beta = MathTex(r"\beta")
        beta_d = Tex(": éxito en la caza del depredador")
        beta_d.next_to(beta, RIGHT)
        betas = VGroup(beta,beta_d)
        betas.next_to(alphas, DOWN)
        y = Tex("y: Número de depredadores")
        y.next_to(betas,DOWN)
        descriptions = VGroup(
            x,alpha,alpha_d,beta,beta_d,y
        )
        descriptions.shift(RIGHT * 2)
        descriptions.shift(UP * 1)
       
        self.play(Write(descriptions), run_time = 5)
  
class Equations3(Scene):
    def construct(self):
        eq_presas = MathTex(r"\frac{dx}{dt} = \alpha x - \beta xy")
        eq_presas.shift(LEFT*5)
        self.add(eq_presas)

        x = Tex("x: Número de presas")
        alpha = MathTex(r"\alpha")
        alpha_d = Tex(": Tasa de crecimiento de las presas")
        alpha_d.next_to(alpha, RIGHT)
        alphas = VGroup(alpha,alpha_d)
        alphas.next_to(x, DOWN)
        beta = MathTex(r"\beta")
        beta_d = Tex(": éxito en la caza del depredador")
        beta_d.next_to(beta, RIGHT)
        betas = VGroup(beta,beta_d)
        betas.next_to(alphas, DOWN)
        y = Tex("y: Número de depredadores")
        y.next_to(betas,DOWN)
        descriptions = VGroup(
            x,alpha,alpha_d,beta,beta_d,y
        )
        descriptions.shift(RIGHT * 2)
        descriptions.shift(UP * 1)

        self.add(descriptions)

        self.play(FadeOut(eq_presas),FadeOut(descriptions))
        self.wait(1)

        eq_depred = MathTex(r"\frac{dy}{dt} = \delta xy - \gamma y")
        eq_depred.shift(LEFT * 5)
        self.play(Write(eq_depred))

        delta = MathTex(r"\delta")
        delta_d = Tex(": Éxito en la caza del depredador")
        delta_d.next_to(delta,RIGHT)
        deltas = VGroup(delta,delta_d)
        gamma = MathTex(r"\gamma")
        gamma_d = Tex(": Tasa de crecimiento del depredador")
        gamma_d.next_to(gamma,RIGHT)
        gammas = VGroup(gamma,gamma_d)
        gammas.next_to(deltas,DOWN)

        desc = VGroup(deltas,gammas)
        desc.shift(LEFT*1)
        desc.shift(UP*0.5)
        self.play(Write(desc))

        self.next_section("Part 1")

        self.play(FadeOut(eq_depred),FadeOut(desc))
        
class Curves(MovingCameraScene):
    def construct(self):
        presas_lotka, depredadores_lotka = solution.T
        presas_points = list(zip(t,presas_lotka))
        depredadores_points = list(zip(t,depredadores_lotka))

        ax = Axes(
                x_range = [0,200,20], 
                y_range= [0,max(max(presas_lotka),max(depredadores_lotka)),4],
                x_length= 10,
                y_length= 10,
                axis_config={"include_numbers": True}
                )
        
        labels = ax.get_axis_labels(x_label = "Tiempo",y_label = Tex("Población"))
        labels[1].shift(UP * 2)
        labels[0].shift(DOWN *2)
        
        depredadores_curve = VMobject()
        depredadores_curve.set_points_smoothly([ax.coords_to_point(x,y) for x,y in depredadores_points])
        depredadores_curve.set_color(RED)

        presas_curve = VMobject()
        presas_curve.set_points_smoothly([ax.coords_to_point(x,y) for x,y in presas_points])
        presas_curve.set_color(BLUE)

        ax_group = VGroup(ax,labels,presas_curve,depredadores_curve)

        #Parámetros:
        alpha = MathTex(r"\alpha = 0.3")
        alpha.shift(UP * 1)
        beta = MathTex(r"\beta = 0.02")
        beta.next_to(alpha, DOWN)
        delta = MathTex(r"\delta = 0.01")
        delta.next_to(beta, DOWN)
        gamma = MathTex(r"\gamma = 0.1")
        gamma.next_to(delta, DOWN)

        """alpha = 0.3  # Tasa de crecimiento de las presas
        beta = 0.02  # Tasa de depredación
        delta = 0.01 # Eficiencia de conversión de una presa a depredador
        gamma = 0.1  # Tasa de mortalidad de los depredadores 
        numero_de_p = 40  # Número inicial de presas
        numero_de_d = 20 """
        #iniciación de la cámara
        self.play(self.camera.frame.animate.scale(1.5))

        title = Text("Parámetros del sistema: ")
        self.play(Write(title))
        self.play(title.animate.shift(UP * 2))
        
        parameters = VGroup(alpha, beta, delta, gamma)
        self.play(Write(parameters), run_time = 5)
        self.wait(2)
        data = VGroup(title, parameters)
        self.play(data.animate.shift(RIGHT*7))

        #crear ejes
        ax_group.shift(LEFT * 4)
        #self.play(Create(ax))
        self.play(Transform(parameters,ax))
        self.play(Write(labels))

        leyenda_p = Text("Presas")
        leyenda_p.set_color(BLUE)
        
        leyenda_p.shift(RIGHT * 5)

        leyenda_d = Text("Depredadores")
        leyenda_d.set_color(RED)
        leyenda_d.next_to(leyenda_p, DOWN)
        self.play(FadeOut(title))
        self.play(Write(leyenda_p),Write(leyenda_d))
        self.play(Create(presas_curve), Create(depredadores_curve), run_time = 20)

class SpaceSimulation(Scene):
    def construct(self):
        background = NumberPlane(
            x_range = [-10,10,1],
            y_range = [-10,10,1],
            background_line_style={
                "stroke_opacity":0.3
            },
            axis_config={
                "include_numbers":True
            }
        )
        #self.add(background)

        edges = Square(side_length= 5)
        grid = NumberPlane(
            x_range= [0,100,20],
            y_range= [0,100,20],
            x_length= 5,
            y_length= 5,
            axis_config = {
                "include_numbers":True,
                "font_size":24
            },
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0,
            }
        )
        #grid.shift(ORIGIN + grid.get_center())
        #grid.move_to(edges.get_center())
        #grid.shift(RIGHT * 0.4)
        """grid.x_axis.set_opacity(0)  # Entire x-axis
        grid.y_axis.set_opacity(0)"""
        #edges.move_to(grid.get_center())
        grid.shift(ORIGIN - grid.get_center())
    
        # Create a border around the grid
        edges.move_to(grid.get_center())
        edges.shift(LEFT*0.2)
        edges.shift(UP*0.12)

        
        #Duración de la simulación espacial
        total_duration = 20

        #Creación de puntos 
        presas_dots = VGroup()
        depredadores_dots = VGroup()

        for presa in presas:
            dot = Dot(color = BLUE,radius = 0.05).move_to(grid.c2p(presa.pos[0],presa.pos[1]))
            presas_dots.add(dot)
        
        for depredador in depredadores:
            dot = Dot(color = RED, radius = 0.05).move_to(grid.c2p(depredador.pos[0],depredador.pos[1]))
            depredadores_dots.add(dot)
        
        Space = VGroup(edges,grid,presas_dots,depredadores_dots)
        Space.shift(LEFT * 2)
        self.play(Create(Space))
        """for dot in presas_dots:
            self.play(FadeIn(dot), run_time = 0.1)
        for dot in depredadores_dots:
            self.play(FadeIn(dot), run_time = 0.1)"""
        #self.play(FadeIn(presas_dots))
        #self.play(FadeIn(depredadores_dots))
        self.wait(2)


        #Definición función de actualización de puntos
        def update(frame):
            global t, presas, depredadores, cantidad_presas, cantidad_depredadores
            presas[:] = [presa for presa in presas if presa.energia > 0]
            depredadores[:] = [depredador for depredador in depredadores if depredador.energia > 0]

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
                        aceleracion = fuerza_aplicada / depredador.masa

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

        update(0)
        #Iniciar Texto de contador
        contador_p = Text(f"Cantidad de Presas: {cantidad_presas}", font_size= 24)
        contador_d = Text(f"Cantidad de Depredadores: {cantidad_depredadores}", font_size= 24)
        contador_d.next_to(contador_p,DOWN)
        contadores = VGroup(contador_p,contador_d)
        contadores.shift(RIGHT * 4)
        self.play(FadeIn(contadores))
