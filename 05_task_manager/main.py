import database  # Импортируем наш модуль для работы с базой данных


def print_menu():
    # Печатаем главное меню программы
    print("\n==== МЕНЕДЖЕР ЗАДАЧ ====\n")
    print("1. Добавить задачу")
    print("2. Список задач")
    print("3. Посмотреть задачу")
    print("4. Редактировать задачу")
    print("5. Завершить задачу")
    print("6. Удалить задачу")
    print("7. Вернуть в работу (pending)")
    print("0. Выход")


def read_int(prompt: str) -> int | None:
    # Читаем строку, убираем пробелы по краям
    raw = input(prompt).strip()
    try:
        # Пытаемся превратить ввод в целое число
        return int(raw)
    except ValueError:
        # Если ввели не число, сообщаем об ошибке и возвращаем None
        print("Ошибка: введите корректный числовой ID.")
        return None


def read_non_empty(prompt: str) -> str:
    # Зацикливаемся, пока пользователь не введет непустую строку
    while True:
        value = input(prompt).strip()
        if value:  # Если строка не пустая — возвращаем её
            return value
        # Иначе просим ввести заново
        print("Ошибка: значение не может быть пустым.")


def ask_existing_task():
    """Запрашивает ID и возвращает задачу или None, если ввод неверный или задачи нет."""
    task_id = read_int("ID задачи: ")
    if task_id is None:
        return None  # Неверный ввод ID
    task = database.get_task(task_id)  # Ищем задачу в базе
    if task is None:
        print(f"Ошибка: задача с ID {task_id} не найдена.")
        return None  # Задачи с таким ID нет
    return task  # Возвращаем найденную задачу


def cmd_add_task():
    print("\n--- Добавление ---")
    # Запрашиваем название (обязательно)
    title = read_non_empty("Название: ")
    # Запрашиваем описание (можно оставить пустым)
    description = input("Описание (можно пустое): ").strip()
    # Сохраняем задачу в базу и получаем её новый ID
    task_id = database.add_task(title, description)
    print(f"Задача создана. ID = {task_id}")


def cmd_list_tasks():
    print("\n--- Список задач ---")
    tasks = database.list_tasks()  # Получаем список всех задач
    if not tasks:
        print("Список задач пуст.")
        return
    # Печатаем шапку таблицы
    print(f"{'ID':<5}{'СТАТУС':<10}НАЗВАНИЕ")
    print("-" * 40)
    # Выводим каждую задачу
    for task in tasks:
        print(f"{task['id']:<5}{task['status']:<10}{task['title']}")


def cmd_view_task():
    print("\n--- Просмотр ---")
    task = ask_existing_task()  # Получаем задачу по ID (или None)
    if task is None:
        return
    
    # Выводим все поля задачи
    print(f"ID:          {task['id']}")
    print(f"Название:    {task['title']}")
    print(f"Описание:    {task['description'] if task['description'] else '(пусто)'}")
    print(f"Статус:      {task['status']}")
    print(f"Создано:     {task['created_at']}")


def cmd_edit_task():
    print("\n--- Редактирование ---")
    task = ask_existing_task()  # Получаем задачу по ID
    if task is None:
        return

    # Запрашиваем новое название
    print(f"Текущее название: {task['title']}")
    new_title = input("Новое название (Enter — оставить): ").strip()
    if not new_title:
        new_title = task['title']  # Если пусто — оставляем старое

    # Запрашиваем новое описание
    print(f"Текущее описание: {task['description'] if task['description'] else '(пусто)'}")
    new_description = input("Новое описание (Enter — оставить, '-' — очистить): ").strip()
    if new_description == "-":
        new_description = ""  # Спецсимвол для очистки описания
    elif not new_description:
        new_description = task['description']  # Если пусто — оставляем старое

    # Сохраняем изменения в базу
    if database.update_task(task['id'], new_title, new_description):
        print("Задача обновлена.")
    else:
        print("Ошибка: не удалось обновить задачу.")


def cmd_complete_task():
    print("\n--- Завершение ---")
    task = ask_existing_task()  # Получаем задачу по ID
    if task is None:
        return
    
    # Если задача уже выполнена — сообщаем об этом
    if task['status'] == 'done':
        print("Задача уже выполнена.")
        return

    # Меняем статус на done
    if database.complete_task(task['id']):
        print("Задача отмечена как выполненная.")
    else:
        print("Ошибка: не удалось изменить статус задачи.")


def cmd_reopen_task():
    print("\n--- Возврат в работу ---")
    task = ask_existing_task()  # Получаем задачу по ID
    if task is None:
        return

    # Если задача уже в pending — сообщаем об этом
    if task['status'] == 'pending':
        print("Задача уже в статусе pending.")
        return

    # Меняем статус обратно на pending
    if database.reopen_task(task['id']):
        print("Задача возвращена в статус pending.")
    else:
        print("Ошибка: не удалось изменить статус задачи.")


def cmd_delete_task():
    print("\n--- Удаление ---")
    task = ask_existing_task()  # Получаем задачу по ID
    if task is None:
        return
    
    # Запрашиваем подтверждение удаления
    answer = input(f"Удалить задачу '{task['title']}'? (y/n): ").strip().lower()
    if answer not in ("y", "yes", "д", "да"):
        print("Удаление отменено.")
        return

    # Удаляем задачу из базы
    if database.delete_task(task['id']):
        print("Задача удалена.")
    else:
        print("Ошибка: не удалось удалить задачу.")


def main():
    database.init_db()  # Создаём базу и таблицу при запуске

    # Словарь: пункт меню -> функция-обработчик
    actions = {
        "1": cmd_add_task,
        "2": cmd_list_tasks,
        "3": cmd_view_task,
        "4": cmd_edit_task,
        "5": cmd_complete_task,
        "6": cmd_delete_task,
        "7": cmd_reopen_task,
    }

    try:
        # Главный цикл программы
        while True:
            print_menu()  # Показываем меню
            choice = input("Выберите пункт: ").strip()  # Читаем выбор

            if choice == "0":
                print("Выход. До свидания!")
                break  # Выходим из цикла

            # Ищем обработчик для выбранного пункта
            action = actions.get(choice)
            if action is None:
                print("Ошибка: неизвестный пункт меню.")
                continue

            try:
                action()  # Вызываем выбранную функцию
            except EOFError:
                raise  # Пробрасываем Ctrl+D наверх
            except Exception as exc:
                # Ловим любые другие ошибки, чтобы программа не падала
                print(f"Непредвиденная ошибка: {exc}")

    except (KeyboardInterrupt, EOFError):
        # Корректный выход при Ctrl+C или Ctrl+D
        print("\nВыход.")


if __name__ == "__main__":
    main()
