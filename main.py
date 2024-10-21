# подготовка текста к анализу
from string import punctuation
text = input("Введите текст: ")
text = text.lower()

for char in punctuation:
    text = text.replace(char, " ")

words = text.split()


word_frequency = {}
for i in range(len(words)):
    word_frequency[words[i]] = word_frequency.get(words[i], 0) + 1

# вывод результатов
print("Количество разных слов:", len(set(words)))
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")