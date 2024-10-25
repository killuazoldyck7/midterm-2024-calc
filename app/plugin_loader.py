"""
This module provides functionality for dynamically loading command plugins.
"""
import os
import importlib


def load_plugins():
    """
    Load additional command plugins from the 'plugins' directory.

    Returns:
        dict: A dictionary of loaded plugins with their names as keys.
    """
    plugins = {}
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')

    for filename in os.listdir(plugins_dir):
        if filename == '__init__.py':  
            continue
        if filename.endswith('.py'):
            module_name = f'app.plugins.{filename[:-3]}'
            try:
                module = importlib.import_module(module_name)
                command_class = getattr(module, 'Command')
                command_instance = command_class()
                plugins[command_instance.name] = command_instance
            except ImportError as e:
                print(f"Failed to import plugin {filename}: {e}")
            except AttributeError as e:
                print(f"Failed to load plugin {filename}: {e}")

    return plugins
