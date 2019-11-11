import time
from sim.hearthstone.hearthstone_cards import HearthstoneCards
from sim.hearthstone.hearthstone_arena import HearthstoneArena


# Testing code
hearthstone_cards = HearthstoneCards('cards.collectible.json')

t_start = time.time()

arena = HearthstoneArena(hearthstone_cards)

arena.simulate_normal()

print(arena.arena_class)
for card in arena.deck:
    print(hearthstone_cards.cards_df.loc[card]['name'])

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
