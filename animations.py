from manim import *
from proyecto import solution, t
class LotkaVolterra(Scene):
    def construct(self):
        presas_lotka, depredadores_lotka = solution.T
        presas_points = list(zip(t,presas_lotka))
        depredadores_points = list(zip(t,depredadores_lotka))

        title = Text("Lotka-Volterra", font_size= 72, color = RED).shift(UP * 0.4)
        subtitle = Text("Presas y Depredadores").shift(DOWN * 0.4)

        ax = always_redraw(lambda :
            Axes(
                x_range = [0,200,20], 
                y_range= [0,max(max(presas_lotka),max(depredadores_lotka)),2]))
        
        labels = ax.get_axis_labels(x_label = "Tiempo",y_label = "Poblacion")
        self.play(Write(title),Write(subtitle))
        self.wait(3)

        #self.add(ax)
        self.play(FadeOut(subtitle))
        self.wait(0.5)
        self.play(
            Transform(title, ax),
        )
        self.play(Write(labels))

        self.wait(2)
        self.remove(title)
        self.play(ax.animate.scale(0.5))