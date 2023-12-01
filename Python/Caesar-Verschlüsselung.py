def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_letters(text):
    count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            count[char] = count.get(char, 0) + 1
    return count

def find_most_frequent_letter(count):
    return max(count, key=count.get)

def calculate_shift(most_frequent):
    return (ord(most_frequent) - ord('e')) % 26

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Hauptprogramm
filename = "text1.txt"
text = read_file(filename)
letter_count = count_letters(text)
most_frequent = find_most_frequent_letter(letter_count)
shift = calculate_shift(most_frequent)
decrypted_text = decrypt(text, shift)

print("Verschlüsselter Text:", text)
print("Entschlüsselter Text:", decrypted_text)