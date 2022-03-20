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
		self.name = kwargs.get('name', 'Nanashi')
		self.birth_date = kwargs.get('birth', datetime.now() - timedelta(days=366*18))
		self.ki = kwargs.get('ki', bstat(strengh=5, speed=5, resistence=5))
		self.development = []
	
	def __str__(self):
		profile = "\n".join( [
			"\n\tName: " + self.name,
			"\tBirthday: " + self.birth_date.strftime("%d/%m/%Y"),
			"\tKi: " + self.ki.__repr__() + "\n"
			"\tDevelopment: " + str(self.development) + "\n"
		] )
		
		return profile
	
	def __repr__(self):
		return "[{0}] {1} Ki:{2}".format("Human", self.name, self.ki.power)
