import numpy as np
from manim import *


class AnimacaoParabola(Scene):
    def construct(self):
        eixos = Axes(
            x_range=[-2, 6, 1],
            y_range=[-2, 6, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_tip": True, "color": BLUE_B},
        ).add_coordinates()

        labels = eixos.get_axis_labels(x_label="x", y_label="y")

        # A forma paramétrica garante que a curva toque exatamente (1,0) e (0,1)
        # x = (u+1)^2 / 4 , y = (u-1)^2 / 4
        parabola = eixos.plot_parametric_curve(
            lambda u: np.array([((u + 1) ** 2) / 4, ((u - 1) ** 2) / 4, 0]),
            t_range=[-3, 5],  # Ajuste do comprimento da parábola
            color=PURPLE_A,
        )

        titulo = Tex("Animação de Cônica: Parábola", font_size=36).to_edge(UP, buff=0.3)
        equacao = MathTex(
            "x^2 - 2xy + y^2 - 2x - 2y + 1 = 0", font_size=32, color=PURPLE_A
        ).next_to(titulo, DOWN, buff=0.2)

        self.play(Write(eixos), Write(labels))
        self.play(FadeIn(titulo, shift=UP))
        self.wait(0.5)
        self.play(Write(equacao))
        self.wait(1)

        self.play(Create(parabola), run_time=4, rate_func=smooth)

        self.wait(3)

        dot_x = Dot(eixos.c2p(1, 0), color=YELLOW)
        dot_y = Dot(eixos.c2p(0, 1), color=YELLOW)
        self.play(FadeIn(dot_x), FadeIn(dot_y))
        self.play(Indicate(dot_x), Indicate(dot_y))
        
        eixos_novos = eixos.copy()
        
        self.play(
            eixos_novos.animate.set_color(GREEN).rotate(
                45 * DEGREES, 
                about_point=eixos.c2p(0, 0)
            ),
            run_time=2.5
        )
        
        legenda_eixos = Tex("Eixos Rotacionados ($45^\circ$)", color=GREEN, font_size=30).to_corner(UR)
        self.play(Write(legenda_eixos))
