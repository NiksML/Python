import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.DictReader(file)

    i = 0
    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(f'{i} {row["language"]}')
        i+=1