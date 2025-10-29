
   
import math 
import numpy as np
import matplotlib.pyplot as plt
t_0 = 0
tau = 1
T = 1
h = 0.0001  # dt
y = 1000 # initial value (y at t=0)


vector_timeFrame = np.arange(t_0, T+h, h)
print(vector_timeFrame)


y_array = np.array([])
N_exact_array = np.array([])
for t in range(len(vector_timeFrame)-1):
    y_n = y *(1-(h/tau))
    N_exact = y * math.exp(-t/tau)
    y_array = np.append(y_array, y)
    N_exact_array = np.append(N_exact_array, N_exact)
    y = y_n
    print(f"At time {t:.2f}, y = {y:.2f}, h = {h:.2f} , Exact N = {N_exact:.2f}")

plt.plot(vector_timeFrame, y_array, label="Numerical Solution")
plt.plot(vector_timeFrame, N_exact_array, label="Exact Solution", linestyle='dashed')
plt.xlabel("Time")
plt.ylabel("y")
plt.title("Plot of y over time")
plt.legend()
plt.show()