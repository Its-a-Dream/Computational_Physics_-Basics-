import numpy as np
import matplotlib.pyplot as plt

B = 0.5 
S0 = 0.1
w = 0.4
g = 9.81
v0 = 50 
m = 0.25
T = 10
theta = 30
dt = 0.01                      
time = np.arange(0, T + dt, dt)
N = time.size

x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

vx[0] = v0 * np.cos(np.radians(theta))
vy[0] = v0 * np.sin(np.radians(theta))

def ay(vx, vy):
    v = np.hypot(vx, vy)
    alpha = B * v / m
    gamma = S0 * w / m
    return -alpha * vy + gamma * vx - g

def ax(vx, vy):
    v = np.hypot(vx, vy)
    alpha = B * v / m
    gamma = S0 * w / m
    return -alpha * vx - gamma * vy

def dxdt(vx):
    return vx

def dydt(vy):
    return vy



for i in range(N - 1):
    if y[i] < 0:
        break
    k1vx = ax(vx[i], vy[i])
    k1vy = ay(vx[i], vy[i])
    k1x = dxdt(vx[i])
    k1y = dydt(vy[i])

    k2vx = ax(vx[i] + 0.5 * dt * k1vx, vy[i] + 0.5 * dt * k1vy)
    k2vy = ay(vx[i] + 0.5 * dt * k1vx, vy[i] + 0.5 * dt * k1vy)
    k2x = dxdt(vx[i] + 0.5 * dt * k1vx)
    k2y = dydt(vy[i] + 0.5 * dt * k1vy)

    k3vx = ax(vx[i] + 0.5 * dt * k2vx, vy[i] + 0.5 * dt * k2vy)
    k3vy = ay(vx[i] + 0.5 * dt * k2vx, vy[i] + 0.5 * dt * k2vy)
    k3x = dxdt(vx[i] + 0.5 * dt * k2vx)
    k3y = dydt(vy[i] + 0.5 * dt * k2vy)

 
    k4vx = ax(vx[i] + dt * k3vx, vy[i] + dt * k3vy)
    k4vy = ay(vx[i] + dt * k3vx, vy[i] + dt * k3vy)
    k4x = dxdt(vx[i] + dt * k3vx)
    k4y = dydt(vy[i] + dt * k3vy)

    vx[i+1] = vx[i] + dt * (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6.0
    vy[i+1] = vy[i] + dt * (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6.0
    x[i+1] = x[i] + dt * (k1x + 2*k2x + 2*k3x + k4x) / 6.0
    y[i+1] = y[i] + dt * (k1y + 2*k2y + 2*k3y + k4y) / 6.0



# plotting
plt.plot(x, y, label="Trajectory")
plt.title("Projectile Motion with Air Resistance and Wind")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid(True)
plt.show()
