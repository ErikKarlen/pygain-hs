from urllib.request import Request, urlopen
import json
import pandas as pd


class HearthstoneCards:

    def __init__(self, cards_file, fetch=False):
        # Use local file with card data
        json_file = open(cards_file, encoding='utf-8')
        self.cards_df = pd.DataFrame(json.load(json_file)).set_index('id')

        # Fetch card data over Internet
        if fetch:
            req = Request('http://api.hearthstonejson.com/v1/35747/enUS/cards.collectible.json',
                          headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(req).read()
            self.cards_df = pd.DataFrame(json.loads(source)).set_index('id')

    def classes_list(self):
        return self.cards_df.loc[self.cards_df['type'] == 'HERO']['cardClass'].unique()

    def arena_cards_list(self):
        return self.cards_df.loc[self.cards_df['type'].isin(['SPELL', 'MINION', 'ENCHANTMENT', 'WEAPON'])]
