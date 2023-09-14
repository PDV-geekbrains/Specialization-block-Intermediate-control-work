import os
from pathlib import Path
import datetime


def start():
    fileName = "notebook.csv"
    menuItem = 0
    while menuItem != 1:
        notebook = getNotebook(fileName)
        menuItem = getMenuItem()
        # 2. Создать.
        if menuItem == 2:
            print(
                "\033[1;37m"
                + "\n=== Новая заметка (нельзя использовать символ ';') ==="
                + "\033[0m"
            )
            record = getNewRecord(notebook)
            saveRecord(fileName, record)
        # 3. Редактировать.
        elif menuItem == 3:
            print(
                "\033[1;37m"
                + "\n=== Редактирование заметки (нельзя использовать символ ';') ==="
                + "\033[0m"
            )
            id = getId()
            notebook = changeRecordById(notebook, id)
            saveNotebook(fileName, notebook)
        # 4. Удалить.
        elif menuItem == 4:
            print("\033[1;37m" + "\n=== Удаление заметки ===" + "\033[0m")
            id = getId()
            notebook = deleteRecordById(notebook, id)
            saveNotebook(fileName, notebook)
        # 5. Найти.
        elif menuItem == 5:
            print("\033[1;37m" + "\n=== Поиск заметки по её номеру ===" + "\033[0m")
            id = getId()
            printRecordById(notebook, id)
        # 6. Показать всё.
        elif menuItem == 6:
            print("\033[1;37m" + "\n=== Список всех заметок ===" + "\033[0m")
            printAllRecords(notebook)


def printAllRecords(notebook: list):
    """Метод выводит на консоль все заметки."""
    for i in range(0, len(notebook), 4):
        print("id: " + notebook[i])
        print("Заголовок: " + notebook[i + 1])
        print("Текст: " + notebook[i + 2])
        print("Дата: " + notebook[i + 3])
    print(
        "\033[1;37m" + "=== Всего " + str(len(notebook) / 4)[:-2] + " ===" + "\033[0m"
    )


def printRecordById(notebook: list, id: int):
    """Метод выводит на консоль заметку по заданному id."""
    isFound = False
    for i in range(0, len(notebook), 4):
        if notebook[i] == str(id):
            isFound = True
            print("id: " + notebook[i])
            print("Заголовок: " + notebook[i + 1])
            print("Текст: " + notebook[i + 2])
            print("Дата: " + notebook[i + 3])
            break
    if isFound == False:
        print(
            "\033[31m"
            + "Ошибка. Заметка с номером "
            + str(id)
            + " не существует."
            + "\033[0m"
        )


def saveNotebook(path: str, notebook: list):
    """Метод перезаписывает файл изменённым содержанием notebook."""
    stringToSave = ""
    for item in notebook:
        stringToSave += ";" + str(item)
    stringToSave = stringToSave[1:]  # Удалить первую запятую.
    with open(path, mode="w") as file:
        file.write(stringToSave)


def changeRecordById(notebook: list, id: int) -> list:
    """Метод изменяет поля заметки."""
    isFound = False
    for i in range(0, len(notebook), 4):
        if notebook[i] == str(id):
            isFound = True
            # Новый заголовок.
            print("Старый заголовок: " + notebook[i + 1])
            notebook[i + 1] = input(
                "\033[36m" + "Введите новый заголовок: " + "\033[0m"
            )
            # Новое тело заметки.
            print("Старый текст: " + notebook[i + 2])
            notebook[i + 2] = input("\033[36m" + "Отредактируйте текст : " + "\033[0m")
            # Обновлённая дата/время.
            notebook[i + 3] = datetime.datetime.now()
            break
    if isFound == False:
        print(
            "\033[31m"
            + "Ошибка. Заметка с номером "
            + str(id)
            + " не существует."
            + "\033[0m"
        )
    return notebook


def deleteRecordById(notebook: list, id: int) -> list:
    """Метод удаляет заметку с заданным id."""
    isFound = False
    for i in range(0, len(notebook), 4):
        if notebook[i] == str(id):
            isFound = True
            for j in range(4):
                notebook.pop(i)
            break
    if isFound == False:
        print(
            "\033[31m"
            + "Ошибка. Заметка с номером "
            + str(id)
            + " не существует."
            + "\033[0m"
        )
    return notebook


def getId() -> int:
    """Метод возвращает id введённый пользователем."""
    userInput = ""
    # result = -1
    userInput = input("\033[36m" + "Введите номер заметки: " + "\033[0m")
    try:
        userInput = int(userInput)
    except Exception:
        print(
            "\033[31m"
            + "Ошибка. Введите целое число. Вы ввели '"
            + userInput
            + "'"
            + "\033[0m"
        )
    return userInput


def saveRecord(path: str, record: list):
    """Метод добавляет заметку в файл."""
    stringToSave = ""
    for item in record:
        stringToSave += ";" + str(item)
    # Если это первая запись в файле, удалить первую запятую.
    if os.stat(path).st_size == 0:
        stringToSave = stringToSave[1:]
    with open(path, mode="a") as file:
        file.write(stringToSave)


def getNewRecord(notebook: list) -> list:
    """Метод возвращает заметку на основании ввода пользователя."""
    record = []
    newId = 0
    if len(notebook) < 4:
        newId = 1
    else:
        newId = int(notebook[-4]) + 1
    record.append(str(newId))  # id.
    record.append(input("\033[36m" + "Введите заголовок: " + "\033[0m"))  # caption.
    record.append(input("\033[36m" + "Введите текст: " + "\033[0m"))  # text.
    record.append(datetime.datetime.now())  # dateTime.
    return record


def getNotebook(path: str) -> list:
    """Метод читает данные из csv файла в список."""
    notebook = []
    createFileIfNotExists(path)
    with open(path, mode="r") as fileToRead:
        notebook = fileToRead.read().split(";")
    return notebook


def createFileIfNotExists(path: str):
    """Создаёт файл с заданным именем в рабочей директории если
    такового не существует."""
    if Path(path).is_file() != True:
        open(path, "w").close()


def getMenuItem() -> int:
    """Метод возвращает номер меню выбранный пользователем."""
    isValid = False
    inputError = False
    result = -1
    userInput = ""
    print("\033[1;37m" + "\n=== РАБОТА С ЗАМЕТКАМИ ===" + "\033[0m")
    print("1. Выход")
    print("2. Создать")
    print("3. Редактировать")
    print("4. Удалить")
    print("5. Найти")
    print("6. Показать всё")
    userInput = input("\033[36m" + "Введите пункт меню: " + "\033[0m")
    try:
        result = int(userInput)
    except Exception:
        inputError = True
        print(
            "\033[31m"
            + "Ошибка. Введите целое число. Вы ввели '"
            + userInput
            + "'"
            + "\033[0m"
        )
    if result > 0 and result < 7:
        isValid = True
    if isValid == False and inputError == False:
        print(
            "\033[31m"
            + "Ошибка. Номер "
            + str(userInput)
            + " не соответствует меню."
            + "\033[0m"
        )
    return result


start()
