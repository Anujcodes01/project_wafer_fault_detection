from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requriments(filepath: str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)


setup(name='wafer fault',
      version='0.0.1',
      description='this project all about wafer fault detection ',
      author='anujdhyani',
      author_email='anujdhyani232@gmail.com',
      packages=find_packages(),
      install_requires = get_requriments("requirements.txt")
     )