try:
    with open('input.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Datei nicht gefunden")