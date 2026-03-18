from pathlib import Path
import json
import time
from PIL import Image


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def coco_paths():
    root = project_root()
    images_dir = root / "data" / "images" / "val2017"
    ann_file = root / "data" / "annotations" / "instances_val2017.json"
    return images_dir, ann_file


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def now():
    return time.perf_counter()


def load_image(path):
    return Image.open(path).convert("RGB")
