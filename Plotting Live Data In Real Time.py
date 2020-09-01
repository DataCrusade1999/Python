import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.style.use('fast')

var5 = []
var6 = []


def function(p):
    var5.append(np.random.randint(10))
    var6.append(np.random.randint(10))
    plt.cla()
    plt.plot(var5, var6)


placeholder = FuncAnimation(plt.gcf(), function, interval=1000)
plt.tight_layout()
plt.show()
