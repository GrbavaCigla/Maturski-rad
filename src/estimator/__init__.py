from typing import Any
from pathlib import Path

from scipy.io import wavfile
from scipy.signal import stft

from .utils import calculate_stft, read_config
from ..constants import FRAME_LEN_MS, MAX_F0, MAX_POLY, MIN_F0, WINDOW_FUNC


class Estimator:
    def __init__(
        self,
        config=None,
        min_f0=MIN_F0,
        max_f0=MAX_F0,
        max_poly=MAX_POLY,
        frame_len_ms=FRAME_LEN_MS,
        window_func=WINDOW_FUNC,
    ):
        if config != None:
            conf = read_config(config)
            self.min_f0 = conf.get("min_f0")
            self.max_f0 = conf.get("max_f0")
            self.max_poly = conf.get("max_poly")
            self.frame_len_ms = conf.get("frame_len_ms")
            self.window_func = conf.get("window_func")

        self.min_f0 = min_f0
        self.max_f0 = max_f0
        self.max_poly = max_poly
        self.frame_len_ms = frame_len_ms
        self.window_func = window_func

    def estimate(self, file_path: Path) -> tuple[Any, Any]:
        assert file_path.exists(), "Audio file specified doesn't exist."

        sample_rate, x = wavfile.read(file_path)

        if x.ndim > 1:
            _, channels_len = x.shape
            x = x.sum(axis=1) / channels_len
        
        data = calculate_stft(x, sample_rate, self.frame_len_ms, self.window_func)

        return ([],[])
