import json
import datetime

notes = []
id_len = len(notes) + 1


def save_notes():
    with open("notebook.json", "w") as file:
        json.dump(notes, file)


# def load_notes():
#    global notes

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
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # id_len = len(notes) + 1
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
            note["title"] = input("Введите новый заголовок заметки: ")
            note["text"] = input("Введите новый текст заметки: ")
            note["date"] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            save_notes()
            return print("Заметка отредактирована.")
    return print(f"Заметка с ID - {id} не найдена.")


def search_notes():  # 4 поиск по дате
    filter_date = input("Введите дату для фильтрации (дд/мм/гггг): ")
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
