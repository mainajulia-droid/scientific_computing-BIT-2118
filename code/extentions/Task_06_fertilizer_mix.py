import numpy as np

# x = kg of Fertilizer 1 (20% nitrogen, 10% phosphorus)
# y = kg of Fertilizer 2 (10% nitrogen, 30% phosphorus)
# Required: 14 kg nitrogen and 16 kg phosphorus

A = np.array([
    [0.20, 0.10],   # nitrogen fraction
    [0.10, 0.30]    # phosphorus fraction
])

b = np.array([14.0, 16.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Fertilizer 1: {solution[0]:.2f} kg")
print(f"Fertilizer 2: {solution[1]:.2f} kg")
print(f"Total mix: {solution.sum():.2f} kg")
print("Nutrients delivered (N, P):", A @ solution)
print("Residual norm:", np.linalg.norm(residual))