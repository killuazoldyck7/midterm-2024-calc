import os
import pytest
from app.plugin_loader import load_plugins


def test_load_plugins(monkeypatch):
    """Test that plugins load correctly."""
    valid_plugin_path = 'app/plugins/test_plugin.py'

    with open(valid_plugin_path, 'w') as f:
        f.write("""
class Command:
    name = 'test'

    def execute(self, a, b):
        return a + b
""")

    monkeypatch.setattr(os, 'listdir', lambda _: ['test_plugin.py'])

    plugins = load_plugins()
    assert 'test' in plugins

    os.remove(valid_plugin_path)
