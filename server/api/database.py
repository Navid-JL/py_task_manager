import sqlite3

conn = sqlite3.connect('./data/tasks.db')

cursor = conn.cursor()

create_task_table = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL CHECK(length(title) <= 50),
    description TEXT CHECK(length(description) <= 200),
    is_completed BOOLEAN NOT NULL
);
'''

cursor.execute(create_task_table)

conn.commit()
conn.close()
