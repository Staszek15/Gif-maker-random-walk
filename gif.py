import numpy as np
import os
import matplotlib.pyplot as plt
import random
import imageio

frames = 100
filenames = []
moves = [(5,0), (-5,0), (0,5), (0,-5)]
position = (50, 50)

for i in range(frames):
    move = random.choice(moves)
    position = (position[0] + move[0], position[1] + move[1])
    plt.scatter(position[0], position[1], c = "red", s = 20)

    #plt.ylim(0,50)
    #plt.xlim(0,50)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title("Agent")
    plt.grid(True, linewidth=0.4)
    plt.xticks(np.arange(0, 101, 5))
    plt.yticks(np.arange(0, 101, 5))

    filename = f"frame {i+1}.png"
    filenames.append(filename)

    plt.savefig(filename)
    #plt.close()


with imageio.get_writer("agent.gif", mode="I") as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in filenames:
    os.remove(filename)