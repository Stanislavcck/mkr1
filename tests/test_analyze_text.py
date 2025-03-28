import pytest
import re
from analyze_text import read_file, count_words, count_sentences, count_words_and_sentences


@pytest.fixture
def test_file(tmpdir):
    test_file = tmpdir.join("example_text.txt")
    content = "Hello world! This is a test. How are you? Great! ..."
    test_file.write(content)
    return test_file


def test_read_file(test_file):
    content = read_file(str(test_file))
    assert content == "Hello world! This is a test. How are you? Great! ..."


@pytest.mark.parametrize("text, expected_word_count", [
    ("Hello world! This is a test.", 6),
    ("One more test case.", 4),
    ("", 0)
])
def test_count_words(text, expected_word_count):
    assert count_words(text) == expected_word_count


@pytest.mark.parametrize("text, expected_sentence_count", [
    ("Hello world! This is a test.", 2),
    ("Is it working? Yes, it is.", 2),
    ("", 0)
])
def test_count_sentences(text, expected_sentence_count):
    assert count_sentences(text) == expected_sentence_count


def test_count_words_and_sentences(test_file):
    words_count, sentences_count = count_words_and_sentences(str(test_file))
    assert words_count == 9
    assert sentences_count == 4
