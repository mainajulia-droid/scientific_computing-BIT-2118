import math
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Extra: standard error and exact (theoretical) answer for comparison
std_error = np.sqrt(overload_probability * (1 - overload_probability) / N)
z = (capacity - mean_demand) / std_demand
theory = 0.5 * math.erfc(z / math.sqrt(2))
print(f"Standard error: {std_error:.4%}")
print(f"Theoretical probability: {theory:.4%}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)
plt.axhline(theory, linestyle="--", linewidth=0.8, label="Theoretical value")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.legend()
plt.grid(True)
plt.savefig("images/task_20.png", dpi=150)
plt.show()
