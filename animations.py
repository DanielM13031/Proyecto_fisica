from manim import *
from proyecto import solution, t

template = TexTemplate()
template.add_to_preamble(r"\usepackage{amsmath}")

# Set the custom template in the config
config.tex_template = template

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
                y_range= [0,max(max(presas_lotka),max(depredadores_lotka)),2],
                x_length= 5,
                y_length= 5
                ))
        
        
        labels = ax.get_axis_labels(x_label = "Tiempo",y_label = "Poblaci\'{o}n")

        depredadores_plot = ax.plot_line_graph(
            x_values = t,
            y_values = presas_lotka,
            line_color = RED,

        )
        self.play(Write(title),Write(subtitle))
        self.wait(3)

        #self.add(ax)
        self.play(FadeOut(subtitle))
        self.wait(0.5)
        self.play(
            Transform(title, ax),
        )

        self.wait(2)
        self.play(Write(labels))
        self.wait(2)
        #self.play(FadeOut(labels))
        self.remove(title)
        self.add(ax)
        self.play(Create(depredadores_plot))
        #self.play(ax.animate.scale(0.5).move_to([-5,0,0]))
        self.wait(0.5)
        #self.play(ax.animate.move_to([-5,0,0]))