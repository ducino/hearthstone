from __future__ import print_function

class Card(object):
	'''
	Sample:
	{
        "collectible": 1, 
        "set": 3,     # Invalid, Test_Temporary, Core, Expert1, Reward, Missions, Demo, None, Cheat, Blank, Debug_SP, Promo, FP1, PE1, FP2, PE2, Credits
        "name": "Edwin VanCleef", 
        "faction": 3, # Invalid, Horde, Alliance, Neutral
        "elite": 1,   # as well as Legendary
        "quality": 5, # Invalid, Free, Common, Rare, Epic, Legendary
        "image": "EX1_613", 
        "description": "Combo: Gain +2/+2 for each card played earlier this turn.", 
        "classs": 4,  # Invalid, Warrior=1, Paladin, Hunter, Rogue, Priest, Warlock=7, Shaman, Mage, Druid=11 
        "attack": 2, 
        "cost": 3, 
        #"race": 0,   # Invalid, BloodElf, Draenei, Dwarf, Gnome, Goblin, Human, NightElf, Orc, Tauren, Troll, Undead, Worgen, Goblin2, Murloc, Demon, Scourge, Mechanical, Elemental, Ogre, Pet, Totem, Nerubian, Pirate, Dragon 
        "health": 2, 
        "popularity": 749, 
        "type": 4,    # Invalid, Game, Player, Hero, Minion, Ability, Enchantment, Weapon, Item, Token, Hero_Power 
        "id": 306, 
        "icon": "inv_misc_ticket_tarot_beasts_01"
        }	
	'''
	def __init__(self, data):
		self.name = data["name"]
		self.mana = data["cost"]
		self.attack = data.get("attack", 0)
		self.health = data.get("health", 0)
		self.type = data["type"]
		self.race = data.get("race", 0)
		self.cls = data.get("classs", 0)
		self.set = data["set"]
		self.quality = data["quality"]
		self.desc = data.get("description", "")
		self.image = data["image"]
	
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