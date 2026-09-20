import re


def names_students(file_txt: str) -> list:
    """Функция очищает список студентов"""
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
    """Функция проверяет на русские имена"""
    return bool(re.search("[а-яА-Я]", name_item))


def filter_russian_names(name_list: list) -> list:
    """Функция фильтрует русские имена"""
    new_name_list = list()
    for i in name_list:
        if is_cirillica(i):
            new_name_list.append(i)
    return new_name_list


def filter_english_names(name_list: list) -> list:
    """Функция фильтрует английские имена"""
    new_name_list = list()
    for i in name_list:
        if not is_cirillica(i):
            new_name_list.append(i)
    return new_name_list


def save_to_file(fill_name: str, data: str) -> None:
    """Функция сохраняет данные в файл"""
    with open("data2/" + fill_name, "w", encoding="utf-8") as name_file:
        name_file.write(data)


if __name__ == "__main__":
    clered_name = names_students("/names.txt")

    filtered_name = filter_russian_names(clered_name)
    save_to_file("russian_name.txt", "\n".join(filtered_name))
    filtered_name = filter_english_names(clered_name)
    save_to_file("english_name.txt", "\n".join(filtered_name))
