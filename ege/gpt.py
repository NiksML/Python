def count_visitors_at_time(visitors, current_time):
    total_visitors = 0
    same_category_visitors = 0

    for visitor in visitors:
        arrival_time, duration, category = visitor
        end_time = arrival_time + duration

        if arrival_time <= current_time <= end_time:
            total_visitors += 1
            if category == current_visitor_category:
                same_category_visitors += 1

    return total_visitors, same_category_visitors

# Чтение входных данных
visitors = []
with open("26gpt.txt") as file:
    data=file.readline()
    N, T = map(int, data.split())
    for i in range(7):
        x=file.readline()
        y = list(map(str,x.split()))
        arrival_time, duration, category = y
        visitors.append((int(arrival_time), int(duration), category))

# Сортировка по приоритетам
visitors.sort(key=lambda x: (x[0], x[2] != 'G', x[2] != 'W'))
for i in range(len(visitors)):
    print(f'{i+1} {visitors[i]}')
print(len(visitors))

current_visitor_category = ''
for visitor in visitors:
    arrival_time, duration, category = visitor
    if arrival_time <= T <= arrival_time + duration:
        current_visitor_category = category

total, same_category = count_visitors_at_time(visitors, T)
print(total, same_category)

