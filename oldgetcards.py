# coding: utf-8
import urllib
import json
from BeautifulSoup import BeautifulSoup

def get_url_contents(url):
	url_handle = urllib.urlopen(url)
	return url_handle.read()

def get_table_rows(contents):
	bs = BeautifulSoup(contents)
	table = bs.find(id="myTable")
	return table.findAll("tr")

def get_cells(row):
	return row.findAll("td")

def parse_contents(contents):
	cards = []
	rows = get_table_rows(contents)
	for row in rows:
		cells = get_cells(row)
		if len(cells) > 0:
			# Ignore first column
			cells.pop(0)
			card_data = [cell.text for cell in cells]
			# Get class from img tag, alt attribute
			img = cells[1].find("img")
			if img:
				card_data[1] = img.attrs[1][1]
			cards.append(card_data)
	return cards

def write_to_file(cards, filename):
	with open(filename, "w") as out:
		json.dump(cards, out, indent=4)

def main():
	print "Downloading data.."
	contents = get_url_contents("http://hearthstonecardlist.com/")
	print "Parsing.."
	cards = parse_contents(contents)
	filename = "cards.json"
	print "Writing to {}".format(filename)
	write_to_file(cards, filename)
	print "Done"
	

if __name__ == "__main__":
	main()