################################################################################
################	general utilities section	################
################################################################################

def list_product(values):
	from functools import reduce # because python3 doesn't educate developers
	return reduce(lambda x, y: x*y, values)

# def stringToDevelopment( name ):
def str_to_dev(name):
	name = name.lower().split(' ')
	return [] if len(name)<1 else [ord(ch)-ord('a')+1 for ch in name[0]]

# def costFromDevelopment( development ):
def dev_cost(development):
	return max( sum([ (x+1)*(development[x]-1) for x in range(len(development))]), 1)

# def costFromDevelopmentDict( dev_dict ):
def dev_cost_dict(dev_dict):
	return max( sum([k*(v-1) for k,v in dev_dict.items()]), 1)

def add_triplets(triplets):
	return tuple(map(sum, zip(*triplets)))

def remove_listed_from_list(list_rem, list_from):
	list_from = list(list_from)
	for x in list_rem:
		try:
			list_from.remove(x)
		except:
			pass
	return list_from

def fit_list(sequence):
	total = sum(sequence)
	ranks = int(round(total**0.5))
	
	if len(sequence) >= ranks:
		tech = sequence[:ranks]
		for x in range(ranks, len(sequence)):
			tech[x%ranks] += sequence[x]
	elif len(sequence) < ranks:
		tech = split_list(sequence, ranks)
	
	return tech

def split_list(seq, ranks):
	count = len(seq)
	div = 1
	aux = [[x] for x in seq]
	indexes = range(len(seq))
	while count < ranks:
		div += 1
		for id in indexes:
			count -= len(aux[id]) - aux[id].count(0)
			q = seq[id] // div
			r = seq[id] % div
			aux[id] = [q+1 if x<r else q for x in range(div)]
			count += len(aux[id]) - aux[id].count(0)
			if count >= ranks:
				break
	
	count = len(aux[0])
	for x in aux:
		x.reverse()
		if len(x) < count:
			x.append(0)
	result = map(list, zip(*aux))
	
	return [r for q in result for r in q if r > 0]

def steps_from_direction(direction):
	result = []
	steps = (
		(1,0,0),
		(0,1,0),
		(0,0,1)
	)
	# try replacing list_product with product/GCD method
	threshold = list_product([x for x in direction if x!=0])
	# threshold = reduce(lambda x,y: x*y, [x for x in direction if x!=0])
	
	ordered_indexes = list(zip(*[direction, [0,1,2]]))
	ordered_indexes.sort()
	ordered_indexes = tuple(zip(*ordered_indexes))[1]
	
	p = [0, 0, 0]
	count = sum(direction)
	while count>0:
		for x in ordered_indexes:
			p[x] += direction[x]
		for x in ordered_indexes:
			if p[x]>threshold:
				p[x] -= threshold
				result.append( list(steps[x]) ) # list() constructor used to force deep-copy
				count -= 1
	
	return result

def get_direction_from_development(development):
	from . import directions
	return add_triplets( [directions.get_triplet(x) for x in development] )

def get_level(level, direction=[50,49,47], step=28):
	from math import ceil
	return tuple(map(int, [ceil(level*float(x)/step) for x in direction]))

################################################################################
