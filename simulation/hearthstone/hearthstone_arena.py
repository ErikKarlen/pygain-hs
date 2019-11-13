import random


class HearthstoneArena:

    def __init__(self, hearthstone_cards, arena_class=[], deck=[], deck_size=30):
        self.hearthstone_cards = hearthstone_cards
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
        return self._random_arena_card()[0]

    def _random_class(self):
        return random.choice(self.hearthstone_cards.classes_list())

    def _random_arena_card(self, samples=1):
        return self.hearthstone_cards.arena_cards_list().sample(samples).index.values
