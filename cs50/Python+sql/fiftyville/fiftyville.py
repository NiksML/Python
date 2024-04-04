import sqlite3
from mtranslate import translate

# Подключение к базе данных SQLite (или создание новой, если её нет)
connection = sqlite3.connect('fiftyville.db')

# Создание курсора
cursor = connection.cursor()

# 
cmon_names = []
thief = '?'
city = '?'
accomplice = '?'

# Открываем SQL-файл и выполняем запрос
for i in range(1,15):
    with open(f'{i}.sql', 'r') as sql_file:
        comment = sql_file.readline()
        sql_query = sql_file.read()

    # Выполнение SQL-запроса
    cursor.execute(sql_query)
    
    # Вывод результатов в консоль
    result = cursor.fetchall()
    count = 0

    # Присвоение переменным значений ответов на вопросы расследования
    if(i == 4 or i == 6 or i == 8 or i == 11):
        cmon_names.append(result)
    if (i == 12):
        city = result
    if (i == 14):
        accomplice = result

    print(f'------------Results of {i}st sql-query------------')
    print(f'{comment}\n')

    if(i==1 or i==2):
        for row in result:
            row = ''.join(row)
            transrow = translate(row, 'ru')
            print(f'{count+1}.{transrow}')
            count+=1
    else:
        for row in result:
            print(f'{count+1}.{row}')
            count+=1
    
    print(f'\nfound {count} rows\n\n')
    
# Ответ кто убил сохраняется в переменную. Он ищет пересечения между ответами на запросы 4 6 8 11 sql файлов
thief = set(cmon_names[0]).intersection(*cmon_names[1:])

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

with open('answers.txt', 'r') as file:
    lines = file.readlines()

thief_str = ''.join(str(item[0]) for item in thief)
city_str = ''.join(str(item[0]) for item in city)
accomplice_str = ''.join(str(item[0]) for item in accomplice)

lines[0] = f'The THIEF is: {thief_str}\n'
lines[1] = f'The city the thief ESCAPED TO: {city_str}\n'
lines[2] = f'The ACCOMPLICE is: {accomplice_str}\n'

with open('answers.txt', 'w') as file:
    file.writelines(lines)