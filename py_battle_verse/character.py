################################################################################
#   Character Class and utilities
################################################################################

__all__ = ['Character']

import datetime as date_time
date = date_time.date
time = date_time.time
datetime = date_time.datetime
timedelta = date_time.timedelta
timezone = date_time.timezone

class Character:
	"""base class for character creation in RPG"""
	
	def __init__(self, **kwargs):
		from .status import BattleStatus as bstat
		from .tools import str_to_dev
		from .species import Species
		from .style import Style
		
		self.name = kwargs.get('name', 'Nanashi')
		self.birth_date = kwargs.get('birth', datetime.now() - timedelta(days=366*18))
		self.ki = kwargs.get('ki', bstat(strengh=5, speed=5, resistence=5))
		self.species = kwargs.get('species', [ Species.known['Sapiens'] ])
		self.styles = kwargs.get('style', [ Style(name=self.name, sequence=str_to_dev(self.name)) ])
		self.development = []
	
	def __str__(self):
		profile = [
			"\nName: " + self.name,
			"\tBirthday: " + self.birth_date.strftime("%d/%m/%Y"),
			"\tKi: " + self.ki.__repr__(),
		] + [
			'\t'+line for spec in self.species
			for line in str(spec).splitlines()
		] + [
			'\t'+line for st in self.styles
			for line in str(st).splitlines()
		]
		
		return "\n".join( profile )
	
	def __repr__(self):
		return "[{0}] {1} Ki:{2}".format(self.species[0].name, self.name, self.ki.power)
