import re


def names_students(file_txt: str) -> list:
    """ Функция очищает список студентов"""
    new_list = list()
    with open("data2" + file_txt, encoding="utf-8") as file_names:
        names_list = file_names.read().split()
        for i in names_list:
            new_name = ""
            for sumbol in i:
                if sumbol.isalpha():
                    new_name += sumbol
            if new_name.isalpha():
                new_list.append(new_name)

    return new_list


def is_cirillica(name_item: str) -> bool:
    return bool(re.search("[а-яА-Я]",name_item))


def filter_russian_names(name_list: list) -> list:
    new_name_list = list()
    for i in name_list:
        if is_cirillica(i):
            new_name_list.append(i)
    return new_name_list


if __name__ == "__main__":
    clered_name = names_students("/names.txt")

    print(filter_russian_names(clered_name))