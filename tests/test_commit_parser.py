import re

import pytest

try:
    from cz_kpn.consts import COMMIT_PARSER, COMMIT_PARSER_STRICT
except AttributeError:
    from cz_kpn.consts import COMMIT_PARSER, COMMIT_PARSER_STRICT

MESSAGE_AND_VALIDITY = [
    ("BREAK: New commit with break to bump auto-tag (#3625)", True),
    ("BREAK: Change foobar into quux (#DE-2053)", True),
    ("NEW: BaseView for all my generic functionality (#J-1)", True),
    ("NEW: FancyView using BaseView that does something fancy (#J-2)", True),
    ("OPT: Small fixes for the FancyView", True),
    ("FIX: Bug in the BaseView", True),
    ("OPT(test): Written unittests for the FancyView", True),
    ("FIX: Processed pull-request feedback", True),
    ("FIX: Missing mock data for FancyView and BaseView", True),
    ("FIX: Something completely unrelated", True),
    ("BREAK: Change foobar into quux (#DE-2053)", True),
    ("NEW: Add new InboxMessage and Image version (XXX-3083)", True),
    ("NEW XXX-2966 Add support for teams per campaign", True),
    ("NEW Add support for teams per campaign", True),
    ("feat: add stuff", False),
    ("Add README", False),
    ("fix stuff", False),
    ("foo(bar): pepe", False),
    ("FIX: ", False),
]


@pytest.mark.parametrize("message, result", MESSAGE_AND_VALIDITY)
def test_parser_regex(message, result):
    map_pat = re.compile(COMMIT_PARSER, re.MULTILINE)
    print(COMMIT_PARSER)
    message = map_pat.match(message)
    is_valid = bool(message)
    if is_valid:
        print(message.groupdict())

    assert is_valid == result


STRICT_MESSAGE_AND_VALIDITY = [
    ("BREAK: New commit with break to bump auto-tag (#3625)", True),
    ("BREAK: Change foobar into quux (#DE-2053)", True),
    ("NEW: BaseView for all my generic functionality (#J-1)", True),
    ("NEW: FancyView using BaseView that does something fancy (#J-2)", True),
    ("BREAK: Change foobar into quux (#DE-2053)", True),
    ("BREAK: Foo (#1)", True),
    ("BREAK: Foo (#99999999)", True),
    ("OPT: Small fixes for the FancyView", False),
    ("FIX: Bug in the BaseView", False),
    ("OPT(test): Written unittests for the FancyView", False),
    ("FIX: Processed pull-request feedback", False),
    ("FIX: Missing mock data for FancyView and BaseView", False),
    ("FIX: Something completely unrelated", False),
    ("NEW: Add new InboxMessage and Image version (XXX-3083)", False),
    ("NEW XXX-2966 Add support for teams per campaign", False),
    ("NEW Add support for teams per campaign", False),
    ("feat: add stuff", False),
    ("Add README", False),
    ("fix stuff", False),
    ("foo(bar): pepe", False),
    ("FIX: ", False),
]


@pytest.mark.parametrize("message, result", STRICT_MESSAGE_AND_VALIDITY)
def test_parser_regex_strict(message, result):
    map_pat = re.compile(COMMIT_PARSER_STRICT, re.MULTILINE)
    print(COMMIT_PARSER_STRICT)
    message = map_pat.match(message)
    is_valid = bool(message)
    if is_valid:
        print(message.groupdict())

    assert is_valid == result
