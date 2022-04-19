filename_domains = "C:\\Homeworks\\domains.txt"
filename_names = "C:\\Homeworks\\names_1.txt"
filename_authors = "C:\\Homeworks\\authors.txt"


def read_file(filename: str) -> str:
    with open(filename, 'r') as file:
        data = file.read()
        return data


def return_change_list_domains(filename: str) -> list:
    data = read_file(filename).replace(".", "")
    string_list = data.split("\n")
    return string_list


def return_lastname_list(filename: str) -> list:
    data = read_file(filename)
    sournames = []
    for line in data.split("\n"):
        if line:
            sournames.append(line.split()[1])
    return sournames


def return_list_of_dictionaries(filename: str) -> list:
    data = read_file(filename)
    list_dates = []
    data = data.split("\n")
    for line in data:
        date = line.split("-")
        if date[0] and not date[0].isalpha():
            date_dict = dict(data=date[0])
            list_dates.append(date_dict.copy())
    return list_dates


domains = return_change_list_domains(filename_domains)
last_name = return_lastname_list(filename_names)
dictionaries = return_list_of_dictionaries(filename_authors)

print(domains, "\n", last_name, "\n", dictionaries)




