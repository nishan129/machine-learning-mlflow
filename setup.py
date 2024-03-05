from setuptools import setup, find_packages
from typing import List

def get_requirements() ->List[str]:
    
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    
    return requirement_list

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Machine-Leatning-Mlflow"
AUTHOR_USER_NAME = "nishant139"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "nishant139@gmail.com"

setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small mlops project",
    long_description= long_description,
    long_description_content_type="test/markdown",
    packages= find_packages(), 
    install_requires = get_requirements()     
)