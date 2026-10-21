import sqlite3  # Встроенный модуль для работы с SQLite
from datetime import datetime  # Нужен для получения текущей даты и времени

DB_NAME = "tasks.db"  # Имя файла базы данных


def get_connection():
    return sqlite3.connect(DB_NAME)  # Открываем (или создаём) соединение с БД


def init_db():
    with get_connection() as conn:  # Контекстный менеджер закроет соединение сам
        conn.execute(  # Выполняем SQL-запрос создания таблицы
            """
            CREATE TABLE IF NOT EXISTS tasks (  -- Создаём таблицу, только если её нет
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный ID, автоинкремент
                title TEXT NOT NULL,  -- Название обязательно
                description TEXT,  -- Описание может быть пустым
                status TEXT NOT NULL DEFAULT 'pending',  -- Статус по умолчанию pending
                created_at TEXT NOT NULL  -- Дата и время создания
            )
            """
        )
        conn.commit()  # Фиксируем изменения на диске


def add_task(title: str, description: str) -> int:
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Текущая дата и время строкой
    with get_connection() as conn:
        cursor = conn.execute(  # INSERT с параметрами-заглушками `?`
            "INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
            (title, description, "pending", created_at),  # Значения для `?` по порядку
        )
        conn.commit()  # Фиксируем изменения
        return cursor.lastrowid  # Возвращаем id только что созданной задачи


def list_tasks():
    with get_connection() as conn:
        cursor = conn.execute("SELECT id, title, status FROM tasks ORDER BY id")  # Берём все задачи по порядку
        return cursor.fetchall()  # Возвращаем список кортежей


def get_task(task_id: int):
    with get_connection() as conn:
        cursor = conn.execute(  # Ищем задачу по id через `?`
            "SELECT id, title, description, status, created_at FROM tasks WHERE id = ?",
            (task_id,),  # Кортеж из одного элемента — обязательна запятая
        )
        return cursor.fetchone()  # Вернёт кортеж или None, если задачи нет


def update_task(task_id: int, title: str, description: str) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(  # UPDATE меняет title и description
            "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
            (title, description, task_id),  # Значения для `?` по порядку
        )
        conn.commit()  # Фиксируем изменения
        return cursor.rowcount > 0  # True, если строка реально обновилась


def complete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(  # Меняем статус на done
            "UPDATE tasks SET status = 'done' WHERE id = ?",
            (task_id,),  # id подставляем через `?`
        )
        conn.commit()  # Фиксируем изменения
        return cursor.rowcount > 0  # True, если задача найдена и обновлена


def delete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))  # Удаляем задачу по id
        conn.commit()  # Фиксируем изменения
        return cursor.rowcount > 0  # True, если строка была удалена