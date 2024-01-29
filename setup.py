from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of dependencies from requirements.txt file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','')for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "end_2_end_ml_project",
    version = '0.0.1',
    author = 'pavangorantla2000',
    author_email = 'pavangorantla2000@gmail.com',
    packages =  find_packages(),
    install_requires = get_requirements('requirements.txt')
)