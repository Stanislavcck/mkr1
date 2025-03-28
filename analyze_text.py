import re

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(text):
    words = re.split(r'[ ,:;]+', text.strip())
    return len([word for word in words if word])


def count_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+|\.\.\.', text.strip())
    return len([s for s in sentences if s])