import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Smart-meter readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson - energy_trapezoid):.3f} kWh")
print(f"Average power: {energy_trapezoid / (time_hours[-1] - time_hours[0]):.3f} kW")

plt.plot(time_hours, power_kw, marker="o")
plt.fill_between(time_hours, power_kw, alpha=0.3)
plt.xlabel("Time (hours)")
plt.ylabel("Power (kW)")
plt.title("Power use; shaded area = energy consumed")
plt.grid(True)
plt.savefig("images/task_16.png", dpi=150)
plt.show()