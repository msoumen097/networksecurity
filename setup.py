from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not find")
    return requirement_list
print(get_requirements())

setup(
    name='network_security',
    version ="0.0.1",
    author = 'Soumen Mondal',
    author_email="soumon2003@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
