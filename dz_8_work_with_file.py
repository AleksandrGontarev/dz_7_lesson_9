
###################################################    1

filename_domains = "C:\\Homeworks\\domains.txt"


def return_change_list_domains(filename):
    buffer_line = ""
    with open(filename, 'r') as work_file:
        list_domains = work_file.read()
        for symbol in list_domains:
            if symbol != ".":
                buffer_line += symbol
        return buffer_line.split("\n")


###################################################     2

filename_names = "C:\\Homeworks\\names_1.txt"


def return_lastname_list(filename):
    with open(filename_names, 'r') as file:
        list_name = file.read()
        sournames = []
        for line in list_name.split("\n"):
            if line:
                sourname = line.split()[1]
                sournames.append(sourname)
    return sournames


##############################################################    3

filename_authors = "C:\\Homeworks\\authors.txt"


def return_list_of_dictionaries(filename):
    with open(filename_authors, 'r') as file:
        list_dict = file.read()
        data = []
        dlist = []
        test_dict = {}
        for line in list_dict.split("\n"):
            if len(line.split()[0:3]) == 3:
                data.append(line.split()[0:3])
        for line in data:
            test_dict["data"] = " ".join(line)
            dlist.append(test_dict.copy())
    return dlist


print(return_change_list_domains(filename_domains))
print(return_lastname_list(filename_names))
print(return_list_of_dictionaries(filename_authors))





