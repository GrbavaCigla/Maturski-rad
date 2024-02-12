CONCERT_PITCH = 440
NOTES_START = -33
NOTES_END = 28

ALL_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
FREQUENCIES = [2 ** (n / len(ALL_NOTES)) * CONCERT_PITCH for n in range(NOTES_START, NOTES_END)]
NOTES = [{"name": i, "octave": j} for j in range(2, 8) for i in ALL_NOTES][:NOTES_END - NOTES_START]

MIN_F0 = 65
MAX_F0 = 2100
MAX_POLY = 6
FRAME_LEN_MS = 93
WINDOW_FUNC = "hann"
