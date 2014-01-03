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
	script = div.findNext("script")
	chunks = script.text.split(";")
	variable = ";".join(chunks[3:14])
	cards_json = variable[23:]
	valid_cards_json = cards_json.replace("popularity:", '"popularity":')
	return json.loads(valid_cards_json)

def write_to_file(cards, filename):
	with open(filename, "w") as out:
		json.dump(cards, out, indent=4)
		
def parse_cards(url):
	contents = get_url_contents(url)
	return get_cards_json(contents)

def main():
	cards = parse_cards("http://www.hearthhead.com/cards")
	write_to_file(cards, "simple.json")

if __name__ == "__main__":
	main()