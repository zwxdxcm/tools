def crop2rect(img):
    h, w, _ = img.shape
    len_ = min(h, w)
    h_pads = int((h - len_) / 2)
    w_pads = int((w - len_) / 2)
    return img[h_pads : h_pads + len_, w_pads : w_pads + len_]


def gen_common_color(idx=0):
    # BGR MODE
    colors = (
        (255, 0, 0),  # Blue
        (0, 0, 255),  # Red
        (0, 255, 0),  # Green
        (0, 255, 255),  # Yellow
        (255, 255, 0),  # Cyan
        (255, 0, 255),  # Magenta
        (128, 128, 128),  # Gray
        (192, 192, 192),  # Silver
        (0, 0, 128),  # Maroon
        (0, 128, 128),  # Olive
        (128, 0, 0),  # Navy
        (128, 128, 0),  # Teal
        (128, 0, 128),  # Purple
        (0, 128, 255),  # Orange
        (0, 215, 255),  # Gold
        (0, 51, 153),  # Brown
        (255, 218, 185),  # Peach
        (114, 128, 250),  # Salmon
        (220, 245, 245),  # Beige
        (250, 230, 230),  # Lavender
        (208, 224, 64),  # Turquoise
        (250, 255, 127),  # Mint
        (140, 230, 240),  # Khaki
        (130, 0, 75),  # Indigo
        (255, 0, 200),  # Fuchsia
        (235, 206, 135),  # SkyBlue
        (205, 90, 106),  # SlateBlue
        (55, 140, 45),  # ForestGreen
    )

    return colors[idx % len(colors)]