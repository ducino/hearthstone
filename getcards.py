# coding: utf-8
import urllib
import json
from BeautifulSoup import BeautifulSoup

def get_url_contents(url):
	url_handle = urllib.urlopen(url)
	return url_handle.read()

def get_table_rows(contents):
	bs = BeautifulSoup(contents)
	table = bs.find(id="cards")
	rows = table.findAll("tr")
	# Remove header row
	rows.pop(0)
	return rows

def get_cells(row):
	return row.findAll("td")

def parse_rows(cards, rows):
	def _cleanup(text):
		return text.replace("&nbsp;", "").\
					replace("&#x27;", "'").\
					replace("&quot;", '"').\
					replace("&amp;", "&").\
					replace("&lt;", "<").\
					replace("&gt;", ">")
	def _field(index, key):
		card_data[key] = _cleanup(cells[index].text)
	for row in rows:
		cells = get_cells(row)
		card_data = {}
		_field(0, "name")
		_field(1, "type")
		_field(2, "class")
		_field(3, "cost")
		_field(4, "damage")
		_field(5, "health")
		cards.append(card_data)
	return cards

def write_to_file(cards, filename):
	with open(filename, "w") as out:
		json.dump(cards, out, indent=4)
		
def parse_cards(cards, url):
	contents = get_url_contents(url)
	rows = get_table_rows(contents)
	parse_rows(cards, rows)

def main():
	cards = []
	for i in range(1, 7):
		parse_cards(cards, "http://www.hearthpwn.com/cards?display=1&page={}".format(i))
	write_to_file(cards, "simple.json")

if __name__ == "__main__":
	main()