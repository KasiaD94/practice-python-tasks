import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [1, 4],
    [2, 2]
])
print (data)
x, y = data
#plt.scatter(data.T)
plt.scatter(x,y)
plt.show()

