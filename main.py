TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
LINE = "-" * 40
user_dic = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = input("Zadej uživatelské jméno: ")
print("username:", username)
password = input("Zadej heslo: ")
print("password:", password)
print(LINE)

if username in user_dic and (password == user_dic[username]):
    print(f"Welcome to the app, {username} \nWe have {len(TEXTS)} to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()
print(LINE)

text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not int(text_number.isnumeric()) or int(text_number) > len(TEXTS) or int(text_number) <= 0:
    print("Wrong number, \nEnd of program")
    exit()

selected_text = TEXTS[int(text_number) - 1]
words = selected_text.split()
title_count = 0
upper_count = 0
lower_count = 0
numeric_count = 0
digit_count = 0
words_dict = dict()

for word_raw in words:
    word = word_raw.strip(".,:;")
    if word.istitle():
        title_count += 1
    if word.isupper():
        upper_count += 1
    if word.islower():
            lower_count += 1
    if word.isnumeric():
        numeric_count += 1
    if word.isdigit():
        digit_count += int(word)

    word_length = len(word)
    if word_length > 0:
        if word_length in words_dict:
            words_dict[word_length] += 1
        else:
            words_dict[word_length] = 1

print(f'''
There are {len(selected_text.split())} words in the selected text.
There are {title_count} titlecase words.
There are {upper_count} uppercase words.
There are {lower_count} lowercase words.
There are {numeric_count} numeric strings.
The sum of all the numbers {digit_count}.
''')
print(LINE)
print("LEN|   OCCURRENCES   |NR.")
print(LINE)
for key in sorted(words_dict):
    print(f"{key:>3}|{'*' * words_dict[key]:<17}|{words_dict[key]}")
