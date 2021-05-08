from manim import *


class Arithmetic(Scene):
    def construct(self):
        lines = VGroup(
            MathTex("0", "+", "{1}", "+", "2", "+", "...", "+", "98", "+", "99", "+", "100"),
            MathTex("=", "(", "0", "+", "100", ")", "+", "(", "{1}", "+", "99", ")", "+", "(", "2", "+", "98", ")", "+",
                    "...", "+", "(", "48", "+", "52", ")", "+", "(", "49", "+", "51", ")", "+", "50")

        ).move_to(UP * 3).scale(0.83)
        lines.arrange(DOWN, buff=3, center=False)
        play_kw = {"run_time": 2}
        colors = {
            "+": YELLOW_B,
            "(": BLUE_E,
            ")": BLUE_E,
        }
        for i in colors:
            lines[1].get_parts_by_tex(i).set_color(colors[i])
        self.play(Write(lines[0]), **play_kw)
        self.play(Write(lines[1].get_parts_by_tex("=")))
        self.play(*[Write(lines[1].get_parts_by_tex(tex))
                    for tex in ["(", ")", "..."]
                    ])
        self.play(Write(lines[1].get_parts_by_tex("+")))
        straight_lines = VGroup(
            *[Line(lines[0].get_part_by_tex(tex).get_bottom(),
                   lines[1].get_part_by_tex(tex).get_center())
              for tex in ["0", "100", "{1}", "99", "2", "98"]

              ] + [Line(lines[0].get_part_by_tex("...").get_bottom(),
                        lines[1].get_part_by_tex(tex).get_center())
                   for tex in ["48", "52", "49", "51", "50"]
                   ]).set_opacity(1.0).set_color(RED)

        j = ["0", "100", "{1}", "99", "2", "98", "48", "52", "49", "51", "50"]

        temp = VGroup(*[
            MathTex(tex).scale(0.83)
            for tex in j
        ])
        copies = lines[0].copy()
        for i in range(0, 6, 2):
            self.play(*[ShowCreationThenDestruction(straight_lines[i]),
                        ShowCreationThenDestruction(straight_lines[i + 1])], **play_kw)
            self.play(*[MoveAlongPath(copies.get_part_by_tex(j[i]), straight_lines[i]),
                        MoveAlongPath(copies.get_part_by_tex(j[i + 1]), straight_lines[i + 1])])
        for i in range(6, 10, 2):
            self.play(*[ShowCreationThenDestruction(straight_lines[i]),
                        ShowCreationThenDestruction(straight_lines[i + 1])], **play_kw)
            self.play(*[MoveAlongPath(temp[i], straight_lines[i]),
                        MoveAlongPath(temp[i + 1], straight_lines[i + 1]),
                        ])

        self.play(MoveAlongPath(temp[-1].set_color(YELLOW_D), straight_lines[-1]))

        braces = VGroup(*[Brace(lines[1][1 + i:6 + i])
                          for i in range(0, 18, 6)]
                         + [
                             Brace(lines[1][18:21])
                         ]
                         + [
                             Brace(lines[1][1 + i:6 + i])
                             for i in range(20, len(lines[1]) - 2, 6)
                         ]).set_color(BLUE)

        under_text = VGroup(*[
                                 Tex("100").scale(0.83).move_to(braces[i].get_bottom() + DOWN / 6)
                                 for i in range(0, 3)
                             ] + [Tex("...").scale(0.83).move_to(braces[3].get_bottom() + DOWN / 6)] +
                             [Tex("100").scale(0.83).move_to(braces[i].get_bottom() + DOWN / 6)
                              for i in range(4, len(braces))]
                            ).set_color(RED_E)
        for i in range(len(braces)):
            self.play(FadeInFrom(braces[i], UP))
            if i == 3:
                self.play(Write(under_text[3]))
            else:
                self.play(FadeInFrom(under_text[i], UP))

        bigbrace = Brace(lines[1][1:len(lines[1])])
        _50times = MathTex("50", "\\times", "100", "+", "50").set_color(BLUE_A).move_to(
            bigbrace.get_bottom() + DOWN / 4)
        _50times[-1].set_color(YELLOW_D)
        _50times[0].set_color(YELLOW_D)
        _50times[2].set_color(BLUE)

        self.play(Transform(braces, bigbrace))
        self.play(Transform(under_text, _50times))
        numericals = VGroup(
            MathTex("\\sum^{n}_{k=0} k = "),
            MathTex("{n\\over2}", "\\times", "n", "+", "{n\\over2}"),
            MathTex("n", "(", "n", "+", "1", ") \\over 2")

        )
        numericals.arrange(RIGHT, buff=-1)
        numericals[1].get_parts_by_tex("{n\\over2}").set_color(YELLOW_D)
        numericals[1].get_part_by_tex("n").set_color(BLUE)
        bigbrace.add(lines, braces, temp, copies)
        self.play(FadeOutAndShift(bigbrace, RIGHT))
        self.clear()
        self.play(ApplyMethod(_50times.move_to, ORIGIN))
        self.play(ReplacementTransform(_50times, numericals[1]), **play_kw)
        self.play(ReplacementTransform(numericals[1], numericals[2]), **play_kw)
        self.play(GrowFromCenter(numericals[0]))
        self.wait()