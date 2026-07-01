"""Tests for Module 4 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_has_show_previous_ending():
    assert callable(game.show_previous_ending)


def test_scenes_is_list():
    assert isinstance(game.SCENES, list)
    assert len(game.SCENES) >= 2


def test_uses_while_loop_in_main(main_body):
    assert "while " in main_body(game)


def test_writes_ending_file(tmp_path, monkeypatch, capsys):
    log_file = tmp_path / "ending.txt"
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Jordan\n1\n"))
    game.main()
    assert log_file.exists(), "Write the ending reached to a file"
    content = log_file.read_text()
    assert "Jordan" in content
    assert "TODO" not in content


def test_reads_ending_file_on_next_run(tmp_path, monkeypatch, capsys):
    log_file = tmp_path / "ending.txt"
    marker = "PRIOR_RUN: Alex reached ending: Saved It"
    log_file.write_text(marker)
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Alex\n1\n"))
    game.main()
    out = capsys.readouterr().out
    assert marker in out, "On the next run, read the file and show the previous ending"
