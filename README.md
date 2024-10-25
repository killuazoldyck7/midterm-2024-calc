# Advanced Python Calculator

## Overview
This project implements an advanced Python-based calculator with a command-line interface (REPL), a plugin system, history management using CSV files (via Pandas), comprehensive logging, and environment variable configuration.

## Features
- **Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Command System**: Easily extendable using the Command Pattern for different operations.
- **Plugin System**: Dynamically loads commands as plugins without modifying core code.
- **History Management**: Tracks all user calculations and saves them to a CSV file for future retrieval.
- **Logging**: Logs all operations, errors, and system messages with different logging levels.
- **Environment Variables**: Configures application settings dynamically through `.env` files.


## Project Structure
```plaintext
midterm-2024-calc/
├── app/
│   ├── __init__.py            # Main app file handling REPL and core logic
│   ├── plugin_loader.py       # Dynamically loads plugins
│   ├── history_manager.py     # Manages calculation history with Pandas
│   ├── commands/              # Contains arithmetic command implementations
│   └── plugins/               # Placeholder for additional command plugins
├── data/
│   └── history.csv            # Stores calculation history
├── tests/                     # Pytest test cases for app and commands
├── .github/workflows/         # GitHub Actions for CI/CD
├── logging.conf               # Logging configuration
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── main.py                    # Entry point to run the app
└── pytest.ini                 # Pytest configuration
```

## Setup Instructions

#### 1. Clone the Repository
git clone https://github.com/killuazoldyck7/midterm-2024-calc.git
cd midterm-2024-calc

#### 2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#### 3. Install Dependencies
pip install -r requirements.txt

#### 4. Run the Application
python main.py

#### 5. Run Tests
pytest

#### 6. Check Test Coverage
pytest --cov=app --cov-report=term-missing

## Usage Examples
1. **Basic Operations**:
 ◦ Addition: add 3 5
 ◦ Subtraction: subtract 10 4
 ◦ Multiplication: multiply 2 7
 ◦ Division: divide 9 3
2. **View Calculation History**:
 ◦ history — Displays all previously executed commands and their results.
3. **Exit the Application**:
 ◦ exit

## Architectural Decisions
#### 1. Command Pattern
The Command Pattern encapsulates different arithmetic operations (Add, Subtract, Multiply, Divide) as individual command objects. This design allows easy extensibility for new operations without modifying the core REPL logic.
Each command (e.g., AddCommand, SubtractCommand) implements the execute method, which defines the arithmetic operation. The plugin_loader.py dynamically loads commands, reinforcing the flexibility of this pattern.
 ◦ **Impact**: Enhances maintainability and scalability. New operations can be added as plugins without changing the core system, simplifying future updates.

#### 2. Plugin System
The project’s dynamic plugin system loads commands via Python’s importlib. Adding new command modules to the plugins/ directory automatically registers them at startup.
 ◦ **Impact**: Decouples the core application from new functionalities, allowing modifications and extensions without changes to the core codebase.

#### 3. History Management with Pandas
The HistoryManager class uses Pandas to store calculation history in a CSV file (data/history.csv). Each calculation result is appended to the history, viewable with the history command.
 ◦ **Impact**: Storing history in a CSV file ensures persistence across sessions, supporting further analysis and management.


## Logging Strategy
Logging is implemented across the application using Python's logging module, configured through logging.conf. Logs are separated into a rotating file handler (app.log) and the console.

#### Logging Levels:
◦ **INFO**: Logs general operations like command execution and results.
◦ **WARNING**: Logs invalid inputs or unrecognized commands.
◦ **ERROR**: Logs critical issues like invalid inputs and division by zero.

#### Example Logging Configuration:
The log file rotates when it reaches 1 MB and retains up to 5 files, found in the logs/ directory.
[loggers]
keys=root

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=fileHandler,consoleHandler

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=INFO
formatter=simpleFormatter
args=('logs/app.log', 'a', 1048576, 5)

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stderr,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

◦ **Impact**: This logging strategy enables traceability, aiding in debugging and monitoring. Environment variables allow logging levels to be configured dynamically, adapting to different environments (development, production).


## Design Patterns
1. **Command Pattern**: Facilitates organized and extendable architecture for executing commands.

2. **Facade Pattern**: Simplifies interactions with Pandas for history loading, saving, and management through the HistoryManager.

3. **Singleton Pattern**: Centralizes and reuses logging configuration, ensuring a single control point for log output.


## CI/CD with GitHub Actions
This project includes a GitHub Actions workflow for Continuous Integration (CI). Each push or pull request triggers a build to:

◦ Install dependencies.

◦ Run tests to ensure code integrity.

◦ Check code quality with Pylint.

◦ **Impact**: Automated CI provides quick feedback on code quality and functionality, making the development process efficient and reliable.

## Video Demonstration

[Watch the Video Demonstration](https://drive.google.com/file/d/1vWo7-i9XW6YPIIrZbG2QPPtgce2ef5xC/view?usp=drive_link)

## Conclusion
This project demonstrates professional software development practices focusing on clean architecture, extensibility, and maintainability. The Command Pattern, Plugin System, and comprehensive logging enhance scalability and ease of management across development and production environments.