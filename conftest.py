"""Shared helpers for cyoa-game module tests."""

import inspect

import pytest


def code_without_comments(source: str) -> str:
    return "\n".join(
        line
        for line in source.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )


@pytest.fixture
def main_body():
    def _main_body(module):
        return code_without_comments(inspect.getsource(module.main))

    return _main_body
