import time
import pandas as pd

import hearthstone as hs


t_start = time.time()

# Testing code
cards = hs.Cards(cards_file='data/cards.collectible.json', buckets_file='data/current_arena_cards.csv')
arena = hs.Arena(cards)
arena.simulate_normal()

print("Arena Classes: {}".format(arena.arena_class['name'].values))
for n, row in enumerate(arena.deck.iterrows()):
    card = row[1]
    print("Arena Card {:>2}: [ {:<7} / {} ]".format(n+1, card['cardClass'], card['name']))

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
