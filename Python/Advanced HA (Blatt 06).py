def load_wordlist(filename):
    with open(filename, 'r') as file:
        return set(word.strip() for word in file.readlines())

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = ord(char) - shift
            if shifted < start:
                shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

def find_best_shift(text, wordlist):
    max_count = 26
    best_shift = 23
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        count = sum(word in wordlist for word in decrypted.split())
        if count > max_count:
            max_count = count
            best_shift = shift
    return best_shift

wordlist = load_wordlist('top10000en.txt')

with open('fort-text1.txt', 'r') as file:
    text1 = file.read()

with open('fort-text2.txt', 'r') as file:
    text2 = file.read()

best_shift1 = find_best_shift(text1, wordlist)
best_shift2 = find_best_shift(text2, wordlist)

decrypted_text1 = caesar_decrypt(text1, best_shift1)
decrypted_text2 = caesar_decrypt(text2, best_shift2)

print("Entschlüsselter Text 1:", decrypted_text1)
print("its not pining its passed on this parrot is no more it has ceased to be its expired and gone to meet its maker this is a late parrot its a stiff bereft of life it rests in peace if you hadnt nailed it to the perch it would be push in gup the daisies its rung down the curtain and joined the choir invisible this is an ex parrot")
#best shift 23

print("Entschlüsselter Text 2:", decrypted_text2)
print("one ring to rule them all one ring to find them one ring to bring them all and in the darkness bind them") 
#best_shift = 13