from pathlib import Path
from typing import Any
import json
import numpy as np
from scipy.signal import get_window

from ..constants import FRAME_LEN_MS, WINDOW_FUNC


def read_config(config_path: Path) -> dict[str, Any]:
    """
    Read the estimator configuration from specified json file.
    """
    assert config_path.exists(), "Config file specified doesn't exist."

    text = config_path.read_text()

    return json.loads(text)


def calculate_stft(
    x: np.ndarray,
    sample_rate: int,
    frame_len_ms: int = FRAME_LEN_MS,
    window_func: str = WINDOW_FUNC,
) -> np.ndarray:
    """
    Calculate short time fourier transform.
    """

    frame_len_samps = int(sample_rate * frame_len_ms / 1000)
    window = get_window(window_func, frame_len_samps)

    pad_len = int(2 ** np.ceil(np.log2(2 * frame_len_samps)))
    data = np.array(
        [
            np.fft.fft(window * x[i : i + frame_len_samps], pad_len)
            for i in range(0, len(x) - frame_len_samps, frame_len_samps)
        ]
    )

    return data
