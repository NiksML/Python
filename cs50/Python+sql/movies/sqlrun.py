import sqlite3

# Подключение к базе данных SQLite (или создание новой, если её нет)
connection = sqlite3.connect('movies.db')

# Создание курсора
cursor = connection.cursor()

# Открываем SQL-файл и выполняем запрос
for i in range(13,14):
    with open(f'{i}.sql', 'r') as sql_file:
        sql_query = sql_file.read()

    # Выполнение SQL-запроса
    cursor.execute(sql_query)

    # Вывод результатов в консоль
    result = cursor.fetchall()
    count = 0
    
    print(f'------------Results of {i}st sql-query------------')
    for row in result:
        print(row)
        count+=1
    print(count)


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()