# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

import cv2
import json
import datetime
import os
import sys

import annotator.img_settings as img_settings
import annotator.crosshair as crosshair
import annotator.grid as grid
import annotator.text as text

def main(imagePath, jsonPath, outputPath):
    image = cv2.imread(imagePath)

    with open(jsonPath, "r") as jsonFile:
        data = json.load(jsonFile)

    image = img_settings.apply_image_settings(image, data["ImageSettings"])
    crosshair.draw_crosshair(image, data["ImageOverlays"]["Crosshair"])
    grid.draw_grid(image, data["ImageOverlays"]["Grid"])
    text.draw_side_annotations(image, data["ImageOverlays"]["SideAnnotations"])
    text.draw_texts(image, data["Text"], imagePath)

    cv2.imwrite(outputPath, image)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python main.py <imagePath> <jsonPath> <outputPath>")
    else:
        imagePath = sys.argv[1]
        jsonPath = sys.argv[2]
        outputPath = sys.argv[3]
        main(imagePath, jsonPath, outputPath)
