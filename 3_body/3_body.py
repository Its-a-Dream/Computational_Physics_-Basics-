import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
eartth_v_scale = 0.83
pi = np.pi
GM_sun = 4*pi**2 # AU^3/yr^2
MJupiter = 0.0009543 * 1 # solar masses
r_jupiter = 5.2 #AU
MEarth = 0.000003003
years_total = 12
N =int(years_total/dt)

postiton_e = np.array([1.0, 0.0])
postiton_j = np.array([5.2, 0.0])

xe, ye = np.empty(N+1), np.empty(N+1)
xj, yj = np.empty(N+1), np.empty(N+1)

# store initial positions
xe[0], ye[0] = postiton_e[0], postiton_e[1]
xj[0], yj[0] = postiton_j[0], postiton_j[1]

# Initial velocities (2D vectors)
v_e = np.array([0.0, eartth_v_scale * 2 * pi / np.sqrt(np.linalg.norm(postiton_e))])
vj = np.array([0.0, 2 * pi / np.sqrt(np.linalg.norm(postiton_j))])

# Time integration (simple explicit Euler)
for i in range(1, N+1):
    # current distances
    rE_mag = np.linalg.norm(postiton_e)
    rJ_mag = np.linalg.norm(postiton_j)
    rEJ_vec = postiton_j - postiton_e
    rEJ_mag = np.linalg.norm(rEJ_vec)

    # accelerations: Sun on body and planet-planet interaction
    # acceleration on Earth: due to Sun + due to Jupiter
    accE = -GM_sun * postiton_e / rE_mag**3 + GM_sun * MJupiter * (rEJ_vec / rEJ_mag**3)
    # acceleration on Jupiter: due to Sun + due to Earth
    accJ = -GM_sun * postiton_j / rJ_mag**3 - GM_sun * MEarth * (rEJ_vec / rEJ_mag**3)

    # update velocities
    v_e += accE * dt
    vj += accJ * dt

    # update positions
    postiton_e = postiton_e + v_e * dt
    postiton_j = postiton_j + vj * dt

    # store histories
    xe[i], ye[i] = postiton_e[0], postiton_e[1]
    xj[i], yj[i] = postiton_j[0], postiton_j[1]

plt.figure(figsize=(8,8))
plt.plot(xe, ye, label='Earth Orbit', color='blue')
plt.plot(xj, yj, label='Jupiter Orbit', color='orange')
plt.scatter(0, 0, color='yellow', s=200, label='Sun')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title('orbital Simulation of Earth and Jupiter around the Sun')
plt.legend()
plt.grid(True)
plt.show()