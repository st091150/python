from matplotlib import projections
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
import pandas as pd


ax=axes3d.Axes3D(plt.figure())

i = np.arange(-1, 1 ,0.01)
X, Y = np.meshgrid(i,i)
Z = X**2 -Y**2

ax.plot_wireframe(X,Y,Z, rstride = 10, cstride=10)

plt.show()


