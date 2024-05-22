import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

def generate_phonetic():
    input_string = input("Enter a word: ")
    try:
        output_list = [nato_dict[letter.upper()] for letter in input_string]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()