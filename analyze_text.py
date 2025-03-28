import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(text):
    words = re.split(r'[ ,:;]+', text.strip())
    return len([word for word in words if word])


def count_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+|\.\.\.', text.strip())
    return len([s for s in sentences if s])


def count_words_and_sentences(file_path):
    text = read_file(file_path)
    _words_count = count_words(text)
    _sentences_count = count_sentences(text)
    return _words_count, _sentences_count


if __name__ == "__main__":
    filename = r"D:\univ\CI.CDLabs\mkr1\example_text.txt"
    words_count, sentences_count = count_words_and_sentences(filename)
    print(f"Кількість слів: {words_count}")
    print(f"Кількість речень: {sentences_count}")