import requests
from bs4 import BeautifulSoup

slang_dict = []

for letter in range(ord('А'), ord('а')):
    print(f'Parsing "{chr(letter)}"')
    for page in range(1, 35):
        url = f"https://slang.su/?page={page}&content={chr(letter)}*"
        contents = requests.get(url)
        soup = BeautifulSoup(contents.text, 'lxml')
        words = soup.find_all('span', class_='cap')
        for word in words:
            if 5 < len(word.text) < 12 and ' ' not in word.text:
                slang_dict.append(word.text)
    else:
        print('Pages parsed!')

    slang_dict = list(set(slang_dict))
    slang_dict.sort()

    with open('Slang_ru_dict.txt', 'a', encoding='utf-8') as output_file:
        output_file.write('\n'.join(slang_dict))

    slang_dict.clear()
    print('Added to TXT')

print('Success!')
