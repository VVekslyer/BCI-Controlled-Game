from pyOpenBCI import OpenBCICyton
from collections import deque
import time
import numpy
import cv2

last_print = time.time()
freq_counter = deque(maxlen=50)
sequence = numpy.zeros((100, 16))
counter = 0

def print_raw(sample):
    sequence = numpy.roll(sequence, 1, 0)
    sequence[0, ...] = sample.channels_data

    freq_counter.append(time.time() - last_print)
    last_print = time.time()

    # formatted print of results
    print(f'Freq: {1/(sum(freq_counter)/len(freq_counter)):.2f} Hz, : {len(sequence)}, ... {counter}')


board = OpenBCICyton(daisy=True) # can automatically find connection to EEG helmet

board.start_stream(print_raw)


# it looks like the OpenBCI team uses fourier transforms to convert
# to generate the waves in the GUI.