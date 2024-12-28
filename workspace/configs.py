import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    SimpleTextColorCfg,
)

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))

NUM_IMG = 1000

def story_data():
    return GeneratorCfg(
        num_image=NUM_IMG,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=32,
            perspective_transform=NormPerspectiveTransformCfg(20, 20, 1.5),
            corpus=WordCorpus(
                WordCorpusCfg(
                    # text_paths=[CURRENT_DIR / "corpus" / "demo-full.txt"],
                    # text_paths=[CURRENT_DIR / "corpus" / "demo-title.txt"],
                    text_paths=[CURRENT_DIR / "corpus" / "demo-title-no-lines.txt"],
                    font_dir=CURRENT_DIR / "font",
                    font_size=(20, 30),
                    num_word=(1, 4),
                ),
            ),
            # corpus_effects=Effects(Line(0.9, thickness=(2, 5))),
            gray=False,
            text_color_cfg=SimpleTextColorCfg(),
        ),
    )


configs = [story_data()]