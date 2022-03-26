################################################################################
################	Techniques management section	################
################################################################################

from .status import BattleStatus

class Technique:
	'''A single technique with its data'''
	
	def can_use(self, conditioning, energy):
		'''can_use(conditioning, energy) -> boolean
		both arguments are of type Status
		returns True if the Technique can be wielded by these Stati'''
		return conditioning.battle_status >= self.status and energy.measure >= self.status.power
	
	def as_list(self):
		return self.status.as_list()
	
	def as_direction(self):
		return self.status.as_direction()
	
	def attack(self):
		return self.status.strengh
	
	def speed(self):
		return self.status.speed
	
	def resistence(self):
		return self.status.resistence
	
	def power(self):
		return self.status.power
	
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', 'unknown')
		self.status = BattleStatus(strengh=kwargs.get('attack', 0), speed=kwargs.get('speed', 0), resistence=kwargs.get('resistence', 0))
	
	def __repr__(self):
		return '{0} {1}'.format(self.name, self.status)

################################################################################
