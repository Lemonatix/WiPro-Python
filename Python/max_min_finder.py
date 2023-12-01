def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Warnung: '{file.strip()}' ist keine gültige Zahl.")
    return numbers

def find_max_min(numbers):
    return max(numbers), min(numbers)

def write_max_min_to_file(filename, max_value, min_value):
    with open(filename, 'w') as file:
        file.write(f"max: {max_value}\n")
        file.write(f"mine: {min_value}\n")
        
def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
    numbers = read_numbers_from_file(input_filename)
    if not numbers:
        print("Keine gültigen Zahlen in der Datei gefunden.")
        return
    
    max_value, min_value = find_max_min(numbers)
    write_max_min_to_file(output_filename, max_value, min_value)
    print(f"Maximale und minimale Werte wurden in '{output_filename}' geschrieben.")
    
if __name__ =="__main__":
    main()
    
import os
print("Aktuelles Arbeitsverzeichnis:", os.getcwd())