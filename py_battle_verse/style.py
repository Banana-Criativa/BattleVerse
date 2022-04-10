################################################################################
################	Styles management section	################
################################################################################

from .tools import fit_list, steps_from_direction, shift_sequence, add_triplets
from .technique import Technique

class Style:
	'''Represents the whole data associated with a fighting and training of a martial-arts style
	Comprises a name, ranks, techniques' detailed data and "directions" for training'''
	
	# def GenerateFromSequence(self, sequence=[1]):
	def from_sequence(self, sequence=[1]):
		self.ranks = fit_list(sequence)
		# replicating list of technique levels to wrap around status
		if len(self.ranks)%3==0:
			self.directions = self.ranks + shift_sequence(self.ranks, -1) + shift_sequence(self.ranks, -2)
		else:
			self.directions = self.ranks*3
		# makes a 4-by-ranks matrix with column-0 being status power's lower bound
		self.directions = [ self.directions[3*x:3*x+3] for x in range(len(self.ranks)) ]
		
		# get techniques
		steps = []
		for x in self.directions:
			steps += steps_from_direction(x)
		aux = [ sum(self.ranks[:x]) for x in range(len(self.ranks)+1) ]
		# temporarily store triplets to get or instantiate techniques
		self.techniques = [ add_triplets( steps[3*aux[x]:3*aux[x+1]] ) for x in range(len(aux)-1) ]
		# now we get the final form for this data field
		self.techniques = [
			Technique.get(
				name='{0}_{1}'.format(self.name, x),
				attack=self.techniques[x][0],
				speed=self.techniques[x][1],
				resistance=self.techniques[x][2]
			)
			for x in range(len(self.techniques))
		]
		
		# get directions' milestones
		self.directions = [ add_triplets( self.directions[:x+1] ) for x in range(len(self.directions))]
		
		return self
	
	def check_consistency(self):
		return (sum(self.ranks),)*3 == add_triplets([t.as_list() for t in self.techniques])
	
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', 'default_minimum')
		self.ranks = 0 # filled by calling from_sequence()
		self.directions = [] # filled by calling from_sequence()
		self.techniques = [] # filled by calling from_sequence()
		self.from_sequence( kwargs.get('sequence', [1]) )
	
	def __repr__(self):
		return '{0} ({1} ranks)'.format(self.name, len(self.ranks))
	
	def __str__(self):
		msg = [ 'Style: {0} ({1})'.format(self.name, sum(self.ranks)),
			'ranks ({0}): {1}'.format(len(self.ranks), self.ranks),
		] + [
			'\t{0}'.format(t) for t in self.techniques
		]
		return '\n'.join(msg)

################################################################################
kihap_styles = [
	Style(name='K1', sequence=[1]),
	Style(name='K2', sequence=[2]),
	Style(name='K3', sequence=[1,2]),
	Style(name='K4', sequence=[1,2,1]),
	Style(name='K5', sequence=[1,2,2]),
	Style(name='K6', sequence=[1,2,3]),
	Style(name='K8', sequence=[2,2,4]),
	Style(name='K10', sequence=[1,2,3,4]),
]
################################################################################
