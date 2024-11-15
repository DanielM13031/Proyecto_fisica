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

        ax = Axes(
                x_range = [0,200,20], 
                y_range= [0,max(max(presas_lotka),max(depredadores_lotka)),2],
                x_length= 5,
                y_length= 5
                )
        
        
        labels = ax.get_axis_labels(x_label = "Tiempo",y_label = "Poblaci\'{o}n")

        ax_group = VGroup(ax,labels)    

        ax_group.shift(LEFT * 5)    
        depredadores_curve = VMobject()
        depredadores_curve.set_points_smoothly([ax.coords_to_point(x,y) for x,y in depredadores_points])
        depredadores_curve.set_color(RED)

        presas_curve = VMobject()
        presas_curve.set_points_smoothly([ax.coords_to_point(x,y) for x,y in presas_points])
        presas_curve.set_color(BLUE)

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
        self.play(Create(depredadores_curve), Create(presas_curve), run_time = 20)
        
        #self.play(ax.animate.scale(0.5).move_to([-5,0,0]))
        self.wait(0.5)
        #self.play(ax.animate.move_to([-5,0,0]))