# Annotator
# Quickly annotate images using JSON.
# Github: https://www.github.com/0x4248/Annotator
# Licence: GNU General Public License v3.0
# By: 0x4248

import cv2

def apply_image_settings(image, settings):
    if settings["Invert"]:
        image = cv2.bitwise_not(image)

    if settings["Contrast"] != 0 or settings["Brightness"] != 0:
        image = cv2.convertScaleAbs(image, alpha=(settings["Contrast"] + 1.0), beta=settings["Brightness"])

    if settings["Saturation"] != 0:
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv_image[..., 1] = cv2.add(hsv_image[..., 1], settings["Saturation"])
        image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    if settings["Hue"] != 0:
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv_image[..., 0] = cv2.add(hsv_image[..., 0], settings["Hue"])
        image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    if settings["FlipHorizontal"]:
        image = cv2.flip(image, 1)

    if settings["FlipVertical"]:
        image = cv2.flip(image, 0)

    if settings["Rotate"] != 0:
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, settings["Rotate"], 1.0)
        image = cv2.warpAffine(image, matrix, (w, h))

    return image
