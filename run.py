import sys
import json
import argparse
import datetime

import yaml
from munch import DefaultMunch

from engine import Engine
from molva.common.stroka_logging import setup_logging


def run(cfg):
    engine = Engine(cfg)
    engine.run()

def get_config():
    parser = argparse.ArgumentParser(description='Trading Engine named Strela')
    parser.add_argument('-config', help='a path to configuration file')

    args = parser.parse_args()
    filename = args.config

    with open(filename, 'r') as ymlfile:
        cfg_dict = yaml.load(ymlfile)
        return DefaultMunch.fromDict(cfg_dict, None)

def start_engine():
    cfg = get_config()
    if cfg is None:
        raise Exception("Unable to attach the config")

    logger_name = "{}_{}.log".format(cfg.logger.path,datetime.datetime.now().isoformat())
    logger = setup_logging(cfg, 'strela'+logger_name)
    logger.info("Stroka client is started!")
    logger.info("Configuration: %s", json.dumps(cfg))
    run(cfg)


if __name__ == "__main__":
    start_engine()
