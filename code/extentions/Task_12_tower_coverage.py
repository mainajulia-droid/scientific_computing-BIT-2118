import numpy as np
from scipy.optimize import root

# Tower 1 at (0, 0), range 5 km
# Tower 2 at (6, 0), range 4 km
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 5**2,
        (x - 6)**2 + y**2 - 4**2
    ]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print("Edge point (km):", np.round(solution.x, 4))
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()