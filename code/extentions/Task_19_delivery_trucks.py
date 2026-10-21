import numpy as np
from scipy.optimize import minimize

# x = small trucks, y = large trucks
# Small: 4 tonnes, 3.0 (thousand KES) per trip
# Large: 10 tonnes, 6.5 (thousand KES) per trip
# Need at least 60 tonnes; at most 4 large trucks exist

def cost(z):
    x, y = z
    return 3.0*x + 6.5*y

def tonnes_constraint(z):
    x, y = z
    return 4*x + 10*y - 60

solution = minimize(
    cost,
    x0=[10, 2],
    method="SLSQP",
    bounds=[(0, None), (0, 4)],
    constraints={"type": "ineq", "fun": tonnes_constraint}
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Small trucks: {x:.3f}")
print(f"Large trucks: {y:.3f}")
print(f"Tonnes moved: {4*x + 10*y:.2f}")
print(f"Minimum cost: {solution.fun:.2f} thousand KES")

best_integer = None

for a in range(0, 31):
    for b in range(0, 5):
        tonnes = 4*a + 10*b

        if tonnes >= 60:
            total_cost = 3.0*a + 6.5*b

            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, tonnes)

print("Best whole-truck solution:", best_integer)