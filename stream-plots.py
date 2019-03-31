import numpy as np
import matplotlib.pyplot as plt

y,x = np.mgrid[-3:3:100j,-3:3:100j]

u = 0.5*y
v = -8*x

plt.streamplot(x,y,u,v,density=1)
plt.show()
