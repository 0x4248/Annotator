# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

import cv2
import datetime
import os
import sys

def draw_side_annotations(image, settings):
    if settings["Enabled"]:
        (h, w) = image.shape[:2]
        color = tuple(int(settings["Colour"][i:i+2], 16) for i in (1, 3, 5))
        font = cv2.FONT_HERSHEY_SIMPLEX
        size = settings["TextSize"]

        cv2.putText(image, settings["LText"], (10, h // 2), font, size / 40, color, 1, cv2.LINE_AA)
        cv2.putText(image, settings["RText"], (w - 50, h // 2), font, size / 40, color, 1, cv2.LINE_AA)
        cv2.putText(image, settings["TText"], (w // 2, 30), font, size / 40, color, 1, cv2.LINE_AA)
        cv2.putText(image, settings["BText"], (w // 2, h - 10), font, size / 40, color, 1, cv2.LINE_AA)

def draw_texts(image, settings, imagePath):
    for text in settings:
        display_text = get_data(text["Text"], imagePath)

        color = tuple(int(text["Colour"][i:i+2], 16) for i in (1, 3, 5))
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (text["Position"]["X"], text["Position"]["Y"])
        cv2.putText(image, display_text, position, font, text["Size"] / 20, color, 1, cv2.LINE_AA)

def get_var(num):
    for arg in sys.argv:
        if arg.startswith(f"-v{num}="):
            return arg.split("=")[1]

def get_data(name, imagePath):
    if name.startswith("$") == False:
        return name
    else:
        if name == "$DATE":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        elif name == "$TIME":
            return datetime.datetime.now().strftime("%H:%M:%S")
        elif name == "$FILENAME":
            return os.path.basename(imagePath)
        elif name == "$PATH":
            return imagePath
        elif name == "$FILE_DATE":
            return datetime.datetime.fromtimestamp(os.path.getctime(imagePath)).strftime("%Y-%m-%d")
        elif name == "$FILE_TIME":
            return datetime.datetime.fromtimestamp(os.path.getctime(imagePath)).strftime("%H:%M:%S")
        elif name.startswith("$V"):
            return get_var(name[2])
        else:
            return name
