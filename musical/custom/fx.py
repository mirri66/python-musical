from musical.audio.source import generate_wave_input, ringbuffer
import numpy as np
import math


def tone(freq, time):
    rate = 44100

    Ts = 1.0/freq; # sampling interval
    t = np.arange(0,int(time*rate/freq),Ts) # time vector
    y = np.sin(2*np.pi*t)
    return y

