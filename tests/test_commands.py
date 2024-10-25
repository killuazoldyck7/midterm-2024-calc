# tests/test_commands.py
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


def test_add_command():
    add_cmd = AddCommand()
    assert add_cmd.execute(3, 5) == 8


def test_subtract_command():
    sub_cmd = SubtractCommand()
    assert sub_cmd.execute(10, 4) == 6


def test_multiply_command():
    mult_cmd = MultiplyCommand()
    assert mult_cmd.execute(3, 5) == 15


def test_divide_command():
    div_cmd = DivideCommand()
    assert div_cmd.execute(10, 2) == 5


def test_divide_by_zero():
    div_cmd = DivideCommand()
    with pytest.raises(ZeroDivisionError):
        div_cmd.execute(10, 0)
