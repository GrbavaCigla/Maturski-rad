import numpy as np
from argparse import ArgumentParser, FileType, Namespace
from ..estimator import Estimator

DEFAULTS = {}


def setup(parser: ArgumentParser):
    parser.add_argument("file", type=FileType("rb"))


def run(args: Namespace):
    estimator = Estimator()
    estimations = estimator.estimate(args.file)
