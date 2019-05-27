import pandas as pd
from gensim.models import word2vec
import pickle

if __name__ == '__main__':
    df_data = pd.read_csv('../data/data_pos_neg.csv')

    X = df_data['ing'].values.astype('U')
    y = df_data['label'].values.astype('U')

    sentences = list(map(lambda x: x.split(', '), X))

    num_features = 300  # Word vector dimensionality
    min_word_count = 2  # 50% of the corpus
    num_workers = 4  # Number of CPUs
    context = 10  # Context window size; let's use avg recipte size
    downsampling = 1e-3  # threshold for configuring which; higher-frequency words are randomly downsampled

    w2v_model = word2vec.Word2Vec(sentences, workers=num_workers,
                                  size=num_features, min_count=min_word_count,
                                  window=context, sample=downsampling)
    w2v_model.init_sims(replace=True)  # memory-efficient model (no further training)

    print('Model training finished.')

    print(w2v_model.most_similar('chocolate'))
    print(w2v_model.most_similar('feta cheese'))
    print(w2v_model.similarity('broccoli', 'cabbage'))
    print(w2v_model.similarity('cheese', 'tomato'))
    print(w2v_model.similarity('lemon', 'chocolate'))
    print(w2v_model.similarity('chicken', 'bacon'))

    pickle.dump(w2v_model, open('../models/word2vec_ing.sav', 'wb'))
