import random


class Arena:

    def __init__(self, cards, arena_class=[], deck=[], deck_size=30):
        self.cards = cards  # Cards object with Hearthstone cards
        self.arena_class = arena_class  # List of strings with arena run's classes
        self.deck = deck  # List of card IDs for arena run
        self.deck_size = deck_size

    def simulate_normal(self):
        self.arena_class = self.select_class()
        for i in range(len(self.deck), self.deck_size):
            self.deck.append(self.select_deck_card())

    def select_class(self):
        return [self._random_class()]

    def select_deck_card(self):
        arena_cards = self.cards.arena_cards_list()
        card_classes = self.arena_class.copy()
        card_classes.append('NEUTRAL')
        arena_cards = arena_cards.loc[arena_cards['cardClass'].isin(card_classes)]
        return arena_cards.sample(1).index.values[0]

    def _random_class(self, samples=1):
        return random.choice(self.cards.classes_list())

    def _random_arena_card(self, samples=1):
        return self.cards.arena_cards_list().sample(samples).index.values
