import os
from pathlib import Path
import logging

#logging string (when u will be executing this file ,the acvities that are perfomed will be shown on the terminal)
#Insted of printing that operation you can log it and it will be shown in the terminal. Try to use logging instead of print statements
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier" #you can also name kidney disease classifier

list_of_files = [
    ".github/workflows/.gitkeep", #this is for github actions
    f"src/{project_name}/__init__.py", #this is for the source code of the project
    f"src/{project_name}/components/__init__.py", #this is for the components of the project
    f"src/{project_name}/utils/__init__.py", #this is for the utilities of the project
    f"src/{project_name}/config/__init__.py", #this is for the configuration of the project
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", #this is for the configuration file of the project
    "dvc.yaml", #this is for the dvc file of the project
    "params.yaml", #this is for the parameters file of the project  
    "requirements.txt", #this is for the requirements file of the project
    "setup.py", #this is for the setup file of the project
    "research/trials.ipynb", #this is for the research file of the project
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) #this will convert the string to a path object
    filedir, filename = os.path.split(filepath) #this will split the path into directory and file name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #this will create the directory if it does not exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #this will check if the file does not exist or is empty
        with open(filepath, "w") as f: #this will create an empty file
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
