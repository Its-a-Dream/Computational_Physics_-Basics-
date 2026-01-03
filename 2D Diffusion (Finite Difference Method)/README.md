# 2D Diffusion Solver Using Finite Difference Method

## Overview
This notebook solves the 2D diffusion equation using the **Finite Difference Method (FDM)**. It implements two different approaches to simulate how a pollutant or concentration spreads over a 2D spatial domain over time.

## Physics Background
The 2D diffusion equation is given by:

$$\frac{\partial C}{\partial t} = D \left(\frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2}\right)$$

Where:
- **C** = concentration at position (x, y, t)
- **D** = diffusion constant
- **t** = time

## Two Solution Methods

### Method 1: Fixed Final Time
Simulates diffusion over a predetermined time period (40 seconds by default).

**Key Features:**
- Runs for a fixed number of iterations based on total time
- Plots the concentration distribution at each time step
- Tracks the maximum concentration over time
- Checks stability condition at the end

**Parameters:**
```
D = 0.4          # Diffusion constant
N = 21           # Grid dimension (21x21)
dx = dy = 1      # Spatial step size
dt = 0.2         # Time step
tt = 40          # Total simulation time (seconds)
val = 50         # Initial concentration value
```

**Output:**
- Initial and final concentration plots
- Real-time visualization of diffusion progression
- Plot of maximum concentration vs. time
- Total concentration at all positions
- Stability analysis

### Method 2: Entropy-Based Termination
Simulates diffusion until the system reaches equilibrium based on entropy change.

**Key Features:**
- Runs until entropy change becomes negligible (< 0.001)
- More physically intuitive as it stops when equilibrium is reached
- Automatically determines simulation duration
- Useful for understanding equilibrium states

**Parameters:**
```
D = 0.4          # Diffusion constant
N = 21           # Grid dimension (21x21)
dx = dy = 1      # Spatial step size
dt = 0.2         # Time step
val = 50         # Initial concentration value
```

**Output:**
- Initial and final concentration plots
- Real-time visualization until equilibrium
- Total concentration at equilibrium
- Simulation time to reach equilibrium
- Stability analysis

## Stability Condition
Both methods check the **Courant-Friedrichs-Lewy (CFL) stability condition**:

$$r_x + r_y \leq 0.5$$

Where:
$$r_x = \frac{D \cdot dt}{dx^2}, \quad r_y = \frac{D \cdot dt}{dy^2}$$

If $r_x + r_y > 0.5$, the solution is **unstable** and results may be inaccurate.

## Key Functions

### `plotting(arr2d, max=0, title="")`
- Displays a 2D heatmap of the concentration distribution
- Uses interpolation for smoother visualization
- Includes colorbar and axis labels

## How to Use

1. **Run the notebook cells** sequentially
2. **Method 1:** Choose fixed time method for deterministic simulations
3. **Method 2:** Choose entropy method for equilibrium-based simulations
4. **Adjust parameters** (D, N, dt, val) to see how they affect diffusion behavior
5. **Uncomment** `display.clear_output(wait=True)` to see all plots or leave commented to see only final result

## Requirements
- NumPy
- Matplotlib
- IPython (for Jupyter notebook)

## Physical Interpretation
- **Initial condition:** Point source at the center of the grid
- **Diffusion:** The concentration spreads outward following Gaussian-like profile
- **Equilibrium:** Eventually, concentration becomes uniform across the domain
- **Conservation:** Total mass (concentration) is approximately conserved

## Notes
- The initial concentration is placed at the center: `C[N//2, N//2] = val`
- The finite difference discretization uses explicit forward-time, centered-space (FTCS) scheme
- Boundary conditions: Zero concentration at domain edges (Dirichlet boundary condition)
