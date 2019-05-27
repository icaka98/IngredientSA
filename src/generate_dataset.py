import random

import numpy
import pandas as pd
from sklearn.utils import shuffle


def get_data(filename):
    data = pd.read_csv('../data/' + filename + '.csv')
    return data[['Ingredients']]


def get_dict_ing_count(df_ing):
    ing_counts = dict()

    total_cts = 0
    for i, row in df_ing.iterrows():
        ing_len = len(row['ing'].split(', '))
        total_cts += 1

        if ing_len not in ing_counts.keys():
            ing_counts[ing_len] = 1
        else:
            ing_counts[ing_len] += 1

    max_cnt = max(ing_counts.keys())

    for i in range(max_cnt + 1):
        if i not in ing_counts.keys():
            ing_counts[i] = 0

    for key in ing_counts.keys():
        ing_counts[key] /= total_cts
        print(str(key) + ': ' + str(ing_counts[key]) + ' times.')

    p = []
    for i in range(max_cnt + 1):
        p.append(ing_counts[i])

    print(p)

    return max_cnt, p


def clean_df(df_clean):
    df_clean.rename(columns={'Ingredients': 'ing'}, inplace=True)

    df_clean['ing'] = df_clean['ing'].str.lower()
    # df_clean['ing'] = df_clean['ing'].str.split(', ')
    df_clean['ing'] = df_clean['ing'].astype(str)
    df_clean = df_clean.dropna()
    df_clean = df_clean[pd.notnull(df_clean['ing'])]
    df_clean['label'] = 'pos'

    return df_clean


def get_neg_data(df_pos):
    max_cnt, p = get_dict_ing_count(df_pos)

    all_ing = set()
    for index, row in df_pos.iterrows():
        for el in row['ing'].split(', '):
            all_ing.add(el)

    data_neg = []

    for i in range(len(df_pos)):
        len_ing = numpy.random.choice(numpy.arange(0, max_cnt+1), p=p)
        ings = ', '.join(random.choices(list(all_ing), k=len_ing))
        data_neg.append({'ing': ings, 'label': 'neg'})

    return pd.DataFrame(data_neg)


if __name__ == '__main__':
    df_epi = get_data('epirecipes')
    df_wha = get_data('whatscooking')
    df_bal = get_data('balkan_recipes')

    df_epi = clean_df(df_epi)
    df_wha = clean_df(df_wha)
    df_bal = clean_df(df_bal)

    df_epi_neg = get_neg_data(df_epi)
    df_wha_neg = get_neg_data(df_wha)
    df_bal_neg = get_neg_data(df_bal)

    pd.concat([df_epi, df_wha, df_bal]).to_csv('../data/data_pos.csv')
    pd.concat([df_epi_neg, df_wha_neg, df_bal_neg]).to_csv('../data/data_neg.csv')

    result = pd.concat([df_epi, df_wha, df_bal, df_epi_neg, df_wha_neg, df_bal_neg])
    result = result.sample(frac=1).reset_index(drop=True)

    # Get 15% test data
    percent15 = int(float(len(result)) * 15.0 / 100.0)
    print('15% pecent of the data count: ' + str(percent15))

    result[percent15:].reset_index(drop=True).to_csv('../data/data_pos_neg.csv')
    result[:percent15].to_csv('../data/test_data_pos_neg.csv')
