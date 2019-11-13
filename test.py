import time
from game_data.hearthstone import HearthstoneCards
from simulation.hearthstone import HearthstoneArena


# Testing code
cards = HearthstoneCards('cards.collectible.json')

t_start = time.time()

arena = HearthstoneArena(cards)

arena.simulate_normal()

print("Arena Class: arena.arena_class")
for n, card_id in enumerate(arena.deck):
    print("Arena card {}: {}".format(n, cards.get_card_name(card_id)))

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
