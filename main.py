# подготовка текста к анализу
from string import punctuation
text = input("Введите текст: ")
text = text.lower()

for char in punctuation:
    text = text.replace(char, " ")

words = text.split()

word_length = {}
word_frequency = {}
for i in range(len(words)):
    word_frequency[words[i]] = word_frequency.get(words[i], 0) + 1
    if not words[i] in word_length:
        word_length[words[i]] = len(words[i])

# вывод результатов
print("Количество разных слов:", len(set(words)))
print(f"Слово с максимальным количеством букв: {max(word_length, key=word_length.get)}")
print(f"Слово с минимальным количеством букв: {min(word_length, key=word_length.get)}")
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")