################################################################################
#   Base file for prototyping Package BattleVerse
################################################################################

from . import directions # imports nothing else
from . import status # imports nothing else

from . import tools # imports from directions
from . import technique # imports from status

from . import species # imports from tools
from . import style # imports from tools, technique

from . import character # imports from status, species, style

_m_list = [directions, status, tools, technique, species, style, character]
Technique = technique.Technique
Species = species.Species
Character = character.Character

__test__ = {
	'status': status,
}

def reload():
	global Technique, Species, Character
	from importlib import reload
	for m in _m_list:
		reload(m)
	Technique = technique.Technique
	Species = species.Species
	Character = character.Character

def _test(verbose=True):
	import doctest
	for name, mod in __test__.items():
		doctest.testmod(m=mod, verbose=verbose)
