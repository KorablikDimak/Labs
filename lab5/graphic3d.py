import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

fig = plt.figure()
axes = fig.add_subplot(projection='3d')
axes.plot_surface(xgrid, ygrid, zgrid)
plt.show()
