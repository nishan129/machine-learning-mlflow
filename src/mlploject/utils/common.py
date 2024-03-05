import os
from box.exceptions import BoxValueError
import yaml
from mlploject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns 
    
    Args:
        path_to_yaml(str): Path like input
        
    Raises:
        valueError: if yaml file is empty
        e: empty file
        
    Returns:
        confiBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} lodded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create list of directories

    Args:
        path_to_directories (list): list of the path or directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data

    Args:
        path (Path): Path to json file
        data (dict): data to be saved in json file
    """
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: Return the json data
    """
    with open(path) as f:
        conten = json.load(f)
        
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(conten)

@ensure_annotations
def save_bin(data: Any, path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    """load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """set size in kb

    Args:
        path (Path): path of the file

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"