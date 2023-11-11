from argparse import ArgumentParser, FileType, Namespace, ArgumentTypeError
from time import sleep
from os.path import isdir, join
import ntpath

from scipy.io import wavfile
import sounddevice as sd
import noisereduce


def setup(parser: ArgumentParser):
    parser.add_argument("files", nargs="+", type=FileType("rb"))
    parser.add_argument(
        "output",
        type=lambda x: x
        if isdir(x)
        else ArgumentTypeError(f"Path {x} is not a valid directory."),
    )


def run(args: Namespace):
    for file in args.files:
        rate, data = wavfile.read(file)
        data = noisereduce.reduce_noise(y=data, sr=rate)
        wavfile.write(join(args.output, ntpath.basename(file.name)), rate, data)
