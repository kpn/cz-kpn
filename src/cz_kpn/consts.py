NEW = "NEW"
BREAK = "BREAK"
OPT = "OPT"
FIX = "FIX"
CHANGE = "CHANGE"

NEW_DESCR = (
    "New functionality, fully backwards compatible (new endpoint, service, feature)"
)
BREAK_DESCR = "Change which breaks compatibility with previous versions"
CHANGE_DESCR = (
    "Indicates a backwards incompatible change (endpoint removed, output changes)"
)
OPT_DESCR = (
    "A backwards compatible change, usually internal optimisations, "
    "refactored code or added tests."
)
FIX_DESCR = (
    "A backwards compatible change that fixes something that was "
    "broken or not functioning properly"
)

BUMP_PATTERN = r"^(NEW|CHANGE|FIX|OPT|BREAK)"
COMMIT_PARSER = r"^(?P<change_type>NEW|CHANGE|FIX|OPT|BREAK)(?:\((?P<scope>[^()\r\n]*)\)|\()?:?\s(?P<message>.+)"  # noqa
COMMIT_PARSER_STRICT = r"(?P<keyword>BREAK|CHANGE|NEW|FIX|OPT)(\((?=[a-z]))?(?P<scope>(?<=\()(test|ci|docs|build)(?=\)))?((?<=[a-z])\))?: .{3,79} (?P<ticket>\(#[A-Z]+-[0-9]+\)|\(#[0-9]+\))"  # noqa


## CUSTOM SETTINGS KEYS
STRICT_CHECK = "kpn_strict_check"
COMMIT_URL = "kpn_commit_url"
APP_NAME = "kpn_app_name"
