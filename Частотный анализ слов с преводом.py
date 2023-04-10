import nltk
import json
import re
from nltk.tokenize import word_tokenize
from collections import Counter
from deep_translator import GoogleTranslator

nltk.download('punkt')

# открытие файла
with open("text.txt", "r", encoding="utf-8") as file:
    # чтение текста из файла
    text = file.read()

# удаление знаков препинания из текста
text = re.sub(r'[^\w\s]', '', text)

# токенизация (разбиение текста на слова)
tokens = word_tokenize(text)

# перевод каждого слова и сохранение его переводов в словарь
translations = {}
for word in set(tokens):
    try:
        # перевод слова на несколько языков
        translations[word] = GoogleTranslator(source='auto', target='ru').translate(word)
    except:
        # если возникает ошибка при переводе, записываем None
        translations[word] = None

# сохранение результатов в файл формата JSON
data = {"word_counts": dict(Counter(tokens)), "translations": translations}

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Результаты сохранены в файле result.json")
