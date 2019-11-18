import numpy as np
import pandas as pd


class Arena:
    # Latest arena rules: https://us.forums.blizzard.com/en/hearthstone/t/current-arena-rules/93

    DECK_SIZE = 30
    NUMBER_CARD_OPTIONS = 3
    NUMBER_CLASSES = 1
    NUMBER_CLASS_OPTIONS = 3
    SPECIAL_ROUNDS = [1, 10, 20, 30]

    def __init__(self, cards, arena_class=None, deck=None):
        self.cards = cards  # Cards object with Hearthstone cards
        self.arena_class = pd.DataFrame(columns=cards.all_cards_df.columns)  # DataFrame with arena class(es)
        self.deck = pd.DataFrame(columns=cards.all_cards_df.columns)  # DataFrame with cards in arena deck

    def simulate_normal(self):
        self.arena_class = self.class_selection()
        for i in range(len(self.deck), self.DECK_SIZE):
            self.deck = self.deck.append(self.deck_card_selection(i))

    def class_selection(self):
        return self.random_class_options().sample(1)

    def deck_card_selection(self, round_nbr):
        if round_nbr in self.SPECIAL_ROUNDS:
            return self.random_special_deck_card_options().sample(1)
        else:
            return self.random_normal_deck_card_options().sample(1)

    def random_normal_deck_card_options(self):
        arena_cards = self.cards.arena_cards
        classes = self.arena_class['cardClass'].values
        classes = np.append(classes, 'NEUTRAL')
        valid_cards = arena_cards.loc[arena_cards['cardClass'].isin(classes)]
        return arena_cards.sample(3)

    def random_special_deck_card_options(self):
        arena_cards = self.cards.arena_cards
        return arena_cards.sample(3)

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
