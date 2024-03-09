import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from argparse import ArgumentParser, FileType, Namespace

DEFAULTS = {"spectrogram": False}


def setup(parser: ArgumentParser):
    parser.add_argument("file", type=FileType("rb"))

    parser.add_argument(
        "-s",
        "--spectrogram",
        dest="spectrogram",
        action="store_true",
        default=DEFAULTS["spectrogram"],
    )


def run(args: Namespace):
    frequency, recording = scipy.io.wavfile.read(args.file)
    duration = len(recording) / frequency

    if args.spectrogram:
        x = np.arange(0, frequency / 2, 1 / duration)
        y = abs(fft(recording))[:len(x)]
    else:
        x = np.arange(0, duration, 1 / frequency)
        y = recording

    plt.plot(x, y)
    plt.show()
