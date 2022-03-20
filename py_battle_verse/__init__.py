################################################################################
#   Base file for prototyping Package BattleVerse
################################################################################

from . import status # imports nothing else
from . import tools # imports nothing else
from . import directions # imports nothing else

from . import character # imports from status
from . import technique # imports from status
from . import style # imports from technique

Character = character.Character

__test__ = {
	'status': status,
}

def _test(verbose=True):
	import doctest
	for name, mod in __test__.items():
		doctest.testmod(m=mod, verbose=verbose)
