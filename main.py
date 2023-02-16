from create_keycap import make_keycap
import os

ICON_BASE_DIR = "./svgs"
CAP_STL_FILE = "./keycap_blank/basecapv2-Body.stl"


for svg_file in os.listdir(ICON_BASE_DIR):
    if svg_file.endswith(".svg"):
        ICON_SVG_FILE = f"{ICON_BASE_DIR}/{svg_file}"
        ICON_NAME = svg_file.split(".")[0]
        make_keycap(CAP_STL_FILE, ICON_SVG_FILE, f"target/{ICON_NAME}.stl")