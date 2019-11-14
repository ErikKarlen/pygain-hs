import time
from game.hearthstone import Cards, Arena


# Testing code
cards = Cards('data/hearthstone/cards.collectible.json')

t_start = time.time()

arena = Arena(cards)

arena.simulate_normal()

print("Arena Classes: {}".format(arena.arena_class))
for n, card_id in enumerate(arena.deck):
    print("Arena Card {:>2}: [ {:<9}: {} / {} ]".format(
        n+1, card_id, cards.get_card_class(card_id), cards.get_card_name(card_id)))

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
