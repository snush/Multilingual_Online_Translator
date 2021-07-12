#  Stage 2: Over the internet 
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
print(page.status_code, 'OK')

print('Translations')
soup = BeautifulSoup(page.content, 'html.parser')
words = [word.text.strip() for word in soup.find_all('a', {'class': 'translation'})]
print(words)

examples = [example.text.strip() for example in chain(*[examples for examples in
            zip(soup.find_all('div', {'class': 'src'}), soup.find_all('div', {'class': 'trg'}))])]
print(examples)
