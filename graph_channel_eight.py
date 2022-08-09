import numpy
import time
from collections import deque
import matplot.pyplot as plt
from matplotlib import style

style.use('ggplot')

OPS = 105  # Oscillations per second
HM_SECONDS_SLICE = 1  # this is the horizontal length of graph
                      # we can adjust this range from 1 to 200
                      # the more close each peak is, the most concentrated and awake an individual is,
                      # the more spread out each peak is, the more relaxed, sleepy an individual is.

data = numpy.load('seq-30000.npy')
print(len(data))

# frequency for loop, getting data only from channel 8 of the headset
for i in range(OPS*HM_SECONDS_SLICE, len(data)):
    new_data = data[i-FPS*HM_SECONDS_SLICE: i]
    c8 = new_data[:, 8]

    GRAPH = c8
    print(c8)
    time.sleep(1/OPS)

    plt.plot(c8)
    plt.show()
    break