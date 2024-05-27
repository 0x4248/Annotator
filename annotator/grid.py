# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

import cv2

def draw_grid(image, settings):
    if settings["Enabled"]:
        (h, w) = image.shape[:2]
        color = tuple(int(settings["Colour"][i:i+2], 16) for i in (1, 3, 5))
        thickness = settings["Thickness"]
        spacing = settings["Spacing"]

        for x in range(0, w, spacing):
            if settings["Type"] == "Lines":
                cv2.line(image, (x, 0), (x, h), color, thickness)
            elif settings["Type"] == "Dots":
                for y in range(0, h, spacing):
                    cv2.circle(image, (x, y), thickness, color, -1)

        for y in range(0, h, spacing):
            if settings["Type"] == "Lines":
                cv2.line(image, (0, y), (w, y), color, thickness)
            elif settings["Type"] == "Dots":
                for x in range(0, w, spacing):
                    cv2.circle(image, (x, y), thickness, color, -1)