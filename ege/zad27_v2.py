import sys

with open(sys.argv[1]) as file:
    count_of_priem = int(file.readline().strip())
    priem = []

    for i in range(count_of_priem):
        zayavka = file.readline().strip()

        if not zayavka:
            print("end of file")
            break 

        start, end = map(int, zayavka.split())

        if i == 0 or all(not (p[0] < start < p[1] or p[0] < end < p[1] or (p[0] > start and end > p[1])) for p in priem):
            priem.append((start, end))
            print(f"{i + 1} {start} {end}")
        else:
            print(f"{i + 1} {start} {end} skipped")

    print(priem)
