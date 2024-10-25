import pandas as pd
import os


class HistoryManager:
    def __init__(self, filepath='data/history.csv'):
        self.filepath = filepath
        self._load_history()

    def _load_history(self):
        if os.path.exists(self.filepath):
            self.history = pd.read_csv(self.filepath)
        else:
            self.history = pd.DataFrame(
                columns=[
                    'Command',
                    'Operand1',
                    'Operand2',
                    'Result'])

    def add_record(self, command, operand1, operand2, result):
        new_record = pd.DataFrame([{
            'Command': command,
            'Operand1': operand1,
            'Operand2': operand2,
            'Result': result
        }])
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def save_history(self):
        self.history.to_csv(self.filepath, index=False)

    def show_history(self):
        return self.history
