import numpy as np


class SimpleEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = len(word2vec)

    def fit(self, X, y):
        return self

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words.split(', ') if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in X])
