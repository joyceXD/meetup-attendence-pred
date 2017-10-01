import json
import pandas as pd
import re


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', raw_html)
    return clean_text


def flatten_dict(df, col):
    pd_new = pd.concat([df.drop(col, axis=1), df[col].apply(pd.Series)], axis=1)
    return pd_new


def flatten_list(df, col, reset_index=False):
    col_flat = pd.DataFrame([[i, x] 
                       for i, y in df[col].apply(list).iteritems() 
                           for x in y], columns=['I', col])
    col_flat = col_flat.set_index('I')
    df = df.drop(col, 1)
    df = df.merge(col_flat, left_index=True, right_index=True)
    if reset_index:
        df = df.reset_index(drop=True)
    return df


def get_df(path, encoding):
    i = 0
    df = {}
    for d in parse(path, encoding):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')


def parse(path, encoding):

    with open(path) as data_file:
        data = json.load(data_file, encoding=encoding)
    print type(data)
    return data

