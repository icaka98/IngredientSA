from sklearn.decomposition import PCA
import pickle
import matplotlib.pyplot as plt
from tqdm import tqdm

if __name__ == '__main__':
    w2v_model = pickle.load(open('../models/word2vec_ing.sav', 'rb'))

    X = w2v_model[w2v_model.wv.vocab]

    print('PCA creation.')

    pca = PCA()
    result = pca.fit_transform(X)

    print('Plot scatering.')

    #plt.scatter(result[:, 0], result[:, 1])

    print('Vocabulary words annotation on plot.')

    print(w2v_model.similarity('chocolate', 'white chocolate'))
    print(w2v_model.similarity('chocolate', 'dark chocolate'))
    print(w2v_model.similarity('chocolate', 'cream'))
    print(w2v_model.similarity('chocolate', 'cake'))
    print(w2v_model.similarity('chocolate', 'salt'))
    print(w2v_model.similarity('chocolate', 'coffee'))
    print(w2v_model.similarity('chocolate', 'chocolate cookie'))

    print(w2v_model.most_similar('chocolate'))
    print(w2v_model.most_similar('beef'))

    words = [
        'chocolate', 'vanilla', 'pastry',
        'beef', 'pork', 'rice'
    ]

    for i, word in enumerate(tqdm(list(w2v_model.wv.vocab))):
        if word in words:
            plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    print(list(w2v_model.wv.vocab)[:100])

    print('Showing plot.')

    plt.show()
