import numpy as np
import matplotlib.pyplot as plt

# the points for generating the velocity field
y,x = np.mgrid[-3:3:100j,-3:3:100j]

# the initial conditions for generating stream lines
# provided as an array of points in the plane
xcoords = np.linspace(-3,3,22,endpoint=True)
ycoords = np.zeros_like(xcoords)
strmpts = np.array(zip(xcoords, ycoords))

u = 0.5*y
v = -8*x

plt.streamplot(x, y, u, v, start_points=strmpts, density=35)
plt.show()
