import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# q = litres sold per month (hundreds not needed, plain units)
# Revenue = 30q - 0.005q^2   (price falls slightly at high volume)
# Cost    = 2000 + 8q + 0.01q^2
# Profit  = Revenue - Cost = 22q - 0.015q^2 - 2000
def profit(q):
    return 22*q - 0.015*q**2 - 2000

# Bisection: one root in each bracket
low = root_scalar(profit, bracket=[0, 500], method="bisect", xtol=1e-8)
high = root_scalar(profit, bracket=[1000, 2000], method="bisect", xtol=1e-8)

# Fixed-point for the lower root: q = (2000 + 0.015 q^2) / 22
def g(q):
    return (2000 + 0.015*q**2) / 22

q = 100.0
steps = 0
for _ in range(200):
    q_new = g(q)
    steps += 1
    if abs(q_new - q) < 1e-8:
        q = q_new
        break
    q = q_new

print(f"Lower break-even (bisection): {low.root:.2f} litres")
print(f"Upper break-even (bisection): {high.root:.2f} litres")
print(f"Lower break-even (fixed-point): {q:.2f} litres in {steps} iterations")
print(f"Profit at a sales volume of 700 litres: {profit(700):.2f}")

qs = np.linspace(0, 1600, 400)
plt.plot(qs, profit(qs))
plt.axhline(0, linewidth=0.8)
plt.axvline(low.root, linestyle="--")
plt.axvline(high.root, linestyle="--")
plt.xlabel("Litres sold per month")
plt.ylabel("Profit (KES)")
plt.title("Break-even points for a water-vending business")
plt.grid(True)
plt.savefig("images/task_10_break_even.png", dpi=150)
plt.show()