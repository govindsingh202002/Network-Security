"""
Setup.py is a blueprint which tells Python how to build, install, and run our project like a real software product.
Without is our project is just a file but with it our project is a Python Package
Setup.py is a essential part of packageing and distributing our python project.
It is used by setuptools to define the configuration of our python project

"""

from setuptools import setup, find_packages
import os
from typing import List

requirement_file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'requirements.txt')

# get all the required packages from requirement file
def get_all_requirements()->List[str]:
    try:
        # defining requirement list to store all the requirements
        requirements=[]
        # open requirement.txt file and read all the lines and store those requirement in a list with handling case like replace '\n' , removing '-e .'
        with open(requirement_file_path,'r') as requirement_file_object:
            lines=requirement_file_object.readlines()
            requirements=[requirement.replace('\n','') for requirement in  lines]
            if '-e .' in requirements:
                requirements.remove('-e .')

        return requirements        
    except Exception as e:
        print(f"Got an error while fetching all the requirements from requirement.txt file, the error message is {e}")


#setup this project
setup(
    name="Network_Security_Project",
    version="0.0.1",
    author="Govind Singh",
    author_email="govindsingh202002@gmail.com",
    packages=find_packages(),
    install_requires=get_all_requirements(),
    python_requires=">=3.10"
)