from numpy.testing import assert_allclose


from class_TF_IDF import (
    TfidfTransformer,
    TfidfVectorizer,
    idf_transform,
    tf_transform,
    CountVectorizer,
)

corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste",
]
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
]


def test_CountVectorizer():
    vectorizer = CountVectorizer()
    assert vectorizer.fit_transform(corpus) == count_matrix


def test_tf_transform():
    true = [
        [0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143],
    ]
    assert_allclose(tf_transform(count_matrix), true, rtol=0.1, atol=0.01)


def test_idf_transform():
    true = [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
    assert_allclose(idf_transform(count_matrix), true, rtol=0.1, atol=0.01)


def test_TfidfTransformer():
    transformer = TfidfTransformer()
    true = [
        [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    ]
    assert_allclose(
        transformer.fit_transform(count_matrix), true, rtol=0.1, atol=0.01
    )


def test_TfidfVectorizer():
    vectorizer = TfidfVectorizer()
    true = [
        [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    ]
    assert_allclose(
        vectorizer.fit_transform(corpus), true, rtol=0.1, atol=0.01
    )
