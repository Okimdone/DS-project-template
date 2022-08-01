"""This script splits the data into either (train and test)
   or  (train, valid and test) sets
   Can be run from both cmd line (argparse to read config.yaml)
   or imported as a module
   """

import argparse
from typing import Text
import yaml

from src.data.load import load_features, load_target
from src.data.split import split_data
from src.utils.logging import get_logger


def data_load(config_path: Text) -> None:
    """Split the data into train and valid [and test]

    Args:
       config_path {Text}: path to yaml config file

    """
    # import configs:
    config = yaml.safe_load(open(config_path))

    log_level = config["base"]["log_level"]
    # Paths to data
    load_params = config["data_load"]
    processed_dataset = load_params["processed_dataset"]
    processed_target = load_params["processed_target"]
    col_index = load_params["col_index"]
    # Arguments for split_data
    split_config = config["data_split"]
    split_args = {
        "train_size": split_config["train_size"],
        "split_test_n_valid_sets": split_config["split_test_n_valid_sets"],
        "valid_size": split_config["valid_size"],
        "shuffle": split_config["shuffle"],
        "random_state": split_config["random_state"],
    }
    # Paths to output : (train, valid[, test]) indexes
    train_index_path = split_config["paths"]["train_index_path"]
    valid_index_path = split_config["paths"]["valid_index_path"]
    test_index_path = split_config["paths"]["test_index_path"]

    logger = get_logger("DATA_SPLIT", log_level)

    # 1. load labels and features df-s:
    logger.info("Load dataset")
    features_df = load_features(processed_dataset, index_col=col_index)
    target_df = load_target(processed_target, index_col=col_index)

    # 2. Split The data
    logger.info("Split dataset")
    X_train, X_valid, y_train, y_valid, *df_rem = split_data(
        features_df, target_df, **split_args
    )

    # 3. Store the index of the splits
    logger.info("Storing  the changes!")
    logger.debug(f"Train dataset index path: {train_index_path}")
    X_train.to_csv(train_index_path, columns=[], index=True)
    logger.debug(f"Validation dataset index path: {valid_index_path}")
    X_valid.to_csv(valid_index_path, columns=[], index=True)
    if split_args["split_test_n_valid_sets"]:
        logger.debug(f"Test dataset index path: {test_index_path}")
        X_test, y_test = df_rem
        X_test.to_csv(test_index_path, columns=[], index=True)


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
