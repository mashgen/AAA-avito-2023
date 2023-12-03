import pytest

from one_hot_encoder import fit_transform

TEST_INPUT = ["My", "name", "is", "Maria", "it", "is", "usual", "name"]
EXPECTED_OUTPUT = [
    ("My", [0, 0, 0, 0, 0, 1]),
    ("name", [0, 0, 0, 0, 1, 0]),
    ("is", [0, 0, 0, 1, 0, 0]),
    ("Maria", [0, 0, 1, 0, 0, 0]),
    ("it", [0, 1, 0, 0, 0, 0]),
    ("is", [0, 0, 0, 1, 0, 0]),
    ("usual", [1, 0, 0, 0, 0, 0]),
    ("name", [0, 0, 0, 0, 1, 0]),
]


def test_empty_input():
    assert fit_transform([]) == []


def test_one_word():
    assert fit_transform("test") == [("test", [1])]


def test_multiple_words_as_list():
    assert fit_transform(TEST_INPUT) == EXPECTED_OUTPUT


def test_multiple_words_as_args():
    assert fit_transform(*TEST_INPUT) == EXPECTED_OUTPUT


def test_incorrect_input():
    with pytest.raises(
        TypeError,
        match="expected at least 1 arguments, got 0"
    ):
        fit_transform()
