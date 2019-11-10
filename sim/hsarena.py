import time
import random
import json
import pandas as pd


class HSArena:

    def __init__(self, cards_df, arena_class=[], deck=[], deck_size=30):
        self.cards_df = cards_df  # Pandas DataFrame with card data
        self.arena_class = arena_class  # cardClass string of hero(s)
        self.deck = deck  # List of card IDs
        self.deck_size = deck_size

    def simulate_normal(self):
        self.arena_class = self.select_class()
        for i in range(len(self.deck), self.deck_size):
            self.deck.append(self.select_deck_card())

    def select_class(self):
        return self._random_class()

    def select_deck_card(self):
        return self._random_deck_card()

    def _random_class(self):
        return random.choice(self._class_list())

    def _random_deck_card(self):
        return self._deck_cards_list().sample(1).index[0]

    def _class_list(self):
        return self.cards_df.loc[self.cards_df['type'] == 'HERO']['cardClass'].unique()

    def _deck_cards_list(self):
        return self.cards_df.loc[self.cards_df['type'].isin(['SPELL', 'MINION', 'ENCHANTMENT', 'WEAPON'])]


jsonFile = open('../cards.collectible.json', encoding='utf-8')
cards_df = pd.DataFrame(json.load(jsonFile)).set_index('id')

t_start = time.time()

arena = HSArena(cards_df)

arena.simulate_normal()

print(arena.arena_class)
for card in arena.deck:
    print(cards_df.loc[card]['name'])

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
