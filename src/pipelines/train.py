"""This script trains a model on the final version of the data
   Can be run from both cmd line 'config.yaml' or imported as a module
   Pipelines has artifacts on the output and describe logic"""

import argparse
from typing import Text
import yaml

from src.data.load import load_features, load_target
from src.utils.logging import get_logger
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle


def data_load(config_path: Text) -> None:
    """Load and process data

    Args:
        config_path {Text}: path to yaml config file

    """
    # import configs:
    config = yaml.safe_load(open(config_path))
    log_level = config["base"]["log_level"]
    load_params, split_params, train_params = (
        config["data_load"],
        config["data_split"],
        config["train"],
    )
    dataset_path = load_params["processed_dataset"]
    target_path = load_params["processed_target"]
    col_index = load_params["col_index"]
    model_path = train_params["model_path"]

    logger = get_logger("TRAIN", log_level)

    # 1. load labels and features df-s:
    logger.info("Load dataset & target")
    features_df = load_features(dataset_path, index_col=col_index)
    target_df = load_target(target_path, index_col=col_index)

    # 2. Load the train, valid[, test] indexes
    logger.info("Load indexes for train, valid[, test]")
    train_index_path = split_params["paths"]["train_index_path"]
    valid_index_path = split_params["paths"]["valid_index_path"]
    # test_index_path = split_params['paths']['test_index_path']
    train_index = pd.Index(pd.read_csv(train_index_path).squeeze())
    valid_index = pd.Index(pd.read_csv(valid_index_path).squeeze())
    # test_index = pd.Index(pd.read_csv(test_index_path).squeeze())

    # 3. Split the data into train, valid[, test] using indexes
    logger.info("Separate train, valid[, test]")
    X_train, y_train = features_df.loc[train_index], target_df.loc[train_index]
    X_valid, y_valid = features_df.loc[valid_index], target_df.loc[valid_index]
    # X_test, y_test = features_df.loc[test_index], target_df.loc[test_index]

    # 4. Train the model
    logger.info("Training the model")
    clf = RandomForestClassifier(
        n_estimators=6, min_samples_split=30, n_jobs=2, random_state=42
    )
    clf.fit(X_train, y_train.squeeze())

    # 5. Save the model
    logger.info("Saving the model")
    with open(file=model_path, mode="wb") as f:
        pickle.dump(clf, f)

    # 6. Show Accuracy
    logger.debug(f"Model accuracy [Train]: {clf.score(X_train, y_train)}")
    logger.debug(f"Model accuracy [Valid]: {clf.score(X_valid, y_valid)}")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
