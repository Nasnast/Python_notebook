import json
import datetime

from data_create import *

notes = []


def save_notes():
    with open("notebook.json", "w") as file:
        json.dump(notes, file)


try:
    with open("notebook.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = []


############
def new_id():
    max_id = len(notes)
    for note in notes:
        if max_id < note["id"]:
            max_id = note["id"]
    return max_id


def add_notes():  # 1 создание заметки
    title = input_title()
    text = input_text()
    date = input_date()
    note = {"id": new_id() + 1, "title": title, "text": text, "date": date}
    notes.append(note)
    save_notes()
    print("Заметка добавлена.")


def print_notes():  # 2 вывод списка заметок
    print("Список заметок:")
    if len(notes) == 0:
        print("здесь пока ничего нет :-(")
    else:
        for note in notes:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}"
            )


def edit_notes():  # 3 редактирование заметки
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == id:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}"
            )
            note["title"] = input_title()
            note["text"] = input_text()
            note["date"] = input_date()
            save_notes()
            return print("Заметка отредактирована.")
    return print(f"Заметка с ID - {id} не найдена.")


def search_notes():  # 4 поиск по дате
    filter_date = input("Введите дату для фильтрации (дд/мм/гггг): ")
    try:
        datetime.datetime.strptime(filter_date, "%d/%m/%Y")

    except ValueError:
        return print("неверный формат даты")

    for note in notes:
        if filter_date in note["date"]:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}"
            )
    if not any(filter_date in note["date"] for note in notes):
        print("Заметок с такой датой не найдено.")


def delete_notes():  # 5 удаление
    id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes()
            return print(f"Заметка с ID - {id} удалена.")
    return print(f"Заметка с ID - {id} не найдена.")
