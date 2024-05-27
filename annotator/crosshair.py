# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

import cv2

def draw_crosshair(image, settings):
    if settings["Enabled"]:
        (h, w) = image.shape[:2]
        color = tuple(int(settings["Colour"][i:i+2], 16) for i in (1, 3, 5))
        x_center, y_center = w // 2, h // 2

        x_center += settings["Offset"]["X"]
        y_center += settings["Offset"]["Y"]
        size = settings["Size"]
        thickness = settings["Thickness"]

        if settings["Type"] == "Plus":
            cv2.line(image, (x_center - size, y_center), (x_center + size, y_center), color, thickness)
            cv2.line(image, (x_center, y_center - size), (x_center, y_center + size), color, thickness)
        elif settings["Type"] == "Cross":
            cv2.line(image, (x_center - size, y_center - size), (x_center + size, y_center + size), color, thickness)
            cv2.line(image, (x_center + size, y_center - size), (x_center - size, y_center + size), color, thickness)
        elif settings["Type"] == "Dot":
            cv2.circle(image, (x_center, y_center), thickness, color, -1)
        elif settings["Type"] == "Circle":
            cv2.circle(image, (x_center, y_center), size, color, thickness)
        elif settings["Type"] == "Square":
            cv2.rectangle(image, (x_center - size, y_center - size), (x_center + size, y_center + size), color, thickness)
