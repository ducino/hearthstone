from __future__ import print_function

class Card(object):
	def __init__(self, data):
		self.name = data["name"]
		self.mana = data["mana"]
		self.attack = data["attack"]
		self.health = data["health"]
		self.type = data["type"]
		self.race = data["race"]
		self.cls = data["class"]
		self.set = data["set"]
		self.quality = data["quality"]
		self.desc = data["description"]
	
	def __str__(self):
		text = []
		text.append(self.name)
		text.append(self.desc)
		text.append("{}, {} for {}".format(self.attack, self.health, self.mana))
		text.append(self.quality)
		text.append(self.cls)
		return "\n".join(text)

	def contains(self, keyword):
		return _contains(self.name, keyword) or\
			   _contains(self.cls, keyword) or\
			   _contains(self.quality, keyword) or\
			   _contains(self.type, keyword) or\
			   _contains(self.race, keyword) or\
			   _contains(self.desc, keyword)
	
def _contains(sentence, word):
	return sentence.lower().find(word.lower()) != -1