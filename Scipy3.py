import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([[0, 4], [2, 1.5], [1, 3], [1, 2.2]])
tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()