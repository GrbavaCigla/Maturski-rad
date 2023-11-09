import sounddevice as sd
import scipy.io.wavfile
from time import sleep
from argparse import ArgumentParser, FileType, Namespace

DEFAULTS = {"duration": 3, "frequency": 44100, "output": "output.wav", "sleep": 3}


def setup(parser: ArgumentParser):
    parser.add_argument(
        "-d",
        "--duration",
        dest="duration",
        type=int,
        default=DEFAULTS["duration"],
    )

    parser.add_argument(
        "-s",
        "--sleep",
        dest="sleep",
        type=int,
        default=DEFAULTS["sleep"],
    )

    parser.add_argument(
        "-f",
        "--frequency",
        dest="frequency",
        type=int,
        default=DEFAULTS["frequency"],
    )

    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=FileType("wb"),
        default=DEFAULTS["output"],
    )


def run(args: Namespace):
    sleep(args.sleep)

    print("Recording") # TODO: Replace this with some package-wide function

    recording = sd.rec(
        args.duration * args.frequency,
        samplerate=args.frequency,
        channels=1,
        blocking=True,
        dtype="float64",
    )

    scipy.io.wavfile.write(
        args.output,
        args.frequency,
        recording,
    )
