import numpy as np
import matplotlib.pyplot as plt 

 
power = 400 # in watts
Vo = 4 # initial speed in m/s
h = 1
m = 70
u = 4
V = u
C = 0.0025 * 9.81 * m # constant frictional force
Roh = 1.225 # density of air in kg/m^3
A = 0.35 # cross-sectional area in m^2
time = np.arange(0, 200 + h, h) # time in seconds
speed_nIRL,speed_IRL,speed_nIRl_euler = np.array([]),np.array([]),np.array([]) # speed in m/s

for t in time:
    v = ((power * t / m) + Vo**2)**0.5
    Vn = V + h * (power/(m*V))
    Un = u + h * ((power/(m*v)) - C*Roh*A*u**2/(2*m))
    
    speed_nIRL = np.append(speed_nIRL, v)
    speed_nIRl_euler = np.append(speed_nIRl_euler, Vn)
    speed_IRL = np.append(speed_IRL, Un)
    V = Vn
    #u = Un
    print(f"At time {t:.2f} seconds, speed_nIRL = {v:.2f} m/s, speed_nIrl_euler = {V:.2f} m/s, speed_IRL = {u:.2f} m/s")




plt.plot(time, speed_nIRL, label="Speed of Bicycle (No Air Resistance)", linestyle='dashed')
plt.plot(time, speed_nIRl_euler, label="Speed of Bicycle (Euler Method)", linestyle='dotted')
plt.plot(time, speed_IRL, label="Speed of Bicycle (With Air Resistance)")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m/s)")
plt.title("Speed of Bicycle over Time")
plt.legend()
plt.show()
