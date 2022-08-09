from pyOpenBCI import OpenBCICyton
from collections import deque
import time
import numpy
import cv2

def print_raw(sample):
    print(sample.channels_data)

board = OpenBCICyton(daisy=True) # can automatically find connection to EEG helmet

board.start_stream(print_raw)