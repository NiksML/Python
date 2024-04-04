import sqlite3

# Подключение к базе данных (если она не существует, то будет создана новая)
connection = sqlite3.connect('mydatabase.db')

# Создание объекта курсора
cursor = connection.cursor()

cursor.execute("DELETE FROM users")

# Пример создания таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Tom', 33))

# Пример вставки много данных в таблицу
data = [('John', 25), ('Alice', 30), ('Bob', 28)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)",   data)

# Пример выборки данных
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Фиксация изменений и закрытие соединения
connection.commit()
connection.close()