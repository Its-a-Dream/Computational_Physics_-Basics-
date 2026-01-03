import numpy as np
import matplotlib.pyplot as plt


dt = 0.001
eartth_v_scale = 0.5
pi = np.pi
GM_sun = 4*pi**2 # AU^3/yr^2
MJ_times = 1000
MJupiter = 0.0009543 * MJ_times # solar masses
r_jupiter = 5.2 #AU
MEarth = 0.000003003
years_total = 12
N = int(years_total/dt)


postiton_e = np.array([1.0, 0.0])
postiton_j = np.array([5.2, 0.0])

xe, ye = np.empty(N+1), np.empty(N+1)
xj, yj = np.empty(N+1), np.empty(N+1)

xe[0], ye[0] = postiton_e[0], postiton_e[1]
xj[0], yj[0] = postiton_j[0], postiton_j[1]

# Initial velocities (2D vectors)
v_e = np.array([0.0, eartth_v_scale * 2 * pi / np.sqrt(np.linalg.norm(postiton_e))])
vj = np.array([0.0, 2 * pi / np.sqrt(np.linalg.norm(postiton_j))])

plt.ion()
fig, ax = plt.subplots(figsize=(8,8))
lineE, = ax.plot([], [], label='Earth Orbit', color='blue')
lineJ, = ax.plot([], [], label='Jupiter Orbit', color='orange')
sun = ax.scatter(0, 0, color='yellow', s=200, label='Sun')

# for eart and jupiter as dots
dotE = ax.scatter([], [], color='blue', s=50, label='Earth', zorder=5)
dotJ = ax.scatter([], [], color='orange', s=100, label='Jupiter', zorder=5)

ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')
ax.set_title(f'Orbital Simulation of Earth and Jupiter (with mass change of {MJ_times}x) around the Sun')
ax.legend()
ax.grid(True)
ax.set_aspect('equal', 'box')
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# how often to redraw (every few steps for performance)     
redraw_every = 50

# Time integration (simple explicit Euler) with dynamic drawing
for i in range(1, N+1):
    # current distances
    rE_mag = np.linalg.norm(postiton_e)
    rJ_mag = np.linalg.norm(postiton_j)
    rEJ_vec = postiton_j - postiton_e
    rEJ_mag = np.linalg.norm(rEJ_vec)

    # accelerations: Sun on body and planet-planet interaction
    accE = -GM_sun * postiton_e / rE_mag**3 + GM_sun * MJupiter * (rEJ_vec / rEJ_mag**3)

    accJ = -GM_sun * postiton_j / rJ_mag**3 - GM_sun * MEarth * (rEJ_vec / rEJ_mag**3)

    v_e += accE * dt
    vj += accJ * dt

    postiton_e = postiton_e + v_e * dt
    postiton_j = postiton_j + vj * dt


    xe[i], ye[i] = postiton_e[0], postiton_e[1]
    xj[i], yj[i] = postiton_j[0], postiton_j[1]

    # dynamic redraw
    if (i % redraw_every) == 0 or i == N:
        lineE.set_data(xe[:i+1], ye[:i+1])
        lineJ.set_data(xj[:i+1], yj[:i+1])
        
        # Update planet positions (giant dots)
        dotE.set_offsets(np.c_[postiton_e[0], postiton_e[1]])
        dotJ.set_offsets(np.c_[postiton_j[0], postiton_j[1]])

        plt.draw()
        plt.pause(0.001)


plt.ioff()
plt.show()
