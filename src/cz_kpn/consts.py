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
