# NATO Alphabet project

This console program takes a user's input of a word and return a list of all of the NATO phonetic alphabet 
that matches each of the letters in the word. My daily notes are below.

## 01-27-2024
### Today’s takeaways:

- Pandas `.read()` method will read a csv file as a data frame
- When creating a dictionary from a data frame, you want to create the key and value by getting the row’s column name (i.e. `row.letter` & `row.code`) when setting the new key and value pairs in the dictionary comprehension.

## 01-28-2024
### Today's takeaways:
- It helps to write the code in a loop (the long way) first to get it working and then shorten it using list comprehension.

### Challenges

1. The first “bug” I encountered was when I was trying to just print the values from the letters as keys. Since after the first letter, they were lowercase, I added code to change them to uppercase and resolved that issue.

## 05-22-2024
### Work completed:

- Add error/exception handling