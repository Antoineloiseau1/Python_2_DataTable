import pandas as pd


def load(path: str) -> pd.DataFrame:
    """def load(path: str) -> pd.DataFrame:

Opens a .csv file given by path, display its \
dimensions and returns it as a pandas.DataFrame file
"""
    try:
        if type(path) is not str:
            raise TypeError("TypeError: file must be type .csv")
        if (not path.endswith(".csv")):
            raise Exception("ExtensionError: file must be type .csv")
        file = pd.read_csv(path)
    except Exception as msg:
        print(msg)
        return None
    print("Loading dataset of dimensions:", file.shape)
    return file
