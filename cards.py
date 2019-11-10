from urllib.request import Request, urlopen
import json

# Fetch card data over Internet
"""
req = Request('http://api.hearthstonejson.com/v1/35747/enUS/cards.collectible.json',
                      headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
data = json.loads(source)
"""

# Use local file with card data
json_file = open('cards.collectible.json', encoding='utf-8')
data = json.load(json_file)

