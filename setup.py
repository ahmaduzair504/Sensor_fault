from setuptools import find_packages, setup
# This is the setup file for the Sensor fault detection project.
from typing import List

def get_requirements()-> List[str]:
    requirements_list =list[str] = []
    return requirements_list


setup(
    name="Sensor fault detection",
    version="0.0.1",
    author="Ahmad Uzair",
    author_email="ahmaduzair2585@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),
    
)