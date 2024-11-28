from setuptools import find_packages, setup  # Fixed typo in 'find_pakages'
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    Removes the '-e .' entry if present.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:  # Ensure file is opened in read mode
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use .strip() to handle all whitespace

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Shubham',
    author_email='shoes3171998@gmail.com',
    packages=find_packages(),  # Fixed typo in 'pakages'
    install_requires=get_requirements('requirements.txt')  # Ensure function is properly called
)
