"""~40 s explainer for the public notebook (Manim Community). Every number is from the evidence files:
public 0.958 count (public LB csv), private 0.942 block ranks 584-1880 after the re-rank (private_lb_score_blocks_20261027.txt),
gold-58 0.9384 / 0.9419 (strict_variants_gold.txt), private 0.943 / 0.942 and rank 478 of 6,299 (Kaggle leaderboard API, final standings).
Render: manim -qm --format mp4 explainer_video.py Explainer"""
from manim import *

BG, INK, MUTED, GREY, ORANGE = "#fcfcfb", "#1b1b1a", "#6b6a66", "#c9c7bf", "#d9622b"
config.background_color = BG
FONT = "Arial"


def T(s, size=30, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


class Explainer(Scene):
    def construct(self):
        # 1. title
        title = T("478th of 6,299: a lower public score that finished higher", 33, weight=BOLD)
        sub = T("RSNA Knee Abnormality Detection · bronze · final leaderboard", 26, MUTED).next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(title, shift=UP * 0.2), FadeIn(sub), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(sub))

        # 2. public board
        head = T("Public leaderboard", 34, weight=BOLD).to_edge(UP, buff=0.6)
        block = RoundedRectangle(corner_radius=0.15, width=7.5, height=1.3, fill_color=GREY, fill_opacity=1,
                                 stroke_width=0).shift(UP * 0.6)
        btxt = T("1,638 teams at public 0.958", 30).move_to(block)
        ours = Dot(radius=0.16, color=ORANGE).shift(DOWN * 1.4 + LEFT * 2.2)
        otxt = T("our variant: 0.957", 28, ORANGE).next_to(ours, RIGHT, buff=0.3)
        note = T("Every variant we submitted showed 0.957, one step below.", 24, MUTED)
        note.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(head), GrowFromCenter(block), Write(btxt), run_time=1.5)
        self.play(FadeIn(ours, scale=0.5), FadeIn(otxt), run_time=1)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3)
        self.play(*[FadeOut(m) for m in (head, block, btxt, ours, otxt, note)])

        # 3. gold-58
        head = T("So we chose on gold-58", 34, weight=BOLD).to_edge(UP, buff=0.6)
        expl = T("58 training studies with all 12 findings labelled, full pipeline run on their DICOMs", 24, MUTED)
        expl.next_to(head, DOWN, buff=0.3)
        base_y = -2.2
        scale = 60  # bar height per AUC unit above 0.90
        vals = [("0.958 notebook, unchanged", 0.9384, GREY), ("our variant", 0.9419, ORANGE)]
        bars, labels = VGroup(), VGroup()
        for i, (name, v, col) in enumerate(vals):
            h = (v - 0.90) * scale
            bar = Rectangle(width=2.2, height=h, fill_color=col, fill_opacity=1, stroke_width=0)
            bar.move_to([(-2.2 if i == 0 else 2.2), base_y + h / 2, 0])
            val = T(f"{v:.4f}", 30, INK if i == 0 else ORANGE, BOLD).next_to(bar, UP, buff=0.15)
            lab = T(name, 24, MUTED).next_to(bar, DOWN, buff=0.2)
            bars.add(bar); labels.add(VGroup(val, lab))
        axis = Line([-4.5, base_y, 0], [4.5, base_y, 0], color=GREY, stroke_width=2)
        cav = T("Bars start at AUC 0.90. Reused many times, so a direction to bet on, not a guarantee.", 22, MUTED).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(head), FadeIn(expl), Create(axis), run_time=1)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=1.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.8)
        self.play(FadeIn(cav))
        self.wait(3)
        self.play(*[FadeOut(m) for m in (head, expl, axis, bars, labels, cav)])

        # 4. private board
        head = T("Private leaderboard", 34, weight=BOLD).to_edge(UP, buff=0.6)
        block = RoundedRectangle(corner_radius=0.15, width=7.5, height=1.3, fill_color=GREY, fill_opacity=1,
                                 stroke_width=0).shift(DOWN * 0.6)
        btxt = T("ranks 584 to 1,880: all 0.942", 30).move_to(block)
        ctrl = T("(our unchanged copy of the 0.958 notebook: 0.942)", 22, MUTED).next_to(block, DOWN, buff=0.25)
        ours = Dot(radius=0.16, color=ORANGE).move_to(block.get_center() + DOWN * 2.2 + LEFT * 2.2)
        self.play(FadeIn(head), GrowFromCenter(block), Write(btxt), run_time=1.5)
        self.play(FadeIn(ctrl), FadeIn(ours, scale=0.5))
        target = block.get_top() + UP * 1.1 + LEFT * 2.2
        self.play(ours.animate.move_to(target), run_time=1.6, rate_func=smooth)
        otxt = T("our variant: 478th, private 0.943", 30, ORANGE, BOLD).next_to(ours, RIGHT, buff=0.3)
        self.play(FadeIn(otxt))
        self.wait(3)
        self.play(*[FadeOut(m) for m in (head, block, btxt, ctrl, ours, otxt)])

        # 5. credits
        c1 = T("Two changes on top of public work:", 30, weight=BOLD)
        c2 = T("new Raptor weights for 3 findings · our retrained reader at 0.1", 26, ORANGE)
        c3 = T("Built on goodpjw, heliosli, nartaa, sujanmajhisuzan, varshithakolupuri,", 22, MUTED)
        c4 = T("Dread Development, rostigor, rabari9999 and the label authors. Thank you.", 22, MUTED)
        g = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.35)
        self.play(FadeIn(g, shift=UP * 0.2), run_time=1.2)
        self.wait(4)
