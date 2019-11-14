import time
import game.hearthstone as hs


t_start = time.time()

# Testing code
cards = hs.Cards('data/hearthstone/cards.collectible.json')
arena = hs.Arena(cards)
arena.simulate_normal()

print("Arena Classes: {}".format(arena.arena_class))
for n, card in enumerate(arena.deck):
    print("Arena Card {:>2}: [ {:<9}: {:<7} / {} ]".format(n+1, card['id'].values[0], card['cardClass'].values[0],
                                                           card['name'].values[0]))

t_end = time.time() - t_start
print("\n--------------------------\nTIME: {}".format(t_end))
