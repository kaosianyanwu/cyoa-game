"""Tests for Module 2 acceptance criteria."""

import importlib.util
import re
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_scene_text_stored_in_variable():
    source = (MODULE_DIR / "game.py").read_text()
    assert re.search(r"\w+\s*=\s*(['\"]|f['\"])", source), (
        "Store scene text in a variable before printing it"
    )


def test_prints_scene_and_ending(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Alex\n"))
    game.main()
    out = capsys.readouterr().out
    assert "TODO" not in out, "Replace placeholder scene and ending text"
    assert "Alex" in out
    lines = [line for line in out.splitlines() if line.strip()]
    assert len(lines) >= 4, "Print title, greeting, scene, and ending"


def test_no_branching_yet():
    import inspect

    main_source = inspect.getsource(game.main)
    code_only = "\n".join(
        line for line in main_source.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ).lower()
    assert "if " not in code_only and "elif " not in code_only, (
        "Module 2 has no branching in main() — save if/elif for Module 3"
    )
