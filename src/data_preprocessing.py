import pandas as pd
def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    # Perform any necessary data preprocessing here
    return df
