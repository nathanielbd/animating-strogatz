from manim import *
# from manim_onlinetex import *


class Intro(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        strogatz = ImageMobject('strogatz.jpg')
        book = ImageMobject('book.png').move_to(7*RIGHT)
        book_border = SurroundingRectangle(book, color=WHITE)
        self.play(
                FadeInFrom(strogatz)
        )
        self.play(
                self.camera.frame.animate.move_to(3.5*RIGHT)
        )
        self.play(
                FadeInFrom(book),
                DrawBorderThenFill(book_border)
        )
        self.play(
                FadeOutAndShift(strogatz, direction=3.5*RIGHT),
                FadeOutAndShift(book, direction=3.5*LEFT),
                FadeOutAndShift(book_border, direction=3.5*LEFT)
        )

class Equations(Scene):
    def construct(self):
        eqs = MathTex(
                r'\frac{dx}{dt} = ', r'\dot x &= ', r'x(3-x-2y)\\',
                r'\frac{dy}{dt} = ', r'\dot y &= ', r'y(2-x- y)  '
        )
        nopl = NumberPlane()
        self.add(nopl, eqs)
        self.play(
                FadeOut(nopl),
                FadeOut(eqs)
        )
        self.play(Write(eqs))
        self.play(
                Transform(eqs, eqs.copy().to_corner(UP + LEFT)),
                Create(nopl)
        )
        pt = np.array([1, 2, 0])
        dot = Dot(pt)
        dot_label = MathTex(r'(x, y) = (1, 2)').next_to(dot, RIGHT)
        self.play(
                Create(dot),
                Create(dot_label)
        )
        xdot_box = SurroundingRectangle(eqs[1])
        xeq_box = SurroundingRectangle(eqs[2])
        ydot_box = SurroundingRectangle(eqs[4])
        yeq_box = SurroundingRectangle(eqs[5])
        self.play(
                Create(xdot_box)
        )
        self.play(
                Transform(xdot_box, xeq_box)
        )
        xdot_arr = Arrow(pt, pt+[-2, 0, 0], color=YELLOW, buff=0)
        ydot_arr = Arrow(pt, pt+[0, -2, 0], color=YELLOW, buff=0)
        both_arr = Arrow(pt, pt+[-2, -2, 0], buff=0)
        self.play(
                Transform(xdot_box, xdot_arr)
        )
        self.play(
                Create(ydot_box)
        )
        self.play(
                Transform(ydot_box, yeq_box)
        )
        self.play(
                Transform(ydot_box, ydot_arr)
        )
        self.play(
                Transform(xdot_box, Arrow(pt+[0, -2, 0], pt+[-2, -2, 0], color=YELLOW, buff=0))
        )
        self.play(
                Uncreate(xdot_box),
                Uncreate(ydot_box),
                Create(both_arr)
        )

class Index(Scene):
    def construct(self):
        cc = SVGMobject('small.svg')
        self.play(
                GrowFromCenter(cc)
        )
        self.play(
                Transform(cc, SVGMobject('large.svg'))
        )
        self.play(
                Transform(cc, SVGMobject('smooth.svg'))
        )
        self.play(
                Transform(cc, SVGMobject('squiggly.svg'))
        )
        self.play(
                Transform(cc, SVGMobject('smooth.svg'))
        )

class VFTest(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        vf = VectorField(
                lambda x: np.array([x[0]*(3-x[0]-2*x[1]), x[1]*(2-x[0]-x[1])]),
                # delta_x=0.25,
                # delta_y=0.25,
                # max_magnitude=4
        )
        self.play(*[GrowArrow(vec) for vec in vf])
        self.play(self.camera.frame.animate.scale(0.5).move_to(2*RIGHT+UP))

import numpy as np
from svg.path import parse_path

class SVGPath(VMobject):
    def __init__(self, path_str, *, num_points=500, **kwargs):
        self.path       = parse_path(path_str)
        self.num_points = num_points

        super().__init__(**kwargs)

    def point(self, alpha):
        z = self.path.point(alpha)

        return np.array([z.real, z.imag, 0])

    def generate_points(self):
        step = 1 / self.num_points

        points = [self.point(x) for x in np.arange(0, 1, step)]
        self.start_new_path(points[0])
        self.add_points_as_corners(points[1:])
        self.add_line_to(self.point(1))

        self.flip(RIGHT)
        self.center()

        return self

class SVGTest(Scene):
    def construct(self):
        path_str = 'M 48.888817529296716, 24.204346609310242   C  49.57987066262637, 21.661620923350178 42.064873983475884, 25.442397805331748 40.87161356549331, 27.79168236068086   37.17826292334656, 35.06313081428308 26.29744757503994, 57.35665515183989 33.74184402740781, 54.025624824867066   42.90101303628617, 49.92731142449206 46.25719663384159, 33.887379250146225 48.888817529296716, 24.204346609310242   Z'
        path = SVGPath(path_str).scale(0.2)
        self.add(path)
        dot = Dot()
        def get_arrow():
                x = dot.get_center()[0]
                y = dot.get_center()[1]
                vec = np.array([x*(3-x-2*y), y*(2-x-y), 0])
                vec = vec/np.linalg.norm(vec, ord=2)
                return Arrow(dot.get_center(), dot.get_center()+vec, buff=0)
        arr = always_redraw(get_arrow)
        # dot.add_updater()
        self.add(arr)
        self.play(
                MoveAlongPath(dot, path), run_time=4, rate_func=linear
        )

class StreamLineTest(Scene):
    def construct(self):
        # func = lambda pos: np.sin(pos[0]/2)*UR+np.cos(pos[1]/2)*LEFT
        func = lambda x: np.array([x[0]*(3-x[0]-2*x[1]), x[1]*(2-x[0]-x[1])])
        stream_lines = StreamLines(
            func, max_anchors_per_line=30,
            opacity=0.8, delta_x=0.1, delta_y=0.1,
            max_color_scheme_value=2.5
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False)
        self.wait(stream_lines.virtual_time)