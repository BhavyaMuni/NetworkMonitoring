# import pyspeedtest
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time
import psutil
from collections import deque

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
speed = deque(maxlen=21)


def animate(i):
    st1 = psutil.net_io_counters()[1]
    t1 = time.time()
    time.sleep(1)
    st2 = psutil.net_io_counters()[1]
    t2 = time.time()
    bytesrecv = (st2 - st1)/(t2 - t1)
    mbrecv = bytesrecv/1024/1024
    speed.append(mbrecv)
    ax1.clear()
    ax1.plot(speed)
    fig.suptitle('Internet usage', fontsize=20)
    plt.ylabel('MB/s', fontsize=12)
    plt.grid(True)
    ax1.set_xticklabels([])


ani = anim.FuncAnimation(fig, animate, interval=1000)
plt.show()
