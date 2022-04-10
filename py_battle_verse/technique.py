################################################################################
################	Techniques management section	################
################################################################################

from .status import BattleStatus

class Technique:
	'''A single technique with its data'''
	
	known = {} #static member
	
	# static member
	def get(**kwargs):
		bst = BattleStatus(
			strength=kwargs.get('attack', 0),
			speed=kwargs.get('speed', 0),
			resistance=kwargs.get('resistance', 0)
		)
		kbs = tuple(bst.as_direction())
		if kbs not in Technique.known:
			return Technique(**kwargs)
		else:
			return Technique.known[kbs]
	
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
		return self.status.strength
	
	def speed(self):
		return self.status.speed
	
	def resistance(self):
		return self.status.resistance
	
	def power(self):
		return self.status.power
		
	def __init__(self, **kwargs):
		# create new technique
		bst = BattleStatus(
			strength=kwargs.get('attack', 0),
			speed=kwargs.get('speed', 0),
			resistance=kwargs.get('resistance', 0)
		)
		self.name = kwargs.get('name', 'unknown')
		self.status = bst
		# and register for future consultation
		kbs = tuple(bst.as_direction())
		Technique.known[kbs] = self
	
	def __repr__(self):
		return '{0} {1}'.format(self.name, self.status)

################################################################################
