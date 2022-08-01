import pandas as pd
from typing import Text, Dict


def load_target(path: Text, **args: Dict) -> pd.DataFrame:
    """ Loads data from csv to df
    """
    return pd.read_csv(path, **args)


def load_features(path: Text, **args: Dict) -> pd.DataFrame:
    """ Loads data from csv to df
    """
    return pd.read_csv(path, **args)


def load_data(path: Text, **args: Dict) -> pd.DataFrame:
    """ Loads data from csv to df
    """
    data_df = pd.read_csv(path, **args)
    target_df = data_df['Species']
    features_df = data_df[ data_df.columns.difference(['Species']) ]
    return features_df, target_df

