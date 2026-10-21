import sys  # Нужен для корректного выхода через sys.exit()
import database  # Наш модуль для работы с SQLite


def print_menu():
    print("\n==== TASK MANAGER ====\n")  # Пустая строка + заголовок
    print("1. Add task")  # Пункт меню
    print("2. List tasks")  
    print("3. View task")  
    print("4. Edit task")  
    print("5. Complete task")  
    print("6. Delete task")  
    print("0. Exit")  # Пункт выхода


def read_int(prompt: str) -> int | None:
    raw = input(prompt).strip()  # Читаем строку без пробелов по краям
    try:
        return int(raw)  # Пытаемся превратить в число
    except ValueError:  # Если ввели не число
        print("Ошибка: введите корректный числовой ID.")  # Сообщаем об ошибке
        return None  # Сигналим вызывающему, что ввод плохой


def read_non_empty(prompt: str) -> str:
    while True:  # Крутимся, пока не получим непустую строку
        value = input(prompt).strip()  # Читаем ввод
        if value:  # Если строка не пустая
            return value  # Возвращаем её
        print("Ошибка: значение не может быть пустым. Попробуйте снова.")  # Иначе просим повторить


def cmd_add_task():
    print("\n--- Add task ---")  # Заголовок действия
    title = read_non_empty("Title: ")  # Название обязательно
    description = input("Description (можно оставить пустым): ").strip()  # Описание необязательно
    task_id = database.add_task(title, description)  # Создаём задачу в БД
    print(f"Задача успешно создана. ID = {task_id}")  # Сообщаем пользователю


def cmd_list_tasks():
    print("\n--- List tasks ---")  # Заголовок действия
    tasks = database.list_tasks()  # Получаем все задачи
    if not tasks:  # Если список пуст
        print("Список задач пуст.")  # Сообщаем
        return  # Выходим из функции
    print(f"{'ID':<5}{'STATUS':<10}TITLE")  # Шапка таблицы с выравниванием
    print("-" * 40)  # Разделитель
    for task_id, title, status in tasks:  # Распаковываем каждый кортеж
        print(f"{task_id:<5}{status:<10}{title}")  # Печатаем строку задачи


def cmd_view_task():
    print("\n--- View task ---")  # Заголовок действия
    task_id = read_int("Task ID: ")  # Запрашиваем ID
    if task_id is None:  # Если ввод некорректный
        return  # Выходим
    task = database.get_task(task_id)  # Ищем задачу
    if task is None:  # Если не нашли
        print(f"Ошибка: задача с ID {task_id} не найдена.")  # Сообщаем
        return  # Выходим
    tid, title, description, status, created_at = task  # Распаковываем поля
    print(f"ID:          {tid}")  # Печатаем ID
    print(f"Title:       {title}")  # Печатаем название
    print(f"Description: {description if description else '(пусто)'}")  # Описание или заглушка
    print(f"Status:      {status}")  # Печатаем статус
    print(f"Created at:  {created_at}")  # Печатаем дату создания


def cmd_edit_task():
    print("\n--- Edit task ---")  # Заголовок действия
    task_id = read_int("Task ID: ")  # Запрашиваем ID
    if task_id is None:  # Некорректный ввод
        return  # Выходим
    task = database.get_task(task_id)  # Проверяем, что задача существует
    if task is None:  # Не нашли
        print(f"Ошибка: задача с ID {task_id} не найдена.")  # Сообщаем
        return  # Выходим
    _, old_title, old_description, _, _ = task  # Берём только нужные поля

    print(f"Текущее название: {old_title}")  # Показываем старое название
    new_title = input("Новое название (Enter — оставить текущее): ").strip()  # Запрашиваем новое
    if not new_title:  # Если пусто
        new_title = old_title  # Оставляем старое

    print(f"Текущее описание: {old_description if old_description else '(пусто)'}")  # Показываем старое описание
    new_description = input("Новое описание (Enter — оставить текущее): ").strip()  # Запрашиваем новое
    if not new_description:  # Если пусто
        new_description = old_description  # Оставляем старое

    if not new_title:  # Доп. защита от пустого названия
        print("Ошибка: название не может быть пустым.")  # Сообщаем
        return  # Выходим

    if database.update_task(task_id, new_title, new_description):  # Пробуем обновить
        print("Задача успешно обновлена.")  # Успех
    else:
        print("Ошибка: не удалось обновить задачу.")  # Не удалось


def cmd_complete_task():
    print("\n--- Complete task ---")  # Заголовок действия
    task_id = read_int("Task ID: ")  # Запрашиваем ID
    if task_id is None:  # Некорректный ввод
        return  # Выходим
    if database.complete_task(task_id):  # Пробуем сменить статус
        print(f"Задача с ID {task_id} отмечена как выполненная (done).")  # Успех
    else:
        print(f"Ошибка: задача с ID {task_id} не найдена.")  # Не нашли


def cmd_delete_task():
    print("\n--- Delete task ---")  # Заголовок действия
    task_id = read_int("Task ID: ")  # Запрашиваем ID
    if task_id is None:  # Некорректный ввод
        return  # Выходим
    task = database.get_task(task_id)  # Проверяем, что задача есть
    if task is None:  # Не нашли
        print(f"Ошибка: задача с ID {task_id} не найдена.")  # Сообщаем
        return  # Выходим
    answer = input(f"Удалить задачу '{task[1]}'? (y/n): ").strip().lower()  # Спрашиваем подтверждение
    if answer not in ("y", "yes", "д", "да"):  # Если не подтвердили
        print("Удаление отменено.")  # Сообщаем
        return  # Выходим
    if database.delete_task(task_id):  # Пробуем удалить
        print("Задача удалена.")  # Успех
    else:
        print("Ошибка: не удалось удалить задачу.")  # Не удалось


def main():
    database.init_db()  # Создаём БД и таблицу при старте

    actions = {  # Словарь: пункт меню -> функция
        "1": cmd_add_task,
        "2": cmd_list_tasks,
        "3": cmd_view_task,
        "4": cmd_edit_task,
        "5": cmd_complete_task,
        "6": cmd_delete_task,
    }

    while True:  # Главный цикл программы
        print_menu()  # Показываем меню
        choice = input("Select option: ").strip()  # Читаем выбор

        if choice == "0":  # Выход
            print("Выход. До свидания!")  # Прощаемся
            sys.exit(0)  # Завершаем программу

        action = actions.get(choice)  # Ищем обработчик
        if action is None:  # Неизвестный пункт
            print("Ошибка: неизвестный пункт меню.")  # Сообщаем
            continue  # Снова показываем меню

        try:  # Ловим возможные ошибки, чтобы программа не падала
            action()  # Вызываем обработчик
        except KeyboardInterrupt:  # Ctrl+C
            print("\nПрервано пользователем.")  # Сообщаем
            sys.exit(0)  # Выходим
        except Exception as exc:  # Любая другая ошибка
            print(f"Непредвиденная ошибка: {exc}")  # Печатаем и продолжаем


if __name__ == "__main__":  # Запускаем main() только при прямом запуске файла
    main()  # Точка входа