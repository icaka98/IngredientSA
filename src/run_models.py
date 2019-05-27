import pickle
import dill
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

if __name__ == '__main__':
    w2v_model = pickle.load(open('../models/word2vec_model.sav', 'rb'))
    w2v_tfidf_model = dill.load(open('../models/word2vec_tfidf_model.sav', 'rb'))
    bow_model = dill.load(open('../models/bow_model.sav', 'rb'))
    tfidf_model = dill.load(open('../models/tfidf_model.sav', 'rb'))

    all_models = [
        ('Word2Vec Simple Model', w2v_model),
        ('Word2Vec Tf-idf Model', w2v_tfidf_model),
        ('Bag-of-words model', bow_model),
        ('Tf-idf model', tfidf_model)
    ]

    df_test_data = pd.read_csv('../data/test_data_pos_neg.csv')

    X_test = df_test_data['ing'].values.astype('U')
    y_test = df_test_data['label'].values.astype('U')

    for model in all_models:
        print('--------------------------------------------------------------')
        print(model[0] + ' test set performance:')

        predicted = model[1].predict(X_test)

        print(classification_report(y_test, predicted))
        print(confusion_matrix(y_test, predicted))

    print('--------------------------------------------------------------\n\n')

    test_samples = [
        'salt, frozen lemon, corn, brandy, seed paste',
        'chocolate, sweet tomato, gross asparagus, small rice, fries',
        'grapes, apple, melon, orange juice, watermelon',
        'dark chocolate, tomato soup, chilli, onion, garlic',
        'chicken, lime, rice noodles, spaghetti',
        'chicken thighs, lime, milk, white cheese, wine, white chocolate',
        'sausage, mayonnaise, french fries, sweet chilli, green pepper',
        'brown bread, small rice, potatoes',
        'milk, tuna fish, lemon',
        'bread, rice, potatoes, milk, fish, chilli, onion, chocolate, garlic, tomatoes, feta cheese, pepper, humus',
        'chicken soup, mushrooms, sour cream',
        'rose leaves, coconut oil, chilli chocolate',
        'sesame, salt, orange, apple, melon',
        'azis, emilia, lorena, malkata, cheti, cheti, uchi, onion',
        'olive tapenade, bread',
        'chocolate mousse, tuna',
        'chocolate, tuna',
        'mousse, tuna',
        'chocolate tuna, tuna, chocolate',
        'vinegar, white wine, olive oil, lemon juice, garlic, black pepper, salt',
        'tuna, oil, onions, pears, tomatoes, oregano, sugar, flour, margarine, anchovy fillets, walnut',
        'turnip, cabbage, seed, watermelon, salt',
        'turnip, chocolate, vanilla, carrots',
        'coconut, caramel, chocolate, biscuits',
        'rice, bread, kiwi',
        'kiwi, pepper, avocado, tuna'
    ]

    w2v_pred = w2v_model.predict(test_samples)
    bow_pred = bow_model.predict(test_samples)
    w2v_tfidf_pred = w2v_tfidf_model.predict(test_samples)
    tfidf_pred = tfidf_model.predict(test_samples)

    for idx in range(len(test_samples)):
        print(str(idx) + ': w2v(' + w2v_pred[idx]
              + '), bow(' + bow_pred[idx] + ')'
              + ' w2v_tfidf(' + w2v_tfidf_pred[idx] + ')'
              + ' tfidf(' + tfidf_pred[idx] + ')'
              + '| ' + test_samples[idx])
