import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


input_string = input("Enter a word: ")
output_list = [nato_dict[letter.upper()] for letter in input_string]
print(output_list)
