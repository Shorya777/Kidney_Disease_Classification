import logging
from pathlib import Path
import os

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    f'src/cnnClassifier/__init__.py',
    f'src/cnnClassifier/components/__init__.py',
    # f'src/cnnClassifier/prepare_base_model/__init__.py',
    # f'src/cnnClassifier/model_training/__init__.py',
    f'src/cnnClassifier/pipeline/__init__.py',
    f'src/cnnClassifier/config/__init__.py',
    f'src/cnnClassifier/config/configuration.py',
    f'src/cnnClassifier/utils/__init__.py',
    f'src/cnnClassifier/entity/__init__.py',
    f'src/cnnClassifier/constants/__init__.py',
    f'config/config.yaml',
    f'requirements.txt',
    f'params.yaml',
    f'research/trials.ipynb',
    f'dvc.yaml',
    f'setup.py'
]

for file_path in list_of_files:
    file_path= Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"{file_dir} directory created")

    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as obj:
            pass
        logging.info(f"Empty file created {file_name}")
    else:
        logging.info(f"{file_name} file already exists")