import numpy as np
from manim import *

class AnimacaoParabola(Scene):
    def construct(self):
        eixos = Axes(
            x_range=[-2, 6, 1],
            y_range=[-2, 6, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_tip": True, "color": BLUE_B, "include_ticks": False},
        )

        labels = eixos.get_axis_labels(x_label="x", y_label="y")

        parabola = eixos.plot_parametric_curve(
            lambda u: np.array([((u + 1) ** 2) / 4, ((u - 1) ** 2) / 4, 0]),
            t_range=[-3, 3],
            color=PURPLE_A,
        )

        equacao = MathTex(
            "x^2 - 2xy + y^2 - 2x - 2y + 1 = 0", font_size=32, color=PURPLE_A
        ).to_corner(DR)

        self.play(Write(eixos), Write(labels))
        self.wait(0.5)
        self.play(Write(equacao))
        self.wait(1)

        self.play(Create(parabola), run_time=4, rate_func=smooth)
        self.wait(2)

        # 1. ROTAÇÃO (x1, y1)
        eixos_rotacionados = eixos.copy()
        labels_rotacionados = eixos_rotacionados.get_axis_labels(x_label="x_1", y_label="y_1").set_color(GREEN)
        sistema_rotacionado = VGroup(eixos_rotacionados, labels_rotacionados)
        
        
        legenda_eixos_rotacionados = Tex("Rotação de $\pi/4$", color=GREEN, font_size=30).to_corner(UR)

        self.play(Write(legenda_eixos_rotacionados))
        
        self.wait(2)

        self.play(
            sistema_rotacionado.animate.set_color(GREEN).rotate(
                45 * DEGREES, 
                about_point=eixos.c2p(0, 0)
            ),
            run_time=2.5
        )

        self.play(FadeOut(legenda_eixos_rotacionados))

        # 2. TRANSLAÇÃO (x2, y2)
        ponto_destino = eixos_rotacionados.c2p(1/(2*np.sqrt(2)), 0)
        ponto_origem_verde = eixos_rotacionados.c2p(0, 0)
        vetor_deslocamento = ponto_destino - ponto_origem_verde
        
        eixos_finais = eixos_rotacionados.copy()
        # Criamos os novos labels x2 e y2
        labels_finais = eixos_finais.get_axis_labels(x_label="x_2", y_label="y_2").set_color(RED)
        
        # Agrupamos para transladar os eixos e os labels novos juntos
        sistema_final = VGroup(eixos_finais, labels_finais)
        
        legenda_translacao = Tex(
            "Translação: $x_2 = x_1 - 1/2\\sqrt{2}, y_2 = y_1$", 
            color=RED, 
            font_size=30
        ).to_corner(UR)

        self.play(Write(legenda_translacao))

        self.play(
            sistema_final.animate.set_color(RED).shift(vetor_deslocamento),
            run_time=3
        )
        
        self.wait(3)