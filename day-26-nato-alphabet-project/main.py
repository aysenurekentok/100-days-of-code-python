import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Your name: ").upper()

name_letters = [letter for letter in name]

phonetic = [dict_nato[letter] for letter in name_letters if letter in name]

print(phonetic)