import os
from collections.abc import Iterable, Mapping
from string import Template
from typing import Any

from commitizen import git
from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import required_validator
from commitizen.question import CzQuestion

from cz_kpn.consts import (
    BREAK,
    BREAK_DESCR,
    BUMP_PATTERN,
    COMMIT_PARSER,
    COMMIT_PARSER_STRICT,
    COMMIT_URL,
    FIX,
    FIX_DESCR,
    NEW,
    NEW_DESCR,
    OPT,
    OPT_DESCR,
    STRICT_CHECK,
)


def _parse_subject(text: str) -> str:
    value = text.strip(".").strip()
    msg = ""
    if not value:
        msg = "Subject is required."
    elif len(value) < 3:
        msg = "Subject must be at least 3 characters long."
    elif len(value) > 79:
        msg = "Subject must be at most 79 characters long."
    return required_validator(value, msg=msg)


class KPNCz(BaseCommitizen):
    bump_pattern = BUMP_PATTERN
    bump_map = {
        "CHANGE": "MAJOR",
        "BREAK": "MAJOR",
        "NEW": "MINOR",
        "OPT": "PATCH",
        "FIX": "PATCH",
    }
    bump_map_major_version_zero = {
        "CHANGE": "MINOR",
        "BREAK": "MINOR",
        "NEW": "MINOR",
        "OPT": "PATCH",
        "FIX": "PATCH",
    }
    changelog_pattern = BUMP_PATTERN
    commit_parser = COMMIT_PARSER
    change_type_map = {
        "CHANGE": "BREAKING CHANGES",
        "BREAK": "BREAKING CHANGES",
        "NEW": "Features",
        "OPT": "Improvements",
        "FIX": "Fixes",
    }

    def parse_issue(self, text: str) -> str:
        """Parse issue ID.

        If valid it's converted to uppercase.
        if strict enabled, it's required.
        """
        kpn_strict = self.config.settings.get(STRICT_CHECK, False)
        if kpn_strict:
            return required_validator(text.upper(), msg="Issue ID is required")
        return text.upper()

    def questions(self) -> list[CzQuestion]:
        questions: list[CzQuestion] = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Commit prefix?",
                "choices": [
                    {"value": FIX, "name": f"{FIX} - {FIX_DESCR}"},
                    {"value": NEW, "name": f"{NEW} - {NEW_DESCR}"},
                    {"value": OPT, "name": f"{OPT} - {OPT_DESCR}"},
                    {"value": BREAK, "name": f"{BREAK} - {BREAK_DESCR}"},
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": "Scope or App name:\n",
            },
            {
                "type": "input",
                "name": "title",
                "message": "Short description:\n",
                "filter": _parse_subject,
            },
            {
                "type": "input",
                "name": "issue",
                "message": "Issue ID:\n",
                "filter": self.parse_issue,
            },
            {"type": "input", "name": "description", "message": "Long description:\n"},
        ]
        return questions

    def message(self, answers: Mapping[str, Any]) -> str:
        prefix = answers["prefix"]
        scope = answers["scope"]
        title = answers["title"]
        issue = answers["issue"]
        description = answers["description"]
        message = ""
        if prefix and not scope:
            message += f"{prefix}:"
        elif prefix and scope:
            message += f"{prefix}({scope}):"
        if title:
            message += f" {title}"
        if issue:
            message += f" (#{issue})"
        if description:
            message += f"\n.\n{description}"
        return message

    def example(self) -> str:
        return (
            "BREAK: Change foobar into quux (#XXX-2053)\n"
            "\n"
            "We changed foobar into quux because the backend changed their implementation.\n"
            "This change will make the code more robust for future changes.\n"
        )

    def schema(self) -> str:
        return "<CHANGE_TYPE>(<SCOPE>): <SUBJECT> (#<ISSUE_ID>)\n\n<LONG_DESCRIPTION>"

    def info(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, "cz_kpn_info.txt")
        with open(filepath, "r") as f:
            return f.read()

    def changelog_message_builder_hook(
        self, message: dict[str, Any], commit: git.GitCommit
    ) -> dict[str, Any]:
        commit_url: str | None = self.config.settings.get(COMMIT_URL)
        if commit_url:
            t = Template(commit_url)
            url = t.safe_substitute(COMMIT_REV=commit.rev)
            short_rev = commit.rev[:7]
            msg = message["message"]
            message["message"] = f"{msg} ([{short_rev}]({url}))"
        return message

    def schema_pattern(self) -> str:
        kpn_strict = self.config.settings.get(STRICT_CHECK, False)
        if kpn_strict:
            return COMMIT_PARSER_STRICT
        return COMMIT_PARSER
