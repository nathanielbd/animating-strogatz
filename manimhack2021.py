from manim import *
# import requests

# url = 'https://en.wikipedia.org/wiki/Aleksandr_Lyapunov#/media/File:Alexander_Ljapunow_jung.jpg'

# r = requests.get(url)
# with open('lyapunov.jpg', 'wb') as f:
#   f.write(r.content)

class Lyapunov(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=DEGREES*0, theta=None, distance=None, gamma=None)
        text = Text(
            'Happy 164th birthday, Aleksandr Lyapunov!',
            t2c={
                '[5:8]': BLUE,
                '[19:36]': GREEN
            }
        ).move_to(2*UP)
        alex = ImageMobject('lyapunov.jpg').scale(2).move_to(DOWN)
        self.play(
            FadeInFrom(text),
            FadeInFrom(alex)
        )
        remem = Text(
            'We will remember you for'
        ).shift(3*LEFT).scale(0.75)
        self.wait(3)
        self.play(
            FadeOut(alex),
            Transform(text, remem)
        )
        ls = Text('Lyapunov stability', color=GREEN).next_to(remem, RIGHT).scale(0.75)
        self.play(
            FadeInFrom(ls)
        )
        self.play(
            FadeOut(ls)
        )
        le = Text('Lyapunov exponents', color=GREEN).next_to(remem, RIGHT).scale(0.75)
        self.play(
            FadeInFrom(le)
        )
        self.play(
            FadeOut(le)
        )
        lv = Text('Lyapunov vectors',   color=GREEN).next_to(remem, RIGHT).scale(0.75)
        self.play(
            FadeInFrom(lv)
        )
        self.play(
            FadeOut(lv)
        )
        lf = Text('Lyapunov functions', color=GREEN).next_to(remem, RIGHT).scale(0.75)
        self.play(
            FadeInFrom(lf)
        )
        self.wait(2)
        func = lambda pos: (pos[1]-pos[0]**3)*RIGHT + (-pos[0]-pos[1]**3)*UP
        scale = 4
        x_mag = 7.611111111111111/scale
        y_mag = 4.5/scale
        vdp = StreamLines(
            func, stroke_width=3,
            max_anchors_per_line=30,
            x_min=-x_mag, x_max=x_mag, x_delta=x_mag/scale,
            y_min=-y_mag, y_max=y_mag, y_delta=y_mag/scale
        ).scale(scale)
        way = Text(
            'a way of studying stability in dyanamical systems',
            t2c={
                '[14:23]': BLUE,
                '[25:]': GREEN
            }
        ).move_to(-2*DOWN).scale(0.5)
        self.play(
            FadeOut(text),
            FadeOut(lf),
            FadeInFrom(way)
        )
        self.add(vdp)
        vdp.start_animation()
        self.wait(5)
        res = 42
        parab = ParametricSurface(
            lambda x, y: np.array([x, y, 2 + 0.2*x**2 + 0.2*y**2]),
            resolution=(res, res),
            v_min=-8,
            v_max=+8,
            u_min=-8,
            u_max=+8
        )
        self.play(
            FadeOut(way)
        )
        self.move_camera(phi=DEGREES*65, run_time=3)
        text3d = Text(
            'using an energy landscape analogy',
            t2c={
                '[7:22]': GREEN
            }
        )
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(DL)
        self.play(
            FadeInFrom(text3d),
            Create(parab)
        )
        self.wait(3)

class DSImage(Scene):
    def construct(self):
        func = lambda pos: (pos[1]-pos[0]**3)*RIGHT + (-pos[0]-pos[1]**3)*UP
        scale = 4
        x_mag = 7.611111111111111/scale
        y_mag = 4.5/scale
        vdp = StreamLines(
            func, stroke_width=3,
            max_anchors_per_line=30,
            x_min=-x_mag, x_max=x_mag, x_delta=x_mag/scale,
            y_min=-y_mag, y_max=y_mag, y_delta=y_mag/scale
        ).scale(scale)
        text = MathTex(
            r'\frac{dx}{dt} = y - x^3 \\',
            r'\frac{dy}{dt} = -x -y^3'
        )
        text.to_corner(UL).shift(0.4*DOWN+0.4*LEFT)
        self.add(text)
        self.add(vdp)

class ParabImage(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        res = 42
        parab = ParametricSurface(
            lambda x, y: np.array([x, y, 0.2*x**2 + 0.2*y**2]),
            resolution=(res, res),
            v_min=-8,
            v_max=+8,
            u_min=-8,
            u_max=+8
        )
        axes = ThreeDAxes()
        text3d = MathTex(
            r'V = x^2 + y^2'
        )
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL).shift(DOWN)
        self.add(axes, parab)