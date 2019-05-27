import pandas as pd
import dill as pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

if __name__ == '__main__':
    df_data = pd.read_csv('../data/data_pos_neg.csv')

    X = df_data['ing'].values.astype('U')
    y = df_data['label'].values.astype('U')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=lambda x: x.split(', '))),
        ('clf', RandomForestClassifier())
    ])

    pipeline.fit(X_train, y_train)

    predicted = pipeline.predict(X_test)

    print(classification_report(y_test, predicted))
    print(confusion_matrix(y_test, predicted))

    pickle.dump(pipeline, open('../models/bow_model.sav', 'wb'))
