#  Stage 5: Simultaneous translation

import requests as requests
from bs4 import BeautifulSoup

languages = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew', 7: 'Japanese',
             8: 'Dutch', 9: 'Polish', 10: 'Portuguese', 11: 'Romanian', 12: 'Russian', 13: 'Turkish'}


def welcome():
    print("Hello, you're welcome to the translator. Translator supports:")
    print('\n'.join(f'{index}. {language}' for index, language in languages.items()))
    source_language = languages[int(input('Type the number of your language:\n'))]
    index = int(input("Type the number of a language you want to translate to or '0' to translate to all languages:\n"))
    target_language = languages[index] if index != 0 else 'All'
    word = input('Type the word you want to translate:\n')
    return [source_language, target_language, word]


def translation(source_language, target_language, word):
    url = f'https://context.reverso.net/translation/{source_language.lower()}-{target_language.lower()}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    words = [word.text.strip() for word in soup.find_all('a', {'class': 'translation'})]
    examples_from = [example.text.strip() for example in soup.find_all('div', {'class': 'src'}) if example.text.strip()]
    examples_to = [example.text.strip() for example in soup.find_all('div', {'class': 'trg'}) if example.text.strip()]
    return [words, examples_from, examples_to]


def display(target_language, words, examples_from, examples_to, word, count):
    message_1 = f'{target_language} Translations:\n'
    message_2 = f'\n'.join(words[index] for index in range(1, min(len(words), count + 1)))
    message_3 = f'\n\n{target_language} Examples:\n'
    message_4 = f'\n'.join(f'{examples_from[index]}\n{examples_to[index]}\n' for index in range(min(len(examples_to), count)))
    print(f'{message_1}{message_2}{message_3}{message_4}')
    save_to_file(f'{message_1}{message_2}{message_3}{message_4}\n', word)


def save_to_file(messages, word):
    with open(f'{word}.txt', 'a', encoding='utf-8') as file:
        file.write(messages)


def main():
    greeting = welcome()
    source_language, target_language, word = greeting[0], greeting[1], greeting[2]
    all_languages = {1: target_language} if target_language != 'All' else languages
    count = 5 if target_language != 'All' else 1
    for key in all_languages.keys():
        if all_languages[key] != source_language:
            data = translation(source_language, all_languages[key], word)
            words, examples_from, examples_to = data[0], data[1], data[2]
            display(all_languages[key], words, examples_from, examples_to, word, count)


if __name__ == "__main__":
    main()
    
