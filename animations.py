from manim import *
from proyecto import solution, t
class LotkaVolterra(Scene):
    def construct(self):
        presas_lotka, depredadores_lotka = solution.T
        presas_points = list(zip(t,presas_lotka))
        depredadores_points = list(zip(t,presas_lotka))
