import numpy as np
import matplotlib.pyplot as plt
x_data = np.arange(-2, 2.01, 0.001)
n = 20
b = 0.5
a = 3
y_data = np.array([])
y = np.array([])
for x in x_data:
    for i in range(n):
        y = np.append(y, np.cos(np.pi*x*a**i)*b**i)
    y_sum = np.sum(y)
    y_data = np.append(y_data, y_sum)
    y = np.array([])
 
plt.plot(x_data, y_data)
plt.axis('equal')
plt.grid = True
plt.show()