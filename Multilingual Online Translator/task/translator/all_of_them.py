#  Stage 4: All of them
import requests as requests
from bs4 import BeautifulSoup

languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
             'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
print("Hello, you're welcome to the translator. Translator supports:")
for index in range(13):
    print(f'{index + 1}. {languages[index]}')

source_language = languages[int(input('Type the number of your language:\n')) - 1]
target_language = languages[int(input('Type the number of language you want to translate to:\n')) - 1]
word = input('Type the word you want to translate:\n')

url = f'https://context.reverso.net/translation/{source_language.lower()}-{target_language.lower()}/{word}'
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)

print(f'{target_language} Translations:')
soup = BeautifulSoup(page.content, 'html.parser')
words = [word.text.strip() for word in soup.find_all('a', {'class': 'translation'})]
for index in range(1, min(len(words), 6)):
    print(words[index])

print(f'\n{target_language} Examples:')
examples_from = [example.text.strip() for example in soup.find_all('div', {'class': 'src'}) if example.text.strip()]
examples_to = [example.text.strip() for example in soup.find_all('div', {'class': 'trg'}) if example.text.strip()]
for index in range(min(len(examples_to), 5)):
    print(f'{examples_from[index]}\n{examples_to[index]}\n')
