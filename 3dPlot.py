import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X = np.arange(1, 10)
Y = np.arange(1, 10)
X, Y = np.meshgrid(X, Y)
Z = np.arange(1, 10)
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
ax.set_zlim(1, 10)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
