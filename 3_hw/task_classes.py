from typing import List


class CountVectorizer:
    """
    Transform categorial features to numeric form
    by replacing words in corpus with its count.
    """

    def __init__(self, lowercase=True):
        self.lowercase = lowercase

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Extract unique features from corpus and transform
        to numeric vectors.
        Args: corpus - all texts.
        Return: matrix with shape N*M:
        N - amount of texts, M - amount of unique words,
        matix[i,j] = count of word_j in text_i.
        """
        self.feature_names = []
        self.matrix = []
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
            self.matrix.append(list(cur_vector.values()))
        return self.matrix

    def get_feature_names(self) -> List[str]:
        """
        Return: list of unique categorial features.
        """
        return self.feature_names


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
