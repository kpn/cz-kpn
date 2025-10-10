import os
from string import Template
from typing import Any

from commitizen import git
from commitizen.cz.base import BaseCommitizen
from commitizen.defaults import Questions

from cz_kpn.consts import (
    BREAK,
    BREAK_DESCR,
    BUMP_PATTERN,
    COMMIT_PARSER,
    FIX,
    FIX_DESCR,
    NEW,
    NEW_DESCR,
    OPT,
    OPT_DESCR,
)


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

    def questions(self) -> Questions:
        questions: list[dict[str, str | list[dict[str, str]]]] = [
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
            {"type": "input", "name": "title", "message": "Short description:\n"},
            {"type": "input", "name": "issue", "message": "Issue ID:\n"},
            {"type": "input", "name": "description", "message": "Long description:\n"},
        ]
        return questions

    def message(self, answers: dict) -> str:
        prefix = answers["prefix"]
        title = answers["title"]
        issue = answers["issue"]
        description = answers["description"]
        message = ""
        if prefix:
            message += f"{prefix}:"
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

    def changelog_message_builder_hook(  # type: ignore
        self, message: dict[str, Any], commit: git.GitCommit
    ) -> dict[str, Any]:
        commit_url: str = self.config.settings.get("commit_url")  # type: ignore
        if commit_url:
            t = Template(commit_url)
            url = t.safe_substitute(COMMIT_REV=commit.rev)
            short_rev = commit.rev[:7]
            msg = message["message"]
            message["message"] = f"{msg} ([{short_rev}]({url}))"
        return message

    def schema_pattern(self) -> str:
        return COMMIT_PARSER
