import pandas as pd
import os

def test_data_files_exist():
    """Check if the data files are in the notebooks folder."""
    # We add 'notebooks/' before each filename
    files = [
        'notebooks/ethiopia.csv', 
        'notebooks/sudan.csv', 
        'notebooks/kenya.csv', 
        'notebooks/nigeria.csv', 
        'notebooks/tanzania.csv'
    ]
    for file in files:
        assert os.path.exists(file), f"Missing data file: {file}"

def test_dataframe_loading():
    """Check if we can read the Ethiopia data from the notebooks folder."""
    df = pd.read_csv('notebooks/ethiopia.csv')
    assert not df.empty, "The dataset is empty!"
    assert 'T2M' in df.columns, "Temperature column (T2M) is missing!"
if __name__ == "__main__":
    print("Running tests...")
    test_data_files_exist()
    test_dataframe_loading()
    print("All tests passed! ✅")