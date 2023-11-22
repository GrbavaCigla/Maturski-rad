from typing import Tuple
import numpy as np

from .constants import CONCERT_PITCH, ALL_NOTES


def find_closest_pitch(pitch: float) -> Tuple[str, float]:
    i = int(np.round(np.log2(pitch / CONCERT_PITCH) * 12))

    closest_note = ALL_NOTES[i % 12] + str(4 + (i + 9) // 12)
    closest_pitch = CONCERT_PITCH * 2 ** (i / 12)

    return closest_note, closest_pitch
