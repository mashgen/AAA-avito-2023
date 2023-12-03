from typing import List
import math


class CountVectorizer:
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self.feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        matrix = []
        for line in corpus:
            if self.lowercase:
                line = line.lower()
            words = line.split()
            for word in words:
                if word not in self.feature_names:
                    self.feature_names.append(word)
        for line in corpus:
            if self.lowercase:
                line = line.lower()
            words = line.split()
            cur_vector = dict.fromkeys(self.feature_names, 0)
            for word in words:
                cur_vector[word] += 1
            matrix.append(list(cur_vector.values()))
        return matrix

    def get_feature_names(self):
        return self.feature_names


def tf_transform(count_matrix):
    tf_matrix = []
    for arr in count_matrix:
        all_words = 0
        for elem in arr:
            all_words += elem * (elem > 0)
        curr_arr = []
        for elem in arr:
            curr_arr.append(round(elem / all_words, 3))
        tf_matrix.append(curr_arr)
    return tf_matrix


def idf_transform(count_matrix):
    all_text = len(count_matrix)
    all_words = [0 for _ in range(len(count_matrix[0]))]
    for arr in count_matrix:
        for i in range(len(arr)):
            all_words[i] += arr[i] > 0
    idf_matrix = [
        round(math.log((all_text + 1) / (word + 1)) + 1, 3)
        for word in all_words
    ]
    return idf_matrix


class TfidfTransformer:
    def fit_transform(self, count_matrix):
        tf_matrix = tf_transform(count_matrix)
        idf_list = idf_transform(count_matrix)
        for i in range(len(tf_matrix)):
            for j in range(len(tf_matrix[0])):
                tf_matrix[i][j] = round(tf_matrix[i][j] * idf_list[j], 3)
        return tf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self, lowercase=True):
        super().__init__(lowercase)
        self.tfidftransformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tfidftransformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    # print(vectorizer.get_feature_names())
    # print(count_matrix)
    tf_matrix = tf_transform(count_matrix)
    # print(tf_matrix)
    idf_matrix = idf_transform(count_matrix)
    # print(idf_matrix)

    # transformer = TfidfTransformer()
    # tfidf_matrix = transformer.fit_transform(count_matrix)
    # print(tfidf_matrix)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
