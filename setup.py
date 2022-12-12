from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements_list = requirement_file.readlines()
    requirements_list = [requirement_name.replace("\n","")].for requirement_name in requirement_list]
    
    if  HYPHEN_E_DOT in requirements_list:
        requirements_list.remove(HYPHEN_E_DOT)
    return requirements_list


setup(
    name = "sensor",
    version = "0.0.1",
    author= "Jagannath",
    author_email= "devarakondajagannath6378@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements(),
)