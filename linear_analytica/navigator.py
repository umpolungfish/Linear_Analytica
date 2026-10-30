"""
Linear Analytica — navigator bridge to the IG catalog.

Maps Minoan Linear A sign families through the IG crystal,
decoding accounting computations from structural tuples.
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

_NAV_PATH = Path(__file__).parent.parent.parent / 'imscribing_grammar' / 'navigators'
if str(_NAV_PATH) not in sys.path:
    sys.path.insert(0, str(_NAV_PATH))

import cl8nk_navigator as _nav

_PRIM_KEYS = _nav.PRIMITIVE_KEYS

_SIGN_FAMILIES = {
    'AB001': 'linear_a_AB001',
    'AB002': 'linear_a_AB002',
    'AB003': 'linear_a_AB003',
    'AB004': 'linear_a_AB004',
    'AB005': 'linear_a_AB005',
    'AB006': 'linear_a_AB006',
    'AB007': 'linear_a_AB007',
    'AB008': 'linear_a_AB008',
    'AB009': 'linear_a_AB009',
    'AB010': 'linear_a_AB010',
    'AB011': 'linear_a_AB011',
    'AB012': 'linear_a_AB012',
    'AB013': 'linear_a_AB013',
    'AB014': 'linear_a_AB014',
    'AB015': 'linear_a_AB015',
    'AB016': 'linear_a_AB016',
    'AB017': 'linear_a_AB017',
    'AB018': 'linear_a_AB018',
    'AB019': 'linear_a_AB019',
    'AB020': 'linear_a_AB020',
    'AB021': 'linear_a_AB021',
    'AB022': 'linear_a_AB022',
    'AB023': 'linear_a_AB023',
    'AB024': 'linear_a_AB024',
    'AB025': 'linear_a_AB025',
    'AB026': 'linear_a_AB026',
    'AB027': 'linear_a_AB027',
    'AB028': 'linear_a_AB028',
    'AB029': 'linear_a_AB029',
    'AB030': 'linear_a_AB030',
    'AB031': 'linear_a_AB031',
    'AB032': 'linear_a_AB032',
    'AB033': 'linear_a_AB033',
    'AB034': 'linear_a_AB034',
    'AB035': 'linear_a_AB035',
    'AB036': 'linear_a_AB036',
    'AB037': 'linear_a_AB037',
    'AB038': 'linear_a_AB038',
    'AB039': 'linear_a_AB039',
    'AB040': 'linear_a_AB040',
    'AB041': 'linear_a_AB041',
    'AB042': 'linear_a_AB042',
    'AB043': 'linear_a_AB043',
    'AB044': 'linear_a_AB044',
    'AB045': 'linear_a_AB045',
    'AB046': 'linear_a_AB046',
    'AB047': 'linear_a_AB047',
    'AB048': 'linear_a_AB048',
    'AB049': 'linear_a_AB049',
    'AB050': 'linear_a_AB050',
    'AB051': 'linear_a_AB051',
    'AB052': 'linear_a_AB052',
    'AB053': 'linear_a_AB053',
    'AB054': 'linear_a_AB054',
    'AB055': 'linear_a_AB055',
    'AB056': 'linear_a_AB056',
    'AB057': 'linear_a_AB057',
    'AB058': 'linear_a_AB058',
    'AB059': 'linear_a_AB059',
    'AB060': 'linear_a_AB060',
    'AB061': 'linear_a_AB061',
    'AB062': 'linear_a_AB062',
    'AB063': 'linear_a_AB063',
    'AB064': 'linear_a_AB064',
    'AB065': 'linear_a_AB065',
    'AB066': 'linear_a_AB066',
    'AB067': 'linear_a_AB067',
    'AB068': 'linear_a_AB068',
    'AB069': 'linear_a_AB069',
    'AB070': 'linear_a_AB070',
    'AB071': 'linear_a_AB071',
    'AB072': 'linear_a_AB072',
    'AB073': 'linear_a_AB073',
    'AB074': 'linear_a_AB074',
    'AB075': 'linear_a_AB075',
    'AB076': 'linear_a_AB076',
    'AB077': 'linear_a_AB077',
    'AB078': 'linear_a_AB078',
    'AB079': 'linear_a_AB079',
    'AB080': 'linear_a_AB080',
}

_SEMANTIC_CATEGORIES = {
    'AB001': 'human/man',
    'AB002': 'woman',
    'AB004': 'ox/head',
    'AB006': 'fig',
    'AB008': 'oil',
    'AB009': 'wine',
    'AB010': 'grain',
    'AB013': 'saffron',
    'AB028': 'bronze',
    'AB030': 'wool',
    'AB031': 'flax',
    'AB037': 'sheep',
    'AB054': 'total',
    'AB055': 'deficit',
    'AB057': 'surplus',
    'AB059': 'land/estate',
    'AB065': 'slave',
    'AB067': 'ship',
    'AB070': 'sacred',
    'AB072': 'king',
    'AB076': 'offering',
    'AB080': 'tribute',
}

_ACCOUNTING_ROLES = {
    'AB054': 'aggregator',
    'AB055': 'deficit_marker',
    'AB057': 'surplus_marker',
    'AB080': 'inflow',
    'AB059': 'domain',
    'AB053': 'unit',
}

def _tuple_from_entry(entry: dict) -> list[str]:
    t = entry.get('tuple') or entry.get('raw_tuple', {})
    if isinstance(t, dict):
        return [t.get(k, '—') for k in _PRIM_KEYS]
    if isinstance(t, (list, tuple)):
        return list(t)
    return []

def _tuple_dict(entry: dict) -> dict:
    t = entry.get('tuple') or {}
    if isinstance(t, dict):
        return t
    return {k: v for k, v in zip(_PRIM_KEYS, t)}

def lookup(sign_code: str) -> dict:
    """
    Look up a Linear A sign in the IG catalog.
    """
    _nav.load_catalog()
    name = _SIGN_FAMILIES.get(sign_code.upper())
    if name is None:
        raise KeyError(f'Sign not found: {sign_code!r}')

    entry = _nav.resolve_system(name)
    if entry is None:
        raise KeyError(f'Sign not in catalog: {name!r}')

    t = _tuple_from_entry(entry)
    sem = _SEMANTIC_CATEGORIES.get(sign_code.upper(), 'unknown')
    acct = _ACCOUNTING_ROLES.get(sign_code.upper(), None)

    return {
        'sign_code': sign_code.upper(),
        'name': name,
        'semantic': sem,
        'accounting_role': acct,
        'tuple': t,
        'tuple_dict': _tuple_dict(entry),
        'description': entry.get('description', ''),
    }

def list_signs(category: Optional[str] = None) -> list[dict]:
    """List all Linear A signs, optionally filtered by semantic category."""
    _nav.load_catalog()
    results = []
    for code in _SIGN_FAMILIES:
        try:
            result = lookup(code)
            if category is None or result['semantic'] == category:
                results.append(result)
        except KeyError:
            pass
    return results

def analyse_tablet(transcription: str) -> dict:
    """
    Analyse a Linear A tablet transcription.
    Takes a string of sign codes (e.g. 'AB001 AB054 AB008 AB030 AB055')
    and returns the structural computation.
    """
    codes = transcription.strip().split()
    signs = []
    for code in codes:
        try:
            signs.append(lookup(code))
        except KeyError:
            signs.append({'sign_code': code, 'semantic': 'unknown', 'tuple': []})

    # Detect accounting operations
    aggregators = [s for s in signs if s.get('accounting_role') == 'aggregator']
    deficits = [s for s in signs if s.get('accounting_role') == 'deficit_marker']
    surpluses = [s for s in signs if s.get('accounting_role') == 'surplus_marker']

    return {
        'transcription': transcription,
        'sign_count': len(signs),
        'signs': signs,
        'aggregators': len(aggregators),
        'deficits': len(deficits),
        'surpluses': len(surpluses),
        'is_accounting': len(aggregators) > 0 or len(deficits) > 0 or len(surpluses) > 0,
    }
