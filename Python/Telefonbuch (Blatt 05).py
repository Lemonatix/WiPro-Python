def add_entry(phonebook):
    name = input("Name eingeben: ")
    number = input("Telefonnummer eingeben: ")
    phonebook[name] = number
    print("Eintrag hinzugefügt.")

def find_entry(phonebook):
    name = input("Name zum Suchen eingeben: ")
    if name in phonebook:
        print(f"Telefonnummer: {phonebook[name]}")
    else:
        print("Eintrag nicht gefunden.")

def list_entries(phonebook):
    if phonebook:
        for name, number in phonebook.items():
            print(f"Name: {name}, Telefonnummer: {number}")
    else:
        print("Das Telefonbuch ist leer.")

def save_entries(phonebook):
    filename = input("Gebe den Namen der Datei zum speichern ein: ")
    with open(filename, 'w') as file:
        for name, number in phonebook.items():
            file.write(f"{name}, {number}\n")
    print("Einträge erfolgreich gespeichert.")
    
def load_entries(phonebook):
    filename = input("Gebe den Name der Datei zum Laden ein: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(", ")
                phonebook[name] = number
        print("Einträge erfolgreich geladen.")
    except FileNotFoundError:
        print("Datei nicht gefunden.")

def main():
    phonebook = {}

    while True:
        print("\nTelefonbuch-Menü:")
        print("1. Neuer Eintrag")
        print("2. Eintrag suchen")
        print("3. Alle Einträge anzeigen")
        print("4. Einträge speichern")
        print("5. Einträge laden")
        print("6. Beenden")

        choice = input("Wählen Sie eine Option: ")

        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            find_entry(phonebook)
        elif choice == "3":
            list_entries(phonebook)
        elif choice == "4":
            save_entries(phonebook)
        elif choice == "5":
            load_entries(phonebook)
        elif choice == "6":
            print("Telefonbuch beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()