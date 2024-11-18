from manim import *
from proyecto import solution, t

template = TexTemplate()
template.add_to_preamble(r"\usepackage{amsmath}")

# Set the custom template in the config
config.tex_template = template



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
