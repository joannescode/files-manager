from src.file_manager import file_path, reading_json, folder_per_extension

extension_mapping = reading_json()
path = ""

for file_name in file_path(path):
    folder_per_extension(file_name, path, extension_mapping)
