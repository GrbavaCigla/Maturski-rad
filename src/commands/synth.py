from argparse import ArgumentParser, Namespace
import numpy as np
from scipy.io import wavfile


def setup(parser: ArgumentParser):
    pass


def run(args: Namespace):
    ts = np.linspace(0, 3, 3 * 44100)
    starting = 440

    ys = np.zeros(ts.shape)
    amplitudes = [1, 1/2, 1/2, 1/8, 1/3, 1/7, 1/8, 1/7]
    for i in range(len(amplitudes)):
        ys += 1/3 * amplitudes[i] * np.sin(2 * starting * (i + 1) * np.pi * ts)

    ys += 1/4 * np.sin(2 * 50 * np.pi * ts)

    wavfile.write("bla.wav", 44100, ys)
