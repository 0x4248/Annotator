# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/0x4248/FMAP
# Licence: GNU General Public Licence v3.0
# By: 0x4248

from setuptools import setup

setup(
    name="annotator",
    version="1.0.0",
    packages=["annotator"],
    install_requires=[
        "opencv-python",
    ],
)
