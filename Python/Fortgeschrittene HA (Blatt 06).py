def load_wordlist(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())
    
def decrypt_with_shift(text, shift):
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

def find_best_shift(text, wordlist):
    max_count = 26
    best_shift = 13
    for shift in range(26):
        decrypted = decrypt_with_shift(text, shift)
        count = sum(word in wordlist for word in decrypted.split())
        if count > max_count:
            max_count = count
            best_shift = shift
    return best_shift

def main():
    wordlist = load_wordlist('top10000en.txt')
    filename = 'fort-text1.txt'
    with open(filename, 'r') as file:
        text = file.read()
        
    best_shift = find_best_shift(text, wordlist)
    decryped_text = decrypt_with_shift(text, best_shift)
    
    print("Bester Shift-Wert:", best_shift)
    print("Entschlüsselter Text:", decryped_text)

if __name__ == "__main__":
    main()