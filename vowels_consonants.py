"""Made by https://github.com/CyberDemon-crypto"""
alphabet = {"Русский": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "English": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
vowel = {"Русский": "АОУЫЭЯЁЮИЕ", "English": "AEIOU"}
consonant = {"Русский": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ", "English": "BCDFGHJKLMNPQRSTVWXYZ"}
br = 'y'


def cont_req(func_name):
    br = input("Continue?[Y/N]\n"
               "--> ").capitalize()
    if br == 'N' or br == 'Н':
        return 0
    elif br == 'Y' or br == 'Д':
        func_name()


def vowel_or_consonant():
    letter = str(input("Check ")).capitalize()
    if letter.capitalize() in vowel[language]:
        print(f"{letter.capitalize()} is vowel")
    elif letter.capitalize() in consonant[language]:
        print(f"{letter.capitalize()} is consonant")
    else:
        print("Please write a letter")
        vowel_or_consonant()
    cont_req(vowel_or_consonant)


def vc_count():
    word = input("Put in the word or phrase: ")
    v = 0
    c = 0
    n = 0
    sp = 0
    for i in word.upper():
        if i in vowel[language]:
            v += 1
        elif i in consonant[language]:
            c += 1
        elif i in alphabet[language]:
            n += 1
        elif i == ' ':
            sp += 1
    print(f" ________________\n"
          f"/ {'Phrase' if sp else 'Word'}: {word}     \n"
          f"| Vowels: {v}      \n"
          f"| Consonants: {c}  \n"
          f"| Total Letters: {v+c+n}\n"
          f"\\_______________/")
    cont_req(vc_count)


while 1:
    print("[1]Check if letter is vowel or consonant\n"
          "[2]Number of vowels and consonants in word or phrase\n"
          "[3]Display available languages\n"
          "[4]Quit")
    choice = input("--> ")
    if choice == '1':
        while 1:
            language = str(input("Select language: ")).capitalize()
            if language not in alphabet:
                break
            else:
                vowel_or_consonant()
    elif choice == '2':
        while 1:
            language = str(input("Select language: ")).capitalize()
            if language not in alphabet:
                break
            else:
                vc_count()
    elif choice == '3':
        for i in alphabet:
            print(i, end=", ")
        print("The End(^,^)\n"
              "---")
    elif choice == '4':
        exit("End of Program.")
