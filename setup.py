from setuptools import find_packages, setup
# This is the setup file for the Sensor fault detection project.
from typing import List

setup(
    name="Sensor fault detection",
    version="0.0.1",
    author="Ahmad Uzair",
    author_email="ahmaduzair2585@gmail.com",
    packages= find_packages(),
    install_requires=["pymongo"]
)