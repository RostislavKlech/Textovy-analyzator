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
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
sum_of_numbers = 0
number_of_lenghts = set()
numbers_of_TEXT = []

registered = {"names": ["bob", "ann", "mike", "liz"], 
              "passwords": ["123", "pass123", "password123", "pass123"]
            }

registered_tuple = tuple(zip(registered["names"], registered["passwords"]))
name = input("Username: ")
password = input("Password: ")

if (name, password) not in registered_tuple:
    print("Unregistered user, terminating the program...")
else:
    print(separator)
    print("Welcome to the app, " + name)
    print("We have 3 texts to be analyzed.")
    print(separator)
    number_txt = input("Enter a number btw. 1 and 3 to select: ")
    
    length_of_TEXTS = list(range(1, len(TEXTS)+1))
    for i in length_of_TEXTS:
        numbers_of_TEXT.append(str(i))  

    if number_txt == "2":
        words_separated_by_length = [[]]
    else:
        words_separated_by_length = []

    if number_txt not in numbers_of_TEXT:
        print(separator)
        print("Input is not number btw. 1 and 3.")
    else:
        words = TEXTS[int(number_txt)-1].split()
        number_of_words = len(words) 

        for word in words:
            if "." in word:
                words.remove(word)
                word2 = word.replace(".", "")
                words.append(word2)
            if "," in word:
                words.remove(word)
                word3 = word.replace(",", "")
                words.append(word3)
            #PŘEDPOKLADAM ŽE buff-to-white JSOU TŘI SLOVA
            if "-" in word:    
                word4 = word.split("-")
                words.remove(word)
                for member in word4:
                    words.append(member)
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
            number_of_lenghts.add(len(word))
        
        for i in number_of_lenghts:
            words_separated_by_length.append([])

        for word in words:
            words_separated_by_length[len(word)-1].append(word)

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
        for i in range(1,len(words_separated_by_length)+1):
            print((3-len(str(i)))*" " + str(i) + 
                  "|" + len(words_separated_by_length[i-1])*"*" + 
                  (20-len(words_separated_by_length[i-1]))*" " + 
                  "|" + str(len(words_separated_by_length[i-1]))
                   ) 
        

               

        
        


    








