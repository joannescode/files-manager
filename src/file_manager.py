import os
import json
import shutil
import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG)


def file_path(path):
    """
    Lists all files and directories in a specified path.

    Args:
        path (str): The directory path to list contents.

    Returns:
        list: A list of file and directory names in the specified path.
    """
    return os.listdir(path)


def reading_json():
    """
    Reads a JSON file named 'extensions.json' located in the same directory as the script.

    Returns:
        dict: Parsed JSON data as a dictionary containing file extensions categorized by type.

    Raises:
        FileNotFoundError: If 'extensions.json' is not found in the directory.
        json.JSONDecodeError: If the JSON file is improperly formatted.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(dir_path, "extensions.json")
    with open(json_path, "r") as f:
        return json.load(f)


def folder_per_extension(file_name, path, extension_mapping):
    """
    Organizes files into folders based on their file extensions.

    Args:
        file_name (str): The name of the file to organize.
        path (str): The base directory where the file is located.
        extension_mapping (dict): A dictionary mapping file categories to lists of extensions.

    Moves the file to a folder categorized by its extension. If the extension is not recognized, 
    the file is moved to an 'others' folder. Logs an error if file movement fails.
    
    Raises:
        shutil.Error: If an error occurs while moving the file.
        OSError: If an error occurs while creating directories or handling file extensions.
    """
    extension = os.path.splitext(file_name)[1][1:]

    folder_name = None
    for category, extensions in extension_mapping.items():
        if extension in extensions:
            folder_name = category.lower()
            break

    if not folder_name:
        folder_name = "others"

    try:
        folder_path = os.path.join(path, "files", folder_name)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(path, file_name)

        if os.path.isfile(file_path):
            shutil.move(
                os.path.join(path, file_name), os.path.join(folder_path, file_name)
            )
            logging.info(f"File: {file_name} moved to {folder_path}")
        elif os.path.isdir(file_path):
            pass

    except shutil.Error as e:
        logging.error("Error in trying to move file: " + str(e))

    except os.error as e:
        logging.error(
            "Error in trying to create folder or retrieve extension in file: " + str(e)
        )
