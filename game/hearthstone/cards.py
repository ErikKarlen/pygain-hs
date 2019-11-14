from urllib.request import Request, urlopen
import json
import pandas as pd


class Cards:

    def __init__(self, cards_file, web_fetch=False):
        # Use local file with card data
        json_file = open(cards_file, encoding='utf-8')
        self.cards_df = pd.DataFrame(json.load(json_file))

        # Fetch card data over Internet
        if web_fetch:
            req = Request('http://api.hearthstonejson.com/v1/35747/enUS/cards.collectible.json',
                          headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(req).read()
            self.cards_df = pd.DataFrame(json.loads(source))

    def classes_list(self):
        return pd.Series(self.cards_df.loc[self.cards_df['type'] == 'HERO']['cardClass'].unique())

    def get_cards(self, card_class=[], cost=[], card_id=[], rarity=[],
                  set=[], type=[], mechanics=[], attack=[], health=[]):
        cards = self.cards_df.copy()
        if card_class:
            cards = cards.loc[cards['cardClass'].isin(card_class)]
        if cost:
            cards = cards.loc[cards['cost'].isin(cost)]
        if card_id:
            cards = cards.loc[cards['id'].isin(card_id)]
        if rarity:
            cards = cards.loc[cards['rarity'].isin(rarity)]
        if set:
            cards = cards.loc[cards['set'].isin(set)]
        if type:
            cards = cards.loc[cards['type'].isin(type)]
        if mechanics:
            cards = cards.loc[cards['mechanics'].isin(mechanics)]
        if attack:
            cards = cards.loc[cards['attack'].isin(attack)]
        if health:
            cards = cards.loc[cards['health'].isin(health)]

        return cards
