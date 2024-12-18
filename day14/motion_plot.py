from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# n_steps = 100
# N = 10
# r = np.random.rand(N, 2, n_steps)

def plotRobots(r, n_steps):
    # plot the initial position
    fig, ax = plt.subplots()
    plt.grid()
    colors = np.random.rand(r.shape[0])
    scat = ax.scatter(r[:, 0, 0], r[:, 1, 0], c=colors, marker='^', s=48)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    plt.tight_layout()

    def update_graph(frame):
        scat.set_offsets(np.c_[r[:, 0, frame], r[:, 1, frame]])
        return scat,

    ani = FuncAnimation(fig, update_graph, frames=1, interval=20, repeat=False)
    plt.show()
    return

def isThereLine(r, height, frame):
    N = int(len(r)/2)
    r = np.array(r)
    r = r.reshape(N, 2)
    x = r[:,0]
    y = r[:,1]

    for i in range(height):
        line = np.sort(x[y == i])
        # print(type(line))
        l = 0
        a_prev = -2
        for a in line:
            if a == a_prev + 1:
                l += 1
                a_prev = a
                continue
            if a == a_prev:
                continue
            if l >= 10:
                print(f"Riga di {l} in frame {frame}")
            l = 0
            a_prev = a
            
    
    # for j in range()
