from setuptools import find_packages,setup
from typing import List
TRIGER_NOTATION='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        if TRIGER_NOTATION in requirements:
            requirements.remove(TRIGER_NOTATION)
    return requirements


setup(
    name="ML project",
    version="0.0.0.1",
    author="R Nisahnth",
    author_email="nishanth0962333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)