# tests/test_plugin_loader.py
import os
import pytest
from app.plugin_loader import load_plugins


def test_load_plugins(monkeypatch):
    """Test that plugins load correctly."""
    # Create a valid plugin file in the plugins directory
    valid_plugin_path = 'app/plugins/test_plugin.py'

    with open(valid_plugin_path, 'w') as f:
        f.write("""
class Command:
    name = 'test'

    def execute(self, a, b):
        return a + b
""")

    # Monkeypatch the plugin directory to load our test plugin
    monkeypatch.setattr(os, 'listdir', lambda _: ['test_plugin.py'])

    # Test that the valid plugin is successfully loaded
    plugins = load_plugins()
    assert 'test' in plugins  # Check that 'test' command is loaded

    # Clean up the plugin file after the test
    os.remove(valid_plugin_path)
