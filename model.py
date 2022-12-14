from pylsl import StreamInlet, resolve_stream
from pyOpenBCI import OpenBCICyton
from matplotlib import style
from collections import deque
import tensorflow as tf
import numpy as np
import cv2
import os
import random
import time

MODEL_NAME = 'models/32x3-5epoch-1572915518-acc-0.8500000238418579-loss-0.36.model'

model = tf.keras.models.load_model(MODEL_NAME)
reshape = (-1, 16, 60)
model.predict(np.zeros((32,16,60)).reshape(reshape))

ACTION = 'up'   # ACTION is what I'll be thinking about doing in the game
# here I'm thinking about moving up
FFT_MAX_HZ = 60   # max. frequency
HM_SECONDS = 10   # approximate value
TOTAL_ITERS = HM_SECONDS * 25
BOX_MOVE = 'model'

last_print = time.time()
hz_counter = deque(maxlen=150)

# first resolve an EEG stream
print('looking for an EEG stream...')
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

WIDTH = 800
HEIGHT = 800
SQ_SIZE = 50
MOVE_SPEED = 1

square = {'x1': int(int(WIDTH)/2-int(SQ_SIZE/2)),
          'x2': int(int(WIDTH)/2+int(SQ_SIZE/2)),
          'y1': int(int(HEIGHT)/2-int(SQ_SIZE/2)),
          'y2': int(int(HEIGHT))/2+int(SQ_SIZE/2)
         }

box = np.ones((square['y2']-square['y1'], square['x2']-square['x1'], 3)) * np.random.uniform(size=(3,))
horizontal_line = np.ones((HEIGHT, 10, 3) * np.random.uniform(size=(3,)))
vertical_line = np.ones((10, WIDTH, 3)) * np.random.uniform(size=(3,))

total = 0
up = 0
down = 0
none = 0
correct = 0
channel_datas = []

for i in range(TOTAL_ITERS):
    channel_data = []
    for i in range(16):
        sample, timestamp = inlet.pull_sample()
        channel_data.append(sample[:FFT_MAX_HZ])
    
    hz_counter.append(time.time(), last_print)
    last_print = time.time()
    cur_raw_hz = 1/(sum(hz_counter)/len(hz_counter))
    print(cur_raw_hz)

    env = np.zeros((WIDTH, HEIGHT, 3))
    env[:,HEIGHT//2-5:HEIGHT//2+5,:] = horizontal_line
    env[WIDTH//2-5:WIDTH//2+5,:,:] = vertical_line
    env[square['y1']:square['y2'], square['x1']:square['x2']] = box



    cv2.imshow('', env)
    cv2.waitKey(1)

    network_input = np.array(channel_data).reshape(reshape)
    out = model.predict(network_input)
    print(out[0])

    

    # Model figures out if it got it right or wrong.
    if BOX_MOVE == 'random':
        move = random.choice[-1,0,1]
        square['x1'] += move
        square['x2'] += move

    elif BOX_MOVE == 'model':
        choice = np.argmax(out)
        if choice == 0:
            if ACTION == 'up':
                correct += 1
            square['y1'] = MOVE_SPEED
            square['y2'] = MOVE_SPEED
            up += 1
        
        elif choice == 2:
            if ACTION == 'down':
                correct += 1
            square['y1'] += MOVE_SPEED
            square['y2'] += MOVE_SPEED
            up += 1
        
        else:
            if ACTION == 'none':
                correct += 1
                none += 1
    
    total += 1
    channel_datas.append(channel_data)

#plt.plot(channel_datas[0][0])
#plt.show()


# Save collected DL data to disk 
# so we can continue training the model
datadir = 'data'
if not os.path.exists(datadir):
    os.mkdir(datadir)

actiondir = f'{datadir}/{ACTION}'
if not os.path.exists(actiondir):
    os.mkdir(actiondir)

print(len(channel_datas))
print(f'saving {ACTION} data...')
np.save(os.path.join(actiondir, f'{int(time.time())}.npy'), np.array(channel_datas))
print('done.')

for action in ['up', 'down', 'none']:
    print(action, sum(os.path.getsize(f'data/{action}/{f}') for f in os.listdir(f'data/{action}'))/1_000_000, 'MB')

print(ACTION, correct/total)

with open('accuracies.csv', 'a') as f:
    f.write(f'{int(time.time())},{ACTION},{correct/total},{MODEL_NAME},{up/total},{down/total},{none/total}\n')