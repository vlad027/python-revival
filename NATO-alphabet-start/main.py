import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row['letter']: row['code'] for index, row in data.iterrows()}

while True:
    try:
        word_to_code = input("Enter a word to convert: ").upper()
        list_output = [alphabet[letter] for letter in word_to_code]
        break
    except KeyError:
        print("Only letters are allowed, try again.")
print(list_output)

