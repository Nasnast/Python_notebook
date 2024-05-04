import json
import datetime

# from user_interface import interface

notes = []


def save_notes():
    with open("notebook.json", "a") as file:
        json.dump(notes, file)


# def load_notes():
#    global notes

try:
    with open("notebook.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = []


def add_notes():  # 1 создание заметки
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "text": text, "date": date}
    notes.append(note)
    save_notes()
    print("Заметка добавлена.")


def print_notes():  # 2 вывод списка заметок
    print("Список заметок")
    for note in notes:
        print(
            f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}"
        )


def edit_notes():  # редактирование заметки
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == id:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}"
            )
            note["title"] = input("Введите новый заголовок заметки: ")
            note["text"] = input("Введите новый текст заметки: ")
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка отредактирована.")
            break

    print(f"Заметка с ID - {id} не найдена.")


# var = 0
#            while var != "3":
#                print(
#                    "Для редактирования заголовка нажмите - 1\n"
#                    "Для редактирования текста заметки нажмите  - 2\n"
#                    "Для возврата в главное меню нажмите - 3"
#                )
# var = input("выберите вариант действия: ")
# while var not in ("1", "2", "3"):
#     print("некорректный ввод!")
# var = input("выберите вариант действия: ")
# print()
# match var:
#     case "1":
#         note["title"] = input("Введите новый заголовок заметки: ")
#         note["date"] = datetime.datetime.now().strftime(
#             "%Y-%m-%d %H:%M:%S"
#         )
#         save_notes()
#         print("Заметка отредактирована.")
#         break
#     case "2":
#         note["text"] = input("Введите новый текст заметки: ")
#         note["date"] = datetime.datetime.now().strftime(
#             "%Y-%m-%d %H:%M:%S"
#         )
#         save_notes()
#         print("Заметка отредактирована.")
#         break
#     # case "3":
#     # interface()
