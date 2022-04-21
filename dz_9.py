import os


def creat_dict_file_dir(dirname: str) -> dict:
    list_files = []
    list_path = []
    dict_files_path = dict()
    list_dir = os.listdir(dirname)
    for filename in list_dir:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            list_path.append(filename)
        elif os.path.isfile(filepath):
            list_files.append(filename)
    dict_files_path["filenames"] = list_files
    dict_files_path["dirnames"] = list_path
    return dict_files_path


def sort_dictionary(dictionary: dict, reverse_sort: bool) -> dict:
    for key, value in dictionary.items():
        dictionary[key] = sorted(value, reverse=not reverse_sort)
    return dictionary


def write_file_path(dictionary: dict, string: str) -> dict:
    if string.count("."):
        dictionary["filenames"].append(string)
    else:
        dictionary["dirnames"].append(string)
    return dictionary


dir_name = "\\Homeworks"
reverse_sort = False
string = "test"

dict_files_path = creat_dict_file_dir(dir_name)
sort = sort_dictionary(dict_files_path, reverse_sort)
write = write_file_path(dict_files_path, string)

