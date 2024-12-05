import numpy as np
import matplotlib.pyplot as plt
import math

def easeOutCirc(x):
    return math.sqrt(1 - math.pow(x - 1, 2));


x = np.arange(0,1,0.01)
y = np.array([easeOutCirc(i) for i in x])

plt.plot(x,1-y)
plt.show()
