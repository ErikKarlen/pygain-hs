import numpy as np
import pandas as pd


class Arena:
    # Latest arena rules: https://us.forums.blizzard.com/en/hearthstone/t/current-arena-rules/93

    DECK_SIZE = 30
    NUMBER_CARD_OPTIONS = 3
    NUMBER_CLASSES = 1
    NUMBER_CLASS_OPTIONS = 3

    def __init__(self, cards, arena_class=None, deck=None):
        self.cards = cards  # Cards object with Hearthstone cards
        self.arena_class = pd.DataFrame(columns=cards.cards_df.columns)  # DataFrame with arena class(es)
        self.deck = pd.DataFrame(columns=cards.cards_df.columns)  # DataFrame with cards in arena deck

    def simulate_normal(self):
        self.arena_class = self.class_selection()
        for i in range(len(self.deck), self.DECK_SIZE):
            self.deck.append(self.deck_card_selection())

    def class_selection(self):
        return self.random_class_options().sample(1)

    def deck_card_selection(self):
        arena_cards = self.cards.get_cards(card_type=['SPELL', 'MINION', 'WEAPON'])
        card_classes = self.arena_class.copy()
        card_classes.append('NEUTRAL')
        arena_cards = arena_cards.loc[arena_cards['cardClass'].isin(card_classes)]
        return arena_cards.sample(1)

    def random_class_options(self):
        all_heroes = self.cards.get_cards(card_type=['HERO'])
        valid_heroes = all_heroes.loc[all_heroes['cost'].isnull()]
        unique_classes = all_heroes['cardClass'].unique()
        unique_valid_classes = list(set(unique_classes) - set(self.arena_class['cardClass'].values))
        random_classes = np.random.choice(unique_valid_classes, self.NUMBER_CLASS_OPTIONS, replace=False)

        random_heroes = pd.DataFrame(columns=all_heroes.columns)
        for i in range(self.NUMBER_CLASS_OPTIONS):
            random_hero = valid_heroes.loc[all_heroes['cardClass'] == random_classes[i]].sample(1)
            random_heroes = random_heroes.append(random_hero)

        return random_heroes

    def _random_arena_card(self, samples=1):
        return self.cards.get_cards(type=['SPELL', 'MINION', 'WEAPON']).sample(samples).index.values
