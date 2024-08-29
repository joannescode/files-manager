import os
import json
import shutil
import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG)


def file_path(path):
    return os.listdir(path)


def reading_json():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(dir_path, "extensions.json")
    with open(json_path, "r") as f:
        return json.load(f)


def folder_per_extension(file_name, path, extension_mapping):
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
