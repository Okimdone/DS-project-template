from sklearn.model_selection import train_test_split
from pandas import DataFrame
from typing import Tuple


def split_data(
    X: DataFrame,
    y: DataFrame,
    train_size: float = 0.8,
    split_test_n_valid_sets: bool = False,
    valid_size: float = 0.1,
    shuffle: bool = True,
    random_state: int = 42,
    **args: dict
) -> Tuple:
    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        train_size=train_size,
        shuffle=shuffle,
        random_state=random_state,
        **args,
    )
    if split_test_n_valid_sets:
        X_valid, X_test, y_valid, y_test = train_test_split(
            X_valid,
            y_valid,
            train_size=valid_size / (1.0 - train_size),
            shuffle=shuffle,
            random_state=random_state,
            **args,
        )
        return X_train, X_valid, y_train, y_valid, X_test, y_test
    return X_train, X_valid, y_train, y_valid
