################################################################################
#   Base file for prototyping Package BattleVerse
################################################################################

from . import status
from . import character
from . import tools
from . import directions

Character = character.Character

__test__ = {
	'status': status,
}

def _test(verbose=True):
	import doctest
	for name, mod in __test__.items():
		doctest.testmod(m=mod, verbose=verbose)
