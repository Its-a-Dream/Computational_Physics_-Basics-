import numpy as np
import matplotlib.pyplot as plt

y = np.array ([0.01675, 0.0205, 0.0266, 0.030])
x = np.array ([0.0412, 0.0530, 0.0864, 0.2758])

slope, intercept = np.polyfit(x, y, 1)
line_of_best_fit = slope * x + intercept

plt.scatter(x, y, label="relationship between the crater diameter (D) and the impact kinetic energy (E)")
plt.plot(x, line_of_best_fit, color='red', label='Line of Best Fit')
plt.xlabel("Crater Diameter (D)")
plt.ylabel("Impact Kinetic Energy (E)")
plt.title("Crater Diameter vs Impact Kinetic Energy")
plt.legend()
plt.show()