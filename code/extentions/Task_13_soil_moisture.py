import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Soil moisture (%) measured every 4 hours
hours = np.array([0, 4, 8, 12, 16, 20, 24], dtype=float)
moisture = np.array([32.0, 30.0, 27.0, 24.0, 29.0, 31.0, 30.0])
# Irrigation is switched on between 12:00 and 16:00, so the moisture rises.

linear = interp1d(hours, moisture, kind="linear")
cubic = CubicSpline(hours, moisture)

missing_time = 14.0
print(f"Linear estimate at 14:00: {float(linear(missing_time)):.2f} %")
print(f"Cubic estimate at 14:00: {float(cubic(missing_time)):.2f} %")

t = np.linspace(0, 24, 300)
plt.scatter(hours, moisture, label="Sensor readings")
plt.plot(t, linear(t), label="Linear")
plt.plot(t, cubic(t), label="Cubic spline")
plt.axvline(missing_time, linestyle="--", linewidth=0.8)
plt.xlabel("Hour of day")
plt.ylabel("Soil moisture (%)")
plt.title("Estimating a missing soil-moisture reading")
plt.legend()
plt.grid(True)
plt.savefig("images/task_13_soil_moisture.png", dpi=150)
plt.show()