#  Stage 1: Repeater
def repeater():
    language = input('Type "en" if you want to translate from French into English, '
                     'or "fr" if you want to translate from English into French:\n')
    word = input('Type the word you want to translate:\n')
    print(f'You chose "{language}" as a language to translate "{word}".')


repeater()
