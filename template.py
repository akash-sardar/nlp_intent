'''
template.Py will create the project structure for the Intent project.
'''
import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]: %(message)s:")

project_name = "intent"

# list of files will contain the workflow and will be used to upload code to github thru YAML file
# constructor file INIT is required to create the code as a local package

list_of_files = [
    ".github/workflow/.gitkeep",
    ".github/workflow/main.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    ".gitignore"
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            f.write("")
            logging.info("Creating Empty File: {filepath}")
    else:
        logging.info(f"File: {filename} already exists and is not empty")

