################################################################################
#   Base file for prototyping Package BattleVerse
################################################################################

from .character import Character
from . import status

__test__ = {
	'status': status,
}

def _test(verbose=True):
	import doctest
	for name, mod in __test__.items():
		doctest.testmod(m=mod, verbose=verbose)
