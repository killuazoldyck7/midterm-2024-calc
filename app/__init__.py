"""
This module contains the main application class and REPL logic.
"""
import os
import logging
from dotenv import load_dotenv
from app.plugin_loader import load_plugins
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.history_manager import HistoryManager  # Import the history manager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

class App:
    """
    The App class handles the main REPL loop and command execution logic.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self):
        """
        Initialize the app, load environment variables, and commands (including plugins).
        """
        load_dotenv()  # Load environment variables
        environment = os.getenv('ENVIRONMENT', 'production')
        logging.info("Running in %s mode", environment)

        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand()
        }

        # Load additional plugins dynamically
        self.commands.update(load_plugins())
        self.history_manager = HistoryManager()  # Initialize the history manager

    def start(self) -> None:
        """
        Starts the REPL loop, processes user input, and executes commands.
        """
        logging.info("Application started.")
        print("Welcome to the Calculator. Type 'menu' to see commands, 'history' to view calculation history, or 'exit' to exit.")

        while True:
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                logging.info("Exiting application.")
                print("Exiting...")
                break
            if user_input == "menu":
                print(f"Available commands: {', '.join(self.commands.keys())}")
            elif user_input == "history":
                print(self.history_manager.show_history())
            else:
                parts = user_input.split()
                if len(parts) == 0:
                    logging.warning("Error: No command entered.")
                    print("Error: Please enter a command.")
                    continue

                command_name = parts[0]
                if command_name not in self.commands:
                    logging.warning("Unknown command entered.")
                    print(
                        "Unknown command. Type 'menu' to list available commands.")
                    continue

                if len(parts) != 3:
                    logging.warning("Invalid input format.")
                    print(
                        "Invalid input. Please provide a command followed by two numbers.")
                    continue

                try:
                    a, b = map(float, parts[1:])
                    result = self.commands[command_name].execute(a, b)
                    logging.info(
                        "Executed %s command with values: %s, %s. Result: %s",
                        command_name, a, b, result
                    )
                    print("Result:", result)

                    # Save the result to history
                    self.history_manager.add_record(command_name, a, b, result)
                    self.history_manager.save_history()

                except ValueError:
                    logging.error("Value error: Invalid number input.")
                    print("Error: Please provide valid numbers.")
                except ZeroDivisionError:
                    logging.error("Attempted division by zero.")
                    print("Error: Division by zero is not allowed.")
