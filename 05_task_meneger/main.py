import database


def print_menu():
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
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Ошибка: введите корректный числовой ID.")
        return None


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не может быть пустым.")


def ask_existing_task():
    """Запрашивает ID и возвращает задачу или None, если ввод неверный или задачи нет."""
    task_id = read_int("ID задачи: ")
    if task_id is None:
        return None
    task = database.get_task(task_id)
    if task is None:
        print(f"Ошибка: задача с ID {task_id} не найдена.")
        return None
    return task


def cmd_add_task():
    print("\n--- Добавление ---")
    title = read_non_empty("Название: ")
    description = input("Описание (можно пустое): ").strip()
    task_id = database.add_task(title, description)
    print(f"Задача создана. ID = {task_id}")


def cmd_list_tasks():
    print("\n--- Список задач ---")
    tasks = database.list_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    print(f"{'ID':<5}{'СТАТУС':<10}НАЗВАНИЕ")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']:<5}{task['status']:<10}{task['title']}")


def cmd_view_task():
    print("\n--- Просмотр ---")
    task = ask_existing_task()
    if task is None:
        return
    
    print(f"ID:          {task['id']}")
    print(f"Название:    {task['title']}")
    print(f"Описание:    {task['description'] if task['description'] else '(пусто)'}")
    print(f"Статус:      {task['status']}")
    print(f"Создано:     {task['created_at']}")


def cmd_edit_task():
    print("\n--- Редактирование ---")
    task = ask_existing_task()
    if task is None:
        return

    print(f"Текущее название: {task['title']}")
    new_title = input("Новое название (Enter — оставить): ").strip()
    if not new_title:
        new_title = task['title']

    print(f"Текущее описание: {task['description'] if task['description'] else '(пусто)'}")
    # Добавлена возможность очистить описание через ввод "-"
    new_description = input("Новое описание (Enter — оставить, '-' — очистить): ").strip()
    if new_description == "-":
        new_description = ""
    elif not new_description:
        new_description = task['description']

    # Убрана проверка if not new_title, так как выше мы гарантировали, что оно не пустое
    
    if database.update_task(task['id'], new_title, new_description):
        print("Задача обновлена.")


def cmd_complete_task():
    print("\n--- Завершение ---")
    task = ask_existing_task()
    if task is None:
        return
    
    if task['status'] == 'done':
        print("Задача уже выполнена.")
        return

    if database.complete_task(task['id']):
        print("Задача отмечена как выполненная.")


def cmd_reopen_task():
    print("\n--- Возврат в работу ---")
    task = ask_existing_task()
    if task is None:
        return

    if task['status'] == 'pending':
        print("Задача уже в статусе pending.")
        return

    if database.reopen_task(task['id']):
        print("Задача возвращена в статус pending.")


def cmd_delete_task():
    print("\n--- Удаление ---")
    task = ask_existing_task()
    if task is None:
        return
    
    answer = input(f"Удалить задачу '{task['title']}'? (y/n): ").strip().lower()
    if answer not in ("y", "yes", "д", "да"):
        print("Удаление отменено.")
        return

    if database.delete_task(task['id']):
        print("Задача удалена.")


def main():
    database.init_db()

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
        while True:
            print_menu()
            choice = input("Выберите пункт: ").strip()

            if choice == "0":
                print("Выход. До свидания!")
                break

            action = actions.get(choice)
            if action is None:
                print("Ошибка: неизвестный пункт меню.")
                continue

            try:
                action()
            except EOFError:
                # Пробрасываем Ctrl+D наверх, чтобы его поймал внешний try/except
                raise
            except Exception as exc:
                print(f"Непредвиденная ошибка: {exc}")

    except (KeyboardInterrupt, EOFError):
        print("\nВыход.")
    if __name__ == "__main__":
        main()