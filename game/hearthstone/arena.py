import random


class Arena:
    # Latest arena rules: https://us.forums.blizzard.com/en/hearthstone/t/current-arena-rules/93

    DECK_SIZE = 30
    NUMBER_CARD_OPTIONS = 3
    NUMBER_CLASSES = 1
    NUMBER_CLASS_OPTIONS = 3

    def __init__(self, cards, arena_class=[], deck=[]):
        self.cards = cards  # Cards object with Hearthstone cards
        self.arena_class = arena_class  # List of strings with arena run's classes
        self.deck = deck  # List of card IDs for arena run

    def simulate_normal(self):
        self.arena_class = self.class_selection()
        for i in range(len(self.deck), self.DECK_SIZE):
            self.deck.append(self.deck_card_selection())

    def class_selection(self):
        return random.choice(self.class_options())

    def deck_card_selection(self):
        arena_cards = self.cards.get_cards(type=['SPELL', 'MINION', 'WEAPON'])
        card_classes = self.arena_class.copy()
        card_classes.append('NEUTRAL')
        arena_cards = arena_cards.loc[arena_cards['cardClass'].isin(card_classes)]
        return arena_cards.sample(1)

    def class_options(self):
        return self._random_hero(samples=self.NUMBER_CLASS_OPTIONS)

    def _random_hero(self, samples=1):
        if samples < 1:
            samples = 1
        elif samples > len(self.cards.classes_list()):
            samples = len(self.cards.classes_list())

        all_heroes = self.cards.classes_list()
        unique_classes = set(all_heroes['cardClass'].unique())
        random_classes = random.sample(unique_classes, samples)
        print(random_classes)
        for i in range(samples):
            random_heros.append(all_heroes.loc[all_heroes['cardClass'] ==
                                               random_classes[i]].sample(1))
        print(random_heros['name'])
        return random_heros

    def _random_arena_card(self, samples=1):
        return self.cards.get_cards(type=['SPELL', 'MINION', 'WEAPON']).sample(samples).index.values
