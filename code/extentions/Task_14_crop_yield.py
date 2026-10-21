import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Fertilizer rate (kg per hectare) and maize yield (tonnes per hectare)
fertilizer = np.array([0, 20, 40, 60, 80, 100], dtype=float)
yield_t = np.array([2.1, 3.0, 3.7, 4.1, 4.2, 4.0])

def model(x, a, b, c):
    return a*x**2 + b*x + c

(a, b, c), _ = curve_fit(model, fertilizer, yield_t)

predicted = model(fertilizer, a, b, c)
rmse = np.sqrt(np.mean((yield_t - predicted)**2))

# The vertex of the parabola is the best rate
best_rate = -b / (2*a)
best_yield = model(best_rate, a, b, c)

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.3f}")
print(f"RMSE: {rmse:.3f} t/ha")
print(f"Best fertilizer rate: {best_rate:.1f} kg/ha")
print(f"Maximum predicted yield: {best_yield:.2f} t/ha")
print(f"Predicted yield at 120 kg/ha: {model(120, a, b, c):.2f} t/ha")

x_plot = np.linspace(0, 120, 300)
plt.scatter(fertilizer, yield_t, label="Trial plots")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.axvline(best_rate, linestyle="--", linewidth=0.8)
plt.xlabel("Fertilizer (kg/ha)")
plt.ylabel("Maize yield (t/ha)")
plt.title("Maize yield versus fertilizer rate")
plt.legend()
plt.grid(True)
plt.savefig("images/task_14_crop_yield.png", dpi=150)
plt.show()