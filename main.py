"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Klara Cibulkova
email: cibulkovaklara@seznam.cz
"""
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

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print("username:", end=" ")
username = input().strip()
print("password:", end=" ")
password = input().strip()

if USERS.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

print("-" * 40)
print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("-" * 40)

print("Enter a number btw. 1 and 3 to select:", end=" ")
choice = input().strip()

if not choice.isdigit() or not (1 <= int(choice) <= 3):
    print("Invalid choice, terminating the program..")
    exit()

text = TEXTS[int(choice) - 1]
words = text.split()

num_words = len(words) 
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_words = sum(1 for word in words if word.islower())
numeric_strings = [int(word) for word in words if word.isdigit()] 
sum_numbers = sum(numeric_strings)

word_lengths = {}
for word in words:
    clean_word = word.strip(r"$%&'()*+,-./:;<#=>?@[\]^_`{|}~")
    length = len(clean_word)
    if length > 0:
        word_lengths[length] = word_lengths.get(length, 0) + 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length in sorted(word_lengths):
    print(f"{length:>2}| {'*' * word_lengths[length]:<12} |{word_lengths[length]}")