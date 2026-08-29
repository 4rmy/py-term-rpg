#!/usr/bin/env python3
"""
Reproduces the output of `ansi --color-codes` from
https://github.com/fidian/ansi

This is a direct port of the ansi::colorCodes and ansi::colorCodePatch
bash functions from that project's `ansi` script.
"""

import sys

ESC = "\033"
CSI = ESC + "["


def bold():
    return CSI + "1m"


def normal():
    return CSI + "22m"


def fg_white():
    return CSI + "37m"


def fg_black():
    return CSI + "30m"


def reset_fg():
    return CSI + "39m"


def bg_color(code):
    return f"{CSI}48;5;{code}m"


def reset_bg():
    return CSI + "49m"


def color_code_patch(code):
    """Equivalent of ansi::colorCodePatch: print a background swatch with its code."""
    out = bg_color(code)
    out += f" {code:>3} "
    out += reset_bg()
    return out


def color_codes():
    """Equivalent of ansi::colorCodes."""
    out = []

    # Standard colors (0-7)
    out.append("Standard: ")
    out.append(bold())
    out.append(fg_white())
    for code in range(0, 8):
        if code == 7:
            out.append(fg_black())
        out.append(color_code_patch(code))
    out.append(reset_fg())
    out.append(normal())

    # Intense colors (8-15)
    out.append("\nIntense: ")
    out.append(fg_white())
    for code in range(8, 16):
        if code == 9:
            out.append(fg_black())
        out.append(color_code_patch(code))
    out.append(reset_fg())
    out.append("\n\n")

    # 216-color cube, in 3 blocks of rows, 6 rows each, 6 columns per half-row
    for i in (16, 22, 28):
        for offset in (0, 36, 72, 108, 144, 180):
            j = i + offset

            out.append(fg_white())
            out.append(bold())
            for code in range(j, j + 6):
                out.append(color_code_patch(code))
            out.append(normal())
            out.append(reset_fg())

            out.append(" ")

            out.append(fg_black())
            for code in range(j + 18, j + 24):
                out.append(color_code_patch(code))
            out.append(reset_fg())

            out.append("\n")
        out.append("\n")

    # Grayscale ramp (232-255)
    out.append("Grays: ")
    out.append(bold())
    out.append(fg_white())
    for code in range(232, 244):
        out.append(color_code_patch(code))
    out.append(reset_fg())
    out.append(normal())

    out.append("\n ")
    out.append(fg_black())
    for code in range(244, 256):
        out.append(color_code_patch(code))
    out.append(reset_fg())
    out.append("\n")

    return "".join(out)


if __name__ == "__main__":
    sys.stdout.write(color_codes())
