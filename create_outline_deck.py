"""
Build 13-slide deck from Lavanya's outline.
Output: Modelling_Information_Spread_Presentation.pptx
"""
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

import build_presentation_pptx as bp
from presentation_notes_data import SLIDE_NOTES

OUT_PATH = bp.BASE_DIR / "Modelling_Information_Spread_Presentation.pptx"

ACCENT = RGBColor(34, 64, 121)
TEXT = RGBColor(32, 39, 49)
MUTED = RGBColor(90, 98, 110)


def add_bg(slide, rgb=(248, 250, 252)):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(*rgb)


def header(slide, title, subtitle=None):
    bar = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.72))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.55), Inches(0.12), Inches(11.5), Inches(0.38))
    p = tb.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = title
    r.font.size = Pt(26)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    if subtitle:
        st = slide.shapes.add_textbox(Inches(0.55), Inches(0.42), Inches(10), Inches(0.22))
        p2 = st.text_frame.paragraphs[0]
        r2 = p2.add_run()
        r2.text = subtitle
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(220, 228, 245)


def footer(slide):
    box = slide.shapes.add_textbox(Inches(0.45), Inches(7.05), Inches(8), Inches(0.22))
    p = box.text_frame.paragraphs[0]
    p.text = "Lavanya Kumar | MATH 4090"
    p.font.size = Pt(10)
    p.font.color.rgb = MUTED


def bullets(slide, items, left=0.65, top=1.05, width=12.0, size=19, height=5.5):
    tx = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tx.text_frame
    tf.word_wrap = True
    for i, t in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = t
        p.font.size = Pt(size)
        p.font.color.rgb = TEXT
        p.space_after = Pt(10)


def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def add_scenario_table(slide, top=2.55):
    rows = [
        ["Scenario", "β", "γ"],
        ["Viral", "1.50", "0.080"],
        ["Moderate", "1.13", "0.089"],
        ["Fizzle", "0.15", "0.600"],
    ]
    tbl = slide.shapes.add_table(4, 3, Inches(0.7), Inches(top), Inches(9.0), Inches(1.95)).table
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = tbl.cell(ri, ci)
            c.text = val
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(17 if ri == 0 else 16)
                p.font.bold = ri == 0
                p.font.color.rgb = TEXT
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(225, 235, 250) if ri == 0 else RGBColor(252, 253, 255)


def add_parameter_table(slide):
    rows = [
        ["Symbol", "Meaning"],
        ["λ(t) = βS(t)/N", "Exposure rate driven by active sharers"],
        ["β", "Repost intensity: more sharing → more exposures"],
        ["γ", "Sharer decay: reposters stop being active over time"],
        ["ρᵢ", "Probability of sharing at exposure level i"],
        ["σᵢ", "Probability of saturating at exposure level i"],
    ]
    tbl = slide.shapes.add_table(len(rows), 2, Inches(0.7), Inches(1.35), Inches(11.5), Inches(3.2)).table
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = tbl.cell(ri, ci)
            c.text = val
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(16 if ri == 0 else 15)
                p.font.bold = ri == 0
                p.font.color.rgb = TEXT
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(225, 235, 250) if ri == 0 else RGBColor(252, 253, 255)


def add_exposure_fork_diagram(slide, y0=2.35):
    def box(x, y, w, h, label, sub=None, fill=(220, 234, 255)):
        sh = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.fill.solid()
        sh.fill.fore_color.rgb = RGBColor(*fill)
        sh.line.color.rgb = RGBColor(110, 125, 150)
        tf = sh.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = label
        r.font.bold = True
        r.font.size = Pt(15)
        r.font.color.rgb = TEXT
        if sub:
            p2 = tf.add_paragraph()
            p2.text = sub
            p2.alignment = PP_ALIGN.CENTER
            p2.font.size = Pt(11)
            p2.font.color.rgb = MUTED

    box(0.9, y0, 1.35, 0.95, "Iᵢ", "current class")
    box(3.2, y0 - 0.85, 1.25, 0.85, "S", "share\nρᵢ")
    box(3.2, y0 + 0.55, 1.25, 0.85, "R", "saturate\nσᵢ")
    box(5.5, y0, 1.35, 0.95, "Iᵢ₊₁", "continue\n1−ρᵢ−σᵢ")
    yl = y0 + 0.15
    for lbl, x, y in [
        ("ρᵢ →", 2.35, y0 - 0.55),
        ("σᵢ →", 2.35, y0 + 0.95),
        ("1−ρᵢ−σᵢ →", 2.35, yl),
    ]:
        tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(0.95), Inches(0.35))
        tb.text_frame.paragraphs[0].text = lbl
        tb.text_frame.paragraphs[0].font.size = Pt(12)
        tb.text_frame.paragraphs[0].font.color.rgb = MUTED
    cap_y = y0 + 1.35
    cap = slide.shapes.add_textbox(Inches(0.65), Inches(cap_y), Inches(11), Inches(0.45))
    cap.text_frame.paragraphs[0].text = "At i = 0: first exposure splits between repost, drop-out, or advancing to I₁."
    cap.text_frame.paragraphs[0].font.size = Pt(12)
    cap.text_frame.paragraphs[0].font.italic = True
    cap.text_frame.paragraphs[0].font.color.rgb = MUTED


def add_equation_block(slide):
    lines = [
        "λ(t) = β S(t) / N",
        "",
        "dI₀/dt = −λ(t) I₀",
        "",
        "dI₁/dt = (1−ρ₀−σ₀) λ(t) I₀ − λ(t) I₁",
        "",
        "dI₂/dt = (1−ρ₁−σ₁) λ(t) I₁ − (ρ₂+σ₂) λ(t) I₂",
        "",
        "dS/dt = Σᵢ₌₀² ρᵢ λ(t) Iᵢ − γ S",
        "",
        "dR/dt = Σᵢ₌₀² σᵢ λ(t) Iᵢ + γ S",
    ]
    left = slide.shapes.add_textbox(Inches(0.65), Inches(1.05), Inches(6.6), Inches(5.5))
    tf = left.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(15 if line else 6)
        p.font.color.rgb = TEXT
        p.space_after = Pt(4)
    note = slide.shapes.add_textbox(Inches(0.65), Inches(6.15), Inches(6.4), Inches(0.65))
    note.text_frame.paragraphs[0].text = (
        "Note: Inflow I₀→I₁ is (1−ρ₀−σ₀)λI₀ — only the “continue” outcome increases exposure count."
    )
    note.text_frame.paragraphs[0].font.size = Pt(11)
    note.text_frame.paragraphs[0].font.italic = True
    note.text_frame.paragraphs[0].font.color.rgb = MUTED


def flow_diagram_lower(slide, y=3.35):
    labels = ["I₀", "I₁", "I₂", "S", "R"]
    subs = ["0 exp.", "1 exp.", "2 exp.", "Sharers", "Saturated"]
    colors = [(220, 234, 255), (220, 234, 255), (220, 234, 255), (222, 245, 229), (252, 232, 230)]
    x_positions = [0.7, 2.85, 5.0, 7.35, 9.5]
    for i, (lab, sub, color, x) in enumerate(zip(labels, subs, colors, x_positions)):
        shp = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(1.55), Inches(1.05))
        shp.fill.solid()
        shp.fill.fore_color.rgb = RGBColor(*color)
        shp.line.color.rgb = RGBColor(110, 125, 150)
        tf = shp.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = f"{lab}\n{sub}"
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = TEXT
        if i < len(labels) - 1:
            arr = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.CHEVRON, Inches(x + 1.62), Inches(y + 0.32), Inches(0.5), Inches(0.45))
            arr.fill.solid()
            arr.fill.fore_color.rgb = RGBColor(160, 177, 201)
            arr.line.fill.background()


def build():
    ni = 0  # index into SLIDE_NOTES (must match slide order)

    def note(s):
        nonlocal ni
        set_notes(s, SLIDE_NOTES[ni])
        ni += 1

    assets = bp.ensure_assets()
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # Slide 1 — Title
    s = prs.slides.add_slide(blank)
    add_bg(s, (244, 247, 252))
    band = s.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.95))
    band.fill.solid()
    band.fill.fore_color.rgb = ACCENT
    band.line.fill.background()
    t = s.shapes.add_textbox(Inches(0.75), Inches(1.35), Inches(11.5), Inches(1.2))
    tf = t.text_frame
    p = tf.paragraphs[0]
    p.text = "Modelling the Spread of Information Through Social Media"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT
    p2 = tf.add_paragraph()
    p2.text = "Lavanya Kumar"
    p2.font.size = Pt(22)
    p2.font.color.rgb = MUTED
    p3 = tf.add_paragraph()
    p3.text = "MATH 4090"
    p3.font.size = Pt(20)
    p3.font.color.rgb = MUTED
    p4 = tf.add_paragraph()
    p4.text = "ODE model for repost spread with repeated exposure."
    p4.font.size = Pt(17)
    p4.font.color.rgb = RGBColor(70, 78, 90)
    p4.space_before = Pt(14)
    footer(s)
    note(s)

    # Slide 2
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "The question", "Why this model?")
    footer(s)
    bullets(
        s,
        [
            "Content gains visibility through reposting; users often see the same post more than once before reposting or losing interest.",
            "Goal: a tractable ODE framework with explicit exposure classes (I₀, I₁, …, Iₘ) tracking how many times someone has been exposed.",
            "A single “exposed / not exposed” split hides reinforcement from repeated views — this model keeps exposure count explicit.",
        ],
        size=18,
    )
    note(s)

    # Slide 3
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Background", "Where this project sits")
    footer(s)
    bullets(
        s,
        [
            "Epidemic-style models: classic diffusion uses compartments such as spreaders, ignorants, and stiflers.",
            "Complex contagion: experiments show repeated exposure can be needed before someone adopts or shares.",
            "This project: extend SIR-style ideas with an explicit chain I₀ → I₁ → ⋯ → Iₘ.",
        ],
        size=19,
    )
    note(s)

    # Slide 4
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Compartments", "State variables")
    footer(s)
    bullets(
        s,
        [
            "I₀: users not yet exposed (0 exposures).",
            "I₁, I₂: exposed 1 or 2 times, not actively sharing.",
            "S: active sharers.",
            "R: saturated users who will no longer share.",
            "Constraint: N is fixed — I₀ + I₁ + I₂ + S + R = N.",
        ],
        size=19,
        height=2.15,
    )
    flow_diagram_lower(s, y=3.35)
    note(s)

    # Slide 5
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "The exposure mechanism", "What happens on one new view")
    footer(s)
    bullets(
        s,
        [
            "New exposures arrive at mean-field rate λ.",
            "From Iᵢ: repost with probability ρᵢ → S; saturate with σᵢ → R; otherwise → Iᵢ₊₁ with probability 1−ρᵢ−σᵢ.",
            "Constraint: 0 ≤ ρᵢ, σᵢ ≤ 1 and ρᵢ + σᵢ ≤ 1.",
        ],
        top=1.05,
        width=11.8,
        size=18,
        height=1.85,
    )
    add_exposure_fork_diagram(s, y0=2.95)
    note(s)

    # Slide 6
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Model parameters", "Symbols and roles")
    footer(s)
    add_parameter_table(s)
    note(s)

    # Slide 7
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Governing equations", "Case m = 2")
    footer(s)
    add_equation_block(s)
    rb = s.shapes.add_textbox(Inches(7.35), Inches(1.1), Inches(5.5), Inches(4.8))
    rt = rb.text_frame
    rt.word_wrap = True
    hdr = rt.paragraphs[0]
    hdr.text = "One exposure from I₀"
    hdr.font.bold = True
    hdr.font.size = Pt(16)
    hdr.font.color.rgb = ACCENT
    for line in ["→ S   (prob. ρ₀)", "→ R   (prob. σ₀)", "→ I₁ (prob. 1−ρ₀−σ₀)"]:
        p = rt.add_paragraph()
        p.text = line
        p.font.size = Pt(15)
        p.font.color.rgb = TEXT
    note(s)

    # Slide 8
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Simulation setup", "Initial conditions and scenarios")
    footer(s)
    bullets(
        s,
        [
            "N = 1000, maximum exposure index m = 2.",
            "Seed: S(0) = 15, I₀(0) = 985; I₁(0) = I₂(0) = R(0) = 0.",
        ],
        top=1.05,
        width=11.5,
        size=19,
        height=1.35,
    )
    add_scenario_table(s, top=2.45)
    cap = s.shapes.add_textbox(Inches(0.7), Inches(4.55), Inches(11.5), Inches(0.9))
    cap.text_frame.word_wrap = True
    pcap = cap.text_frame.paragraphs[0]
    pcap.text = (
        "Viral: high β, low γ — strong exposure, slow sharer decay. Moderate: weaker β/γ (same ρ,σ as viral in runs). "
        "Fizzle: low β, high γ and higher σ — growth stalls near the seed. Values illustrate regimes, not platform calibration."
    )
    pcap.font.size = Pt(12)
    pcap.font.color.rgb = MUTED
    note(s)

    # Slide 9
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Active sharers over time", "S(t) for three scenarios")
    footer(s)
    s.shapes.add_picture(str(assets["comparison"]), Inches(0.75), Inches(1.2), width=Inches(9.2))
    cap = s.shapes.add_textbox(Inches(0.7), Inches(5.95), Inches(11.8), Inches(0.95))
    cap.text_frame.word_wrap = True
    p = cap.text_frame.paragraphs[0]
    p.text = (
        "Figure: Active reposters S(t). Viral: large peak — many users sharing at once. Moderate: lower/slower peak. "
        "Fizzle: S(t) ≈ 15 — no amplification. Same model; different β, γ, and (for fizzle) ρ,σ."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT
    note(s)

    # Slide 10
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Viral compartment dynamics", "All state variables, viral case")
    footer(s)
    s.shapes.add_picture(str(assets["exposure"]), Inches(0.75), Inches(1.2), width=Inches(9.2))
    cap = s.shapes.add_textbox(Inches(0.7), Inches(5.95), Inches(11.8), Inches(0.95))
    cap.text_frame.word_wrap = True
    p = cap.text_frame.paragraphs[0]
    p.text = (
        "Figure: Viral run — I₀ falls; I₁, I₂ rise then fall; S peaks then declines; R rises. "
        "Separate curves for 1st vs 2nd exposure validate the chain beyond one “exposed” state."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT
    note(s)

    # Slide 11
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Sensitivity to sharer decay γ", "Peak active sharers vs γ")
    footer(s)
    s.shapes.add_picture(str(assets["sensitivity"]), Inches(0.75), Inches(1.2), width=Inches(9.2))
    cap = s.shapes.add_textbox(Inches(0.7), Inches(5.95), Inches(11.8), Inches(0.95))
    cap.text_frame.word_wrap = True
    p = cap.text_frame.paragraphs[0]
    p.text = (
        "Figure: Peak max S(t) vs γ (β and viral ρ,σ fixed). Higher γ → faster loss of sharers → smaller peak; "
        "past a threshold the peak drops to ~ seed — qualitative regime change."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT
    note(s)

    # Slide 12
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Future work", "Toward the final report")
    footer(s)
    bullets(
        s,
        [
            "Complete nonlinear eigenvalue and stability analysis for the disease-free equilibrium E₀.",
            "Extend parameter sensitivity grids over β, γ, and ρᵢ.",
            "Optional: degree-weighted exposure or a small network toy model for heterogeneous influence.",
        ],
        size=19,
    )
    note(s)

    # Slide 13
    s = prs.slides.add_slide(blank)
    add_bg(s)
    header(s, "Conclusion", "Takeaways")
    footer(s)
    bullets(
        s,
        [
            "Repeated exposure is central to modelling complex social contagion in repost-driven settings.",
            "The interplay of repost intensity (β), attention decay (γ), and local rules (ρᵢ, σᵢ) "
            "determines whether content goes viral, spreads moderately, or fizzles out.",
            "Questions?",
        ],
        size=20,
    )
    note(s)

    assert ni == len(SLIDE_NOTES), f"Expected {len(SLIDE_NOTES)} note slides, got {ni}"

    prs.save(OUT_PATH)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    build()
