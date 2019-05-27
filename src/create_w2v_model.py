import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from tqdm import tqdm
from custom_models.SimpleEmbeddingVectorizer import SimpleEmbeddingVectorizer

if __name__ == '__main__':
    w2v_model = pickle.load(open('../models/word2vec_ing.sav', 'rb'))
    w2v_model = dict(zip(w2v_model.wv.index2word, w2v_model.wv.syn0))

    df_data = pd.read_csv('../data/data_pos_neg.csv')

    X = df_data['ing'].values.astype('U')
    y = df_data['label'].values.astype('U')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    print('Data is prepared.')

    pipeline = Pipeline([
        ('simple w2v vect', SimpleEmbeddingVectorizer(w2v_model)),
        ('rf_clf', RandomForestClassifier())
    ])

    print('Pipeline is created.')

    pipeline.fit(X_train, y_train)

    print('Training finished.')

    predicted = pipeline.predict(X_test)

    print(classification_report(y_test, predicted))
    print(confusion_matrix(y_test, predicted))

    print('Saving the model.')

    pickle.dump(pipeline, open('../models/word2vec_model.sav', 'wb'))

