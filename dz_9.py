import os
CHEKBOX = False
NAME_FILE_OR_PATH = "test"



def creat_dict_file_dir(dirname: str) -> dict:
    list_files = []
    list_path = []
    dict_files_path = dict()
    list_dir = os.listdir(dirname)
    for filename in list_dir:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            list_path.append(filename)
            dict_files_path["dirnames"] = list_path
        if os.path.isfile(filepath):
            list_files.append(filename)
            dict_files_path["filenames"] = list_files
    return dict_files_path


def sort_dictionary(dictionary: dict, checkbox: bool = CHEKBOX) -> dict:
    if not checkbox:
        for key, value in dictionary.items():
            dictionary[key] = sorted(value)
        else:
            for key, value in dictionary.items():
                dictionary[key] = sorted(value, reverse=True)
    return dictionary


def write_file_path(dictionary: dict, string: str = NAME_FILE_OR_PATH) -> dict:
    if string.count("."):
        dictionary["filenames"].append(string)
    else:
        dictionary["dirnames"].append(string)
    return dictionary


dir_name = "\\Homeworks"

dict_files_path = creat_dict_file_dir(dir_name)
sort = sort_dictionary(dict_files_path, CHEKBOX)
write = write_file_path(dict_files_path, NAME_FILE_OR_PATH)