# tests/test_app.py
import pytest
from app import App
from app.commands.divide import DivideCommand


def test_app_start_exit_command(monkeypatch, capsys):
    """Test the exit command in the REPL."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Exiting..." in captured.out


def test_app_menu_command(monkeypatch, capsys):
    """Test the menu command in the REPL."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Available commands" in captured.out


def test_app_history_command(monkeypatch, capsys):
    """Test the history command in the REPL."""
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    # Instead of checking the exact output, check for key components of the
    # DataFrame
    assert "Command" in captured.out
    assert "Operand1" in captured.out
    assert "Operand2" in captured.out
    assert "Result" in captured.out


def test_invalid_command(monkeypatch, capsys):
    """Test unknown command in the REPL."""
    inputs = iter(['invalid_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out


def test_invalid_number_input(monkeypatch, capsys):
    """Test invalid number input in the REPL."""
    inputs = iter(['add a b', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Error: Please provide valid numbers." in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    """Test division by zero in the REPL."""
    inputs = iter(['divide 4 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out


def test_valid_command(monkeypatch, capsys):
    """Test valid command in the REPL."""
    inputs = iter(['add 3 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    captured = capsys.readouterr()
    assert "Result: 8.0" in captured.out
