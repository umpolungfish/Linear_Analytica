"""Corpus front-end package. The compilation engine is the installed
`linear_a_engine` distribution; the session protocol is re-exported when that engine
ships one."""

from .navigator import lookup, list_signs, analyse_tablet
from . import navigator

# The engine ships as an installed package; its seven-gate session is optional
# and only some corpora implement it. Re-export it when present.
try:
    from linear_a_engine.session import LinearASession, SessionState  # noqa: F401
    _HAS_SESSION = True
except ImportError:
    _HAS_SESSION = False

__version__ = '1.0.0'

__all__ = ['lookup', 'list_signs', 'analyse_tablet', 'navigator']
if _HAS_SESSION:
    __all__ += ['LinearASession', 'SessionState']
