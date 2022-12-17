import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = pandas.DataFrame(nato_csv)

dict_nato = {value.letter:value.code for key, value in nato.iterrows()}

name = input("What's your name ? ")
name_list = [i.upper() for i in name]

phonetic_word = [dict_nato[i] for i in name_list]
print(phonetic_word)