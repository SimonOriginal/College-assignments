import nltk
import json
import re
from nltk.tokenize import word_tokenize
from collections import Counter
from deep_translator import GoogleTranslator
from tqdm import tqdm

nltk.download('punkt')

# открытие файла
with open("text.txt", "r", encoding="utf-8") as file:
    # чтение текста из файла
    text = file.read()

# удаление знаков препинания из текста
text = re.sub(r'[^\w\s]', '', text)

# токенизация (разбиение текста на слова)
tokens = word_tokenize(text)

# подсчет количества повторений каждого слова
word_counts = Counter(tokens)

# перевод каждого слова и сохранение его переводов в словарь
translations = {}
for word in tqdm(set(tokens), desc="Перевод слов"):
    try:
        # перевод слова на несколько языков
        translations[word] = GoogleTranslator(source='auto', target='ru').translate(word)
    except:
        # если возникает ошибка при переводе, записываем None
        translations[word] = None

# сортировка слов по убыванию частоты использования
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# создание списка словарей для записи в файл JSON
data = []
for word, count in sorted_words:
    translation = translations.get(word)
    data.append({"word": word, "count": count, "translation": translation})

# сохранение результатов в файл формата JSON
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent = 4, ensure_ascii=False)

print("Результаты сохранены в файле result.json")
input()
