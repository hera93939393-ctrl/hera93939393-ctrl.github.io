import json
import shutil
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

from build_docx import add_exam_table, add_footer_logo, add_header

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_ROOT / "data"
OUT_ROOT = PROJECT_ROOT / "generated" / "KTW VOCA"

LEVELS = [
    ("BA", "BASIC"),
    ("PA", "PRE-INTERMEDIATE"),
    ("IA", "INTERMEDIATE"),
    ("HA", "HIGH"),
    ("JUPITER", "JUPITER"),
    ("SATURN", "SATURN"),
    ("URANUS", "URANUS"),
    ("NEPTUNE", "NEPTUNE"),
]


def ordered_items(data, code):
    indexed = list(enumerate(data[code]))
    indexed.sort(key=lambda pair: (int(pair[1].get("tier", 1)), pair[1]["day"], pair[0]))
    return [item for _, item in indexed]


def build_one(path, level_name, ab, items, is_answer):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.35)
    section.bottom_margin = Cm(0.9)
    section.left_margin = Cm(1.1)
    section.right_margin = Cm(1.1)
    section.footer_distance = Cm(0.2)
    add_footer_logo(section)

    normal = doc.styles["Normal"]
    normal.font.name = "함초롬바탕"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "함초롬바탕")
    normal.font.size = Pt(10.5)

    add_header(doc, level_name, ab)
    add_exam_table(doc, items[:50], 1, 0.86, is_answer)
    doc.add_page_break()
    add_exam_table(doc, items[50:100], 51, 1.00, is_answer)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)


def main():
    level_filter = sys.argv[1] if len(sys.argv) > 1 else None
    selected_levels = [pair for pair in LEVELS if level_filter is None or pair[1] == level_filter]
    if level_filter:
        target = OUT_ROOT / level_filter
        if target.exists():
            shutil.rmtree(target)
    elif OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    datasets = {
        "A": json.loads((SOURCE / "selected_A.json").read_text(encoding="utf-8")),
        "B": json.loads((SOURCE / "selected_B.json").read_text(encoding="utf-8")),
    }
    made = []
    for code, level_name in selected_levels:
        for ab in ("A", "B"):
            items = ordered_items(datasets[ab], code)
            folder = OUT_ROOT / level_name / f"{ab}형"
            for is_answer, suffix in ((False, "시험지"), (True, "정답지")):
                path = folder / f"{level_name}_{ab}_{suffix}.docx"
                build_one(path, level_name, ab, items, is_answer)
                made.append(path)
    print(f"CREATED={len(made)}")
    for path in made:
        print(path)


if __name__ == "__main__":
    main()
