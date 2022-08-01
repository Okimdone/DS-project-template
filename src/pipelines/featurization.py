"""This script creates new features from the processed data
   Can be run from both cmd line 'config.yaml' or imported as a module
   Pipelines has artifacts on the output and describe logic"""

import argparse
from typing import Text
import yaml

from src.data.load import load_target, load_data
from src.utils.logging import get_logger


def data_load(config_path: Text) -> None:
    """Load and process data

    Args:
        config_path {Text}: path to yaml config file
    """
    # import configs:
    config = yaml.safe_load(open(config_path))
    log_level = config["base"]["log_level"]

    # config_param = config["key1"]["key2"]

    logger = get_logger("FEATURIZATION", log_level)

    # 1. load labels and features df-s:
    # logger.info("Load dataset")

    # 2. featurize:
    # logger.info("Generating features")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
