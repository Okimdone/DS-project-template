"""This script loads and pre-process raw data
   Can be run from both cmd line 'config.yaml' or imported as a module
   Pipelines has artifacts on the output and describe logic"""

import argparse
from typing import Text
import yaml

from src.data.load import load_target, load_data
from src.data.process import process_target, process_data
from src.utils.logging import get_logger


def data_load(config_path: Text) -> None:
    """Load and process data

    Args:
        config_path {Text}: path to yaml config file

    """
    # import configs:
    config = yaml.safe_load(open(config_path))

    log_level = config["base"]["log_level"]
    load_params = config["data_load"]
    # target_raw_path = config['data_load']['unprocessed_target']
    dataset_raw_path = load_params["unprocessed_dataset"]
    dataset_processed_path = load_params["processed_dataset"]
    target_processed_path = load_params["processed_target"]
    col_index = load_params["col_index"]

    logger = get_logger("DATA_LOAD", log_level)

    # 1. load labels and features df-s:
    logger.info("Load dataset")
    data_df, target_df = load_data(dataset_raw_path, index_col=col_index)

    # 2. process labels:
    logger.info("Process target")
    target_df = process_target(target_df)

    # 3. process features:
    logger.info("Process dataset")
    data_df = process_data(data_df)
    data_df.dropna(inplace=True)

    # 4. save labels and features:
    logger.info("Save processed data and target")
    target_df.to_csv(target_processed_path)
    data_df.to_csv(dataset_processed_path)
    logger.debug(f"Processed data path: {dataset_processed_path}")
    logger.debug(f"Processed data path: {target_processed_path}")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
