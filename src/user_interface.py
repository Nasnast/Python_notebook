from basic_metod import *


def interface():

    var = 0
    while var != "6":
        print(
            "Главное меню:\n"
            "1. Добавить заметку\n"
            "2. Вывести на экран все заметки\n"
            "3. Редактировать заметку\n"
            "4. Поиск заметок\n"
            "5. Удалить заметку\n"
            "6. Выход"
        )
        print()
        var = input("выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5", "6"):
            print("некорректный ввод!")
            var = input("выберите вариант действия: ")
        print()

        match var:
            case "1":
                add_notes()
            case "2":
                print_notes()
            case "3":
                edit_notes()
            case "4":
                search_notes()
            case "5":
                delete_notes()
            case "6":
                print("Приложение закрыто")
        print()
