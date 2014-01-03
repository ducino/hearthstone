# coding: utf-8
"""
Drops you in an IPython shell where you can manipulate the list of cards.

Filter <cards> using expressions like:
[card.name for card in cards if card.contains("secret")]
[card.name for card in cards if card.cls == "warrior"]
[(card.name, card.dmg) for card in cards if card.mana == 2]

"""
import json
from hearthstone import Card

def load_cards(filename):
	cards = []
	with open(filename, "r") as input:
		cards_data = json.load(input)
		for card_data in cards_data:
			cards.append(Card(card_data))
	return cards

def  main():
	cards = load_cards("cards.json")
	print __doc__
	import IPython
	IPython.embed()

if __name__ == "__main__":
	main()