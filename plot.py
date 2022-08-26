import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# y = x*x   
# f(x) = x*x
# xpoints = np.array([1, 2, 3, 4,   5,  6, 7])
# ypoints = np.array([1, 4, 9, 16, 25, 36, 49])

# function 
# y = 2*x + 1 
# f(x)= 2*x + 1 
# xpoints = np.array([])
# ypoints = np.array([])

# xpoints = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
# ypoints = xpoints**2

xpoints = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
ypoints = xpoints**3 - 20*xpoints**2 + 5*xpoints + 1

plt.plot(xpoints, ypoints)
plt.show()
