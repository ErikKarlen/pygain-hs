from urllib.request import Request, urlopen
import json
import numpy as np
import pandas as pd


class Cards:

    def __init__(self, cards_file=None, buckets_file=None):
        if cards_file:
            # Use local file with card data
            json_file = open(cards_file, encoding='utf-8')
            self.all_cards_df = pd.DataFrame(json.load(json_file))
        else:
            # Fetch card data over Internet
            req = Request('http://api.hearthstonejson.com/v1/35747/enUS/cards.collectible.json',
                          headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(req).read()
            self.all_cards_df = pd.DataFrame(json.loads(source))

        all_heroes = self.get_cards(card_type=['HERO'])
        self.heroes_df = all_heroes.loc[all_heroes['cost'].isnull()]

        if buckets_file:
            bucket_cards = pd.read_csv(buckets_file)
            bucket_cards.columns = ['cardClass', 'name', 'bucket', 'halfBucket']
            bucket_cards['cardClass'] = bucket_cards['cardClass'].str.upper()
            self.all_cards_df = pd.merge(self.all_cards_df, bucket_cards, how='outer', on=['cardClass', 'name'])
            self.arena_cards = self.all_cards_df.loc[self.all_cards_df['bucket'].notnull()]
            buckets = self.arena_cards['bucket'].value_counts()
            buckets = pd.concat([buckets, self.arena_cards['halfBucket'].value_counts()], axis=1)
            buckets['bucketSize'] = buckets.apply(lambda row: row.bucket
                                                  if np.isnan(row.halfBucket)
                                                  else row.halfBucket, axis=1)
            del buckets['bucket']
            del buckets['halfBucket']
            self.buckets = buckets.copy()

    def get_cards(self, card_class=None, cost=None, card_id=None, rarity=None,
                  card_set=None, card_type=None, mechanics=None, attack=None, health=None):
        cards = self.all_cards_df.copy()
        if card_class:
            cards = cards.loc[cards['cardClass'].isin(card_class)]
        if cost:
            cards = cards.loc[cards['cost'].isin(cost)]
        if card_id:
            cards = cards.loc[cards['id'].isin(card_id)]
        if rarity:
            cards = cards.loc[cards['rarity'].isin(rarity)]
        if card_set:
            cards = cards.loc[cards['set'].isin(card_set)]
        if card_type:
            cards = cards.loc[cards['type'].isin(card_type)]
        if mechanics:
            cards = cards.loc[cards['mechanics'].isin(mechanics)]
        if attack:
            cards = cards.loc[cards['attack'].isin(attack)]
        if health:
            cards = cards.loc[cards['health'].isin(health)]

        return cards
