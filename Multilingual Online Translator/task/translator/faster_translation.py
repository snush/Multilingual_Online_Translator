#  Stage 6/7: Faster translation
import requests as requests
from bs4 import BeautifulSoup
import sys

languages = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew', 7: 'Japanese',
             8: 'Dutch', 9: 'Polish', 10: 'Portuguese', 11: 'Romanian', 12: 'Russian', 13: 'Turkish'}


def welcome():
    args = sys.argv
    source_language = args[1]
    target_language = args[2]
    word = args[3]
    return [source_language, target_language, word]


def translation(source_language, target_language, word, count):
    url = f'https://context.reverso.net/translation/{source_language.lower()}-{target_language.lower()}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    print(f'{target_language} Translations:')
    write_to_file(f'{target_language} Translations:', word)
    words = [word.text.strip() for word in soup.find_all('a', {'class': 'translation'})]
    for index in range(1, min(len(words), count + 1)):
        print(words[index])
        write_to_file(words[index], word)

    print(f'\n{target_language} Examples:')
    write_to_file(f'\n{target_language} Examples:', word)
    examples_from = [example.text.strip() for example in soup.find_all('div', {'class': 'src'}) if example.text.strip()]
    examples_to = [example.text.strip() for example in soup.find_all('div', {'class': 'trg'}) if example.text.strip()]
    for index in range(min(len(examples_to), count)):
        print(f'{examples_from[index]}\n{examples_to[index]}\n')
        write_to_file(f'{examples_from[index]}\n{examples_to[index]}\n', word)


def write_to_file(result, word):
    with open(f'{word}.txt', 'a', encoding='utf-8') as final_result:
        final_result.write(f'{result}\n')


def main():
    greeting = welcome()
    source_language = greeting[0]
    target_language = greeting[1]
    word = greeting[2]
    if target_language == 'all':
        for key in languages.keys():
            if languages[key] != source_language:
                translation(source_language, languages[key], word, count=1)
    else:
        translation(source_language, target_language, word, count=5)


if __name__ == "__main__":
    main()
