################################################################################
################	Species management section	################
################################################################################

def speciesFromBlocks( blocks, development=None, name=None ):
	'''Receives either a dict or a list as input to generate new species data'''
	from .tools import dev_cost, list_product
	
	if development != None:
		blocks = {}
		for x in development:
			if x in blocks:
				blocks[x] += 1
			else:
				blocks[x] = 1
	
	if type(blocks)==dict:
		if sum([1 if type(x)==int and type(blocks[x])==int else 0 for x in blocks]) < len(blocks):
			print('ERROR: speciesFromBlocks(dict) expects a dict with integer keys and values')
			return None
		# convert dict into list
		blocks = [blocks[x+1] if (x+1) in blocks else 1 for x in range(max(blocks.keys()))]
	elif type(blocks)==list:
		if sum([1 if type(x)==int else 0 for x in blocks]) < len(blocks):
			print('ERROR: speciesFromBlocks(list) expects a list with integer values')
			return None
	else:
		print('ERROR: speciesFromBlocks(...) expects one argument, dict or list')
		return None
	
	total = sum(blocks)
	stages = total - len(blocks)
	active = len(blocks) - blocks.count(1)
	level_multiplier = dev_cost(blocks)
	life_stage = stages * active
	species = {
		'blocks': blocks,
		'total': total,
		'active': active,
		'stages': stages,
		'power': {
			'max': list_product(blocks),
			'mean': max(blocks) + sum([1 for x in blocks if 1<x])-1, # subtracts the recount of max value
			'cost': level_multiplier
		},
		'life': {
			'stage': life_stage,
			'span': level_multiplier * life_stage,
			'adult': life_stage * min([(x+1) for x in range(len(blocks)) if blocks[x]>1]),
			'senior': life_stage * sum([(x+1) for x in range(len(blocks)) if blocks[x]>1])
		},
		'name': name if name!=None else 'unkwnown'
	}
	
	if development == None:
		aux = [x-1 for x in blocks]
		development = [x+1 for x in range(len(aux))]
		count = stages
		while count > 0:
			for x in xrange(len(aux)):
				if aux[x]>0:
					aux[x] -= 1
					count -= 1
					development.append(x+1)
				if count == 0:
					break
	
	species['development'] = development
	return species

class Species:
	'''Species class: each living character must be associated with one'''
	
	known = {} # class member, not instantiated per object
	
	def FromBlocks( self, blocks, development=None, name=None ):
		'''Receives either a dict or a list as input to generate new species data'''
		species = speciesFromBlocks( blocks, development, name)
		self.blocks = species['blocks']
		self.chroma = len(self.blocks)
		self.total = species['total']
		self.active = species['active']
		self.stages = species['stages']
		self.power = species['power']
		self.life = species['life']
		self.name = species['name']
		self.development = species['development']
		return self
	
	def StatusFromAge(self, today, birthday):
		'uses the arguments as today and birthday to calculate respective to the species'
		from math import floor, ceil
		from status import Status
		from datetime import date
		
		if type(today)!=date or type(birthday)!=date:
			print('ERROR: at least one of the dates was in the wrong format. Please use datetime.date')
			return None
		
		of_age = birthday.replace(year=birthday.year+self.life['adult'])
		diff_today = (today - birthday).days
		diff_of_age = (of_age - birthday).days
		# check for early return
		if diff_today >= diff_of_age:
			return Status(measure=self.power['mean'], development=self.development)
		
		power = floor( (self.power['mean'] * diff_today) / float(diff_of_age) )
		days_to_power = int( ceil( power * float(diff_of_age) / self.power['mean'] ) )
		diff_today -= days_to_power
		diff_of_age = int( ceil( (power+1) * float(diff_of_age) / self.power['mean'] ) ) - days_to_power
		xp_to_next = (self.power['cost']*(power+1)*diff_today) / float(diff_of_age)
		
		return Status(measure=int(power), xp=int(xp_to_next), development=list(self.development))
	
	def __init__(self, **kwargs):
		self.FromBlocks(kwargs.get('blocks', None), kwargs.get('development', list(range(1,24)) + [2,3,3,2,2]), kwargs.get('name', 'Sapiens'))
		if self.name not in Species.known:
			Species.known[self.name] = self
	
	def __str__(self):
		msg = [ 'Specie: {0}'.format(self.name),
			'\tlife: {0}'.format(self.life),
			'\tpower: {0}'.format(self.power),
			'\tdevelopment: (1..{0}) + {1}'.format(self.chroma, self.development[self.chroma:]),
		]
		return '\n'.join(msg)
	
	def __repr__(self):
		return '{0} (max {1}y)'.format(self.name, self.life['span'])

################################################################################
Species() # this call creates the Sapiens species
Species(development= list(range(1,24)) + [2,3,2], name='Afar')
Species(development= list(range(1,24)) + [2,3,3], name='Floren')
Species(development= list(range(1,24)) + [2,3,3,2], name='Orthias')
Species(development= list(range(1,24)) + [2,3,2,2,2], name='Neander')
Species(development= list(range(1,24)) + [2,3,3,2,2,2], name='Norsk')
Species(development= list(range(1,24)) + [2,3]*3, name='Gyges')
Species(development= list(range(1,24)) + [2,1,3,3,2], name='Latius')
Species(development= list(range(1,24)) + [4,2,3,3,2], name='Dutch')
################################################################################
