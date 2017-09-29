import gzip
import json
import pandas as pd
import pymongo
from pymongo import MongoClient


def parse(path, encoding):

    with open(path) as data_file:
        data = json.load(data_file, encoding=encoding)
    print type(data)
    return data


def get_df(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')


def insert_item_metadata(meta_collection, meta_path):
    item_meta_data = []

    for item_meta in parse(meta_path):
        item_meta_data.append(item_meta)
        meta_collection.insert_many(item_meta_data)
        item_meta_data = []

    if not meta_collection:
        meta_collection.insert_many(item_meta_data)

    meta_collection.create_index([('asin', pymongo.ASCENDING)])


def insert_item_review(review_collection, review_path):
    item_reviews = []

    for review in parse(review_path):
        if 'unixReviewTime' in review.keys():
                if len(item_reviews) < 1000:
                    item_reviews.append(review)
                else:
                    review_collection.insert_many(item_reviews)
                    item_reviews = []

    if not item_reviews:
        review_collection.insert_many(item_reviews)






