#  Stage 3: Translations
from itertools import chain

import requests as requests
from bs4 import BeautifulSoup

target_language = input('Type "en" if you want to translate from French into English, '
                        'or "fr" if you want to translate from English into French:\n')
word = input('Type the word you want to translate:\n')
print(f'You chose "{target_language}" as a language to translate "{word}".')

language_translation_pair = 'english-french' if target_language == 'fr' else 'french-english'
url = f'https://context.reverso.net/translation/{language_translation_pair}/{word}'
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
print(page.status_code, 'OK\n')

language = 'English' if target_language == 'en' else 'French'
print(f'{language} Translations:')
soup = BeautifulSoup(page.content, 'html.parser')
words = [word.text.strip() for word in soup.find_all('a', {'class': 'translation'})]
for index in range(1, 6):
    print(words[index])

print(f'\n{language} Examples:')
examples_from = [example.text.strip() for example in soup.find_all('div', {'class': 'src'}) if example.text.strip()]
examples_to = [example.text.strip() for example in soup.find_all('div', {'class': 'trg'}) if example.text.strip()]
for index in range(5):
    print(f'{examples_from[index]}\n{examples_to[index]}\n')
