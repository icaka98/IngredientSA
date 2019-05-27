import pickle
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from tqdm import tqdm
import matplotlib.patches as mpatches
import seaborn as sns

if __name__ == '__main__':
    w2v_model = pickle.load(open('../models/word2vec_ing.sav', 'rb'))

    corpus = sorted(tqdm(w2v_model.wv.vocab.keys()))

    print('Vocab sorted')

    emb_tuple = tuple([w2v_model[v] for v in corpus])
    X = np.vstack(tqdm(emb_tuple))

    print('TSNE plot prepare')

    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)

    print('Plotting')

    plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
    plt.show()
