################################################################################
################	Status structures	################
################################################################################

'''This module offers two main classes:
	- one raw for battle matters
	- and a more elaborated for character file and progression

example usage:

>>> BattleStatus(strength=2, speed=2, resistance=5)
[3.0] (2, 2, 5)

>>> BattleStatus(strength=0, speed=0, resistance=6) * 2
[4.0] (0, 0, 12)
'''

class BattleStatus:
	'''Minimal status information for immediate actions
	'''
	def __init__(self, **kwargs):
		self.strength = kwargs.get('strength', 0)
		self.speed = kwargs.get('speed', 0)
		self.resistance = kwargs.get('resistance', 0)
		self.power = 0 # set in self.update_power()
		
		self.update_power()
	
	def __repr__(self):
		return '[{0}] ({1}, {2}, {3})'.format(self.power, self.strength, self.speed, self.resistance)
	
	def update_power(self):
		self.power = sum([self.strength, self.speed, self.resistance]) // 3
		return self.power
	
	def update(self, atk=0, spd=0, res=0):
		self.strength = atk
		self.speed = spd
		self.resistance = res
		self.update_power()
		return self
	
	def as_list(self):
		return [self.strength, self.speed, self.resistance]
	
	def as_direction(self):
		return [self.update_power()] + self.as_list()
	
	def __iadd__(self, bat_stat):
		self.strength += bat_stat.strength
		self.speed += bat_stat.speed
		self.resistance += bat_stat.resistance
		self.update_power()
		return self
	
	def __add__(self, bat_stat):
		result = BattleStatus(strength=self.strength, speed=self.speed, resistance=self.resistance)
		result += bat_stat
		return result
	
	def __radd__(self, bat_stat):
		return bat_stat.__add__(self)
	
	def __isub__(self, bat_stat):
		self.strength -= bat_stat.strength
		self.speed -= bat_stat.speed
		self.resistance -= bat_stat.resistance
		self.update_power()
		return self
	
	def __sub__(self, bat_stat):
		result = BattleStatus(strength=self.strength, speed=self.speed, resistance=self.resistance)
		result -= bat_stat
		return result
	
	def __rsub__(self, bat_stat):
		return bat_stat.__sub__(self)
	
	def __imul__(self, value):
		self.strength *= value
		self.speed *= value
		self.resistance *= value
		self.update_power()
		return self
	
	def __mul__(self, value):
		result = BattleStatus(strength=self.strength, speed=self.speed, resistance=self.resistance)
		result *= value
		return result
	
	def __rmul__(self, value):
		return self.__mul__(value)
	
	def __eq__(self, bat_stat):
		return [x==y for x,y in zip(*[self.as_list(), bat_stat.as_list()])].count(True) == 3
	
	def __lt__(self, bat_stat):
		return [x<y for x,y in zip(*[self.as_list(), bat_stat.as_list()])].count(True) == 3
	
	def __le__(self, bat_stat):
		return [x<=y for x,y in zip(*[self.as_list(), bat_stat.as_list()])].count(True) == 3
	
	def __gt__(self, bat_stat):
		return [x>y for x,y in zip(*[self.as_list(), bat_stat.as_list()])].count(True) == 3

	def __ge__(self, bat_stat):
		return [x>=y for x,y in zip(*[self.as_list(), bat_stat.as_list()])].count(True) == 3

def _test(verbose=False):
	'''could not get it to work from within module when __name__ is not __main__'''
	import doctest
	doctest.testmod(m=status, verbose=verbose)
