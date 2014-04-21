# coding: utf-8
import urllib
import json
from BeautifulSoup import BeautifulSoup

def get_url_contents(url):
	url_handle = urllib.urlopen(url)
	return url_handle.read()

def get_cards_json(contents):
	bs = BeautifulSoup(contents)
	div = bs.find(id="lv-hearthstonecards")
	text = div.findNext("script").text
	
	start = text.find("var hearthstoneCards")
	cards_json = text[text.find("[", start):text.find("]", start)+1]
	
	valid_cards_json = cards_json.replace("popularity:", '"popularity":')
	return json.loads(valid_cards_json)

def write_to_file(cards, filename):
	with open(filename, "w") as out:
		json.dump(cards, out, indent=4)
		
def parse_cards(url):
	contents = get_url_contents(url)
	return get_cards_json(contents)

def main():
	urlbase = "http://www.hearthhead.com/cards"
	# Card
	cards = parse_cards(urlbase)
	write_to_file(cards, "card.json")
	print "...Card done!"
	# Hero
	cards = parse_cards(urlbase + "?filter=type=3")
	write_to_file(cards, "hero.json")
	print "...Hero done!"
	# Hero Power
	cards = parse_cards(urlbase + "?filter=type=10")	
	write_to_file(cards, "hpower.json")
	print "...HeroPower done!"

if __name__ == "__main__":
	main()