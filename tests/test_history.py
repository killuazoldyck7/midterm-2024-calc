import os
import pandas as pd
from app.history_manager import HistoryManager


def test_history_manager_add_record():
    test_file = 'data/test_history.csv'

    if os.path.exists(test_file):
        os.remove(test_file)

    manager = HistoryManager(filepath=test_file)
    manager.add_record('add', 3, 4, 7)
    manager.save_history()

    df = pd.read_csv(test_file)
    assert df.shape == (1, 4)
