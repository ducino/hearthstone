import json
import re

def strip_html(text):
	return re.sub('<[^<]+?>', '', text)

def similar(one, other):
	return strip_html(one) == strip_html(other)

if __name__ == "__main__":
	
	with open("cards.json", "r") as input:
		current_cards = json.load(input)
	
	with open("simple.json", "r") as input:
		new_cards = json.load(input)
	
	for card in current_cards:
		id = card["id"]
		for new_card in new_cards:
			def _print_diff(key):
				print "---- Difference: {} ----".format(card["name"])
				print card[key]
				print new_card[key]
			if id == new_card["id"]:
				try:
					if not similar(card["description"], new_card["description"]):
						_print_diff("description")
					if card["cost"] != new_card["cost"]:
						_print_diff("cost")
					if card["mana"] != new_card["mana"]:
						_print_diff("mana")
					if card["health"] != new_card["health"]:
						_print_diff("health")
				except KeyError:
					pass
	
	