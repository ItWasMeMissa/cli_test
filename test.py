import sys
import cli

def test_add(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['cli.py', 'add', '1', '2', '3'])

    cli.main()

    assert capsys.readouterr().out == '6\n'


def test_multiply(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['cli.py', 'multiply', '2', '3', '4'])

    cli.main()

    assert capsys.readouterr().out == '24\n'


def test_hello(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['cli.py', 'hello'])

    cli.main()

    assert capsys.readouterr().out == 'Bob\n'


def test_unknown_command(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['cli.py', 'kek'])

    cli.main()

    assert capsys.readouterr().out == 'Unknown command\n'