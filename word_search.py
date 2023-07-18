"""
Генератор принимает на вход имя файла или файловый объект
и список слов для поиска. Генератор перебирает строки файла
и возвращает только те из них, где встретилось хотя бы одно из слов для поиска.
Поиск выполняется по полному совпадению слова без учета регистра.
"""
import io
import string


def word_search(file, search_words, encoding="utf-8"):
    """
    гениратор ищит строки с заданными словами в файле
    """
    if isinstance(file, str):
        file = open(file, mode='r', encoding=encoding)
    search_words = set(map(lambda element: element.lower(), search_words))
    for line in file:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        line_for_search = set(line.lower().translate(table).split())
        if search_words & line_for_search:
            yield line
    if not isinstance(file, io.StringIO):
        file.close()
