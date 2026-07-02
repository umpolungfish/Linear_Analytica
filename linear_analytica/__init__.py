from .navigator import lookup, list_signs, analyse_tablet
from . import navigator

import sys
from pathlib import Path
_ENGINE = Path(__file__).parent.parent.parent / 'lang' / 'linear-a-engine'
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from linear_a_engine.session import LinearASession, SessionState

__version__ = '1.0.0'
__all__ = [
    'LinearASession',
    'SessionState',
    'lookup',
    'list_signs',
    'analyse_tablet',
    'navigator',
]
