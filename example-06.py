import numpy

from musical.theory import Note, Scale
from musical.audio import source, playback
from musical.custom import fx


# Define key and scale
chunks = []
#chunks.append(source.sine(key, 1.5) + source.square(fifth, 1.5))
chunks.append(fx.tone(150, 1))
#chunks.append(fx.tone(200, 1))

print("Rendering audio...")

data = numpy.concatenate(chunks)
print(data)
print(len(data))

print("Playing audio...")

playback.play(data)

print("Done!")
