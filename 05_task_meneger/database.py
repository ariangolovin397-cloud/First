import sqlite3
from datetime import datetime
from pathlib import Path
from contextlib import closing

# Исправление бага с путями: база всегда будет создаваться рядом с database.py
DB_NAME = Path(__file__).parent / "tasks.db"


def get_connection():
    # row_factory позволяет обращаться к колонкам по имени: row["title"]
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # closing() гарантирует закрытие соединения даже при ошибке
    with closing(get_connection()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                -- Добавлено ограничение CHECK на уровне БД
                status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'done')),
                created_at TEXT NOT NULL
            )
            """
        )
        # commit() теперь делает сам контекстный менеджер `with conn:`
        with conn:
            pass


def add_task(title: str, description: str) -> int:
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with closing(get_connection()) as conn:
        with conn: # Автоматический commit при успехе, rollback при ошибке
            cursor = conn.execute(
                "INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
                (title, description, "pending", created_at),
            )
            return cursor.lastrowid


def list_tasks():
    with closing(get_connection()) as conn:
        cursor = conn.execute("SELECT id, title, status FROM tasks ORDER BY id")
        return cursor.fetchall()


def get_task(task_id: int):
    with closing(get_connection()) as conn:
        cursor = conn.execute(
            "SELECT id, title, description, status, created_at FROM tasks WHERE id = ?",
            (task_id,),
        )
        return cursor.fetchone()


def update_task(task_id: int, title: str, description: str) -> bool:
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(
                "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
                (title, description, task_id),
            )
            return cursor.rowcount > 0


def complete_task(task_id: int) -> bool:
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(
                "UPDATE tasks SET status = 'done' WHERE id = ?",
                (task_id,),
            )
            return cursor.rowcount > 0


def reopen_task(task_id: int) -> bool:
    # Дополнительное задание: возврат в статус pending
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(
                "UPDATE tasks SET status = 'pending' WHERE id = ?",
                (task_id,),
            )
            return cursor.rowcount > 0


def delete_task(task_id: int) -> bool:
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            return cursor.rowcount > 0