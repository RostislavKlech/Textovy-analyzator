"""
První projekt do Engeto Online Python Akademie

Autor: Rostislav Klech
Email: KlechRostislav@seznam.cz
Discord: Rosta K
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = "-"*40
numbers_of_TEXT = []

def quit(name: str, password: str, cancel = "quit") -> bool:
    if name == cancel or password == cancel:
        return True
    else:
        return False

def is_registered(name: str, password: str, registered: dict) -> bool:
    while  (name, password) not in tuple(zip(registered[list(registered.keys())[0]], registered[list(registered.keys())[1]])):
        print("Unregistered user, try again.\nFor tarmination write: quit.")
        name = input("Username: ")
        password = input("Password: ")
        if quit(name, password):
            break
    else:
        return True

def in_range(range: list):
    length = len(range)
    number_txt = input(f"Enter a number btw. 1 and {length} to select: ")
    if number_txt in range:
        return number_txt
    else:
        while number_txt not in range:
            print("Input is not number btw. 1 and 3.")
            number_txt = input(f"Enter a number btw. 1 and {length} to select: ")
        else:
            return number_txt

def cleaner(symbol: str, words: list):
    if symbol == "-":
        for word in words:
            if "-" in word:    
                word1 = word.split("-")
                words.remove(word)
                for member in word1:
                    words.append(member)
    else:
        for word in words:
            if symbol in word:
                words.remove(word)
                word1 = word.replace(symbol, "")
                words.append(word1)
    
def number_of_lengths(words: list):
    lengths = {}
    for word in words:
        if len(word) not in lengths.keys():
            lengths.update({len(word): 1})
        else:
            lengths[len(word)] += 1
    return lengths


def statistics(words: list):
    titlecase_count = 0
    uppercase_count = 0
    lowercase_count = 0
    numeric_count = 0
    sum_of_numbers = 0 
    for word in words:
            if word[0].isupper() and word.isalpha():
                titlecase_count += 1
                if word.isupper():
                    uppercase_count += 1
            if word.islower():
                lowercase_count += 1
            if word.isnumeric():
                numeric_count += 1
                sum_of_numbers += int(word)
    lengths = number_of_lengths(words)
    return titlecase_count, uppercase_count, lowercase_count, numeric_count, sum_of_numbers, lengths

def complete_lengths(numbers: dict):
    maximum = max(list(numbers.keys()))
    for i in range(1, maximum):
        if i not in numbers.keys():
            numbers.update({i: 0})
    return numbers

def write_row(length: int, count: int):
    print((3-len(str(length)))*" " + str(length) + 
              "|" + count*"*" + 
              (20-count)*" " + 
              "|" + str(count)
            ) 

registered = {"names": ["bob", "ann", "mike", "liz"], 
              "passwords": ["123", "pass123", "password123", "pass123"]
            }
name = input("Username: ")
password = input("Password: ")

if is_registered(name, password, registered):
    length_of_TEXTS = list(range(1, len(TEXTS)+1))
    print(separator)
    print(f"Welcome to the app, {name}")
    print(f"We have {length_of_TEXTS[-1]} texts to be analyzed.")
    print(separator)

    for i in length_of_TEXTS:
        numbers_of_TEXT.append(str(i))
    
    number = in_range(numbers_of_TEXT)
    words = TEXTS[int(number)-1].split()
    number_of_words = len(words)

    cleaner("-", words)
    cleaner(".", words)
    cleaner(",", words)

    titlecase_count, uppercase_count, lowercase_count, numeric_count, sum_of_numbers, lengths = statistics(words)
    
    complete_lengths(lengths)
    lengths = dict(sorted(lengths.items()))
    
    print(separator)
    print(f"There are {number_of_words} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all numbers is {sum_of_numbers}.")
    print(separator)
    print("LEN|     OCCURENCES     |NR.") 
    print(separator) 
    
    for key in lengths.keys():
        write_row(key, lengths.setdefault(key))

else:
    print("Terminating the program.")

