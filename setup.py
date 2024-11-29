from setuptools import find_packages,setup
from typing import List

# HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements.

    requ = []

    with open(file_path) as file_obj:
        requ = file_obj.readlines()
        requ = [req.replace('\n',"")for req in requ]

        # if HYPHEN_E_DOT in requ:
        #     requ.remove(HYPHEN_E_DOT)

    return requ

setup(
    name = "mlProject",
    version='0.0.1',
    author='Sanjana',
    author_email='patilsanjana761@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirement.txt')
)