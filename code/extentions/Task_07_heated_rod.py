import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Steady-state temperatures at 3 interior points of a rod.
# Each point is the average of its two neighbours: 2*T_i - T_(i-1) - T_(i+1) = 0
A = np.array([
    [ 2.0, -1.0,  0.0],
    [-1.0,  2.0, -1.0],
    [ 0.0, -1.0,  2.0]
])

# The left end is always 100 C. The right end changes.
right_end_temps = [0.0, 20.0, 40.0]

lu, piv = lu_factor(A)

for right in right_end_temps:
    b = np.array([100.0, 0.0, right])
    T = lu_solve((lu, piv), b)
    residual = np.linalg.norm(b - A @ T)
    print(f"Right end = {right:.0f} C -> interior temperatures: {np.round(T, 2)} (residual {residual:.1e})")