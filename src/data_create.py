import datetime


def input_title():
    return input("Введите заголовок заметки: ")


def input_text():
    return input("Введите текст заметки: ")


def input_date():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
