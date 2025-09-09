from manim import *

class Escena0(Scene):
    def construct(self):
        obj_0 = MathTex("\int_0^1 x^2 dx").move_to([0, 0, 0]).set_color(BLUE)
        self.play(FadeIn(obj_0), run_time=2.0)


