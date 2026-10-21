import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Time in minutes and flow rate in litres per minute
time_min = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120], dtype=float)
flow_lpm = np.array([0, 12, 20, 25, 22, 18, 10, 5, 0], dtype=float)

water_trapezoid = np.trapezoid(flow_lpm, time_min)
water_simpson = simpson(flow_lpm, x=time_min)

print(f"Total water (trapezoid): {water_trapezoid:.0f} L")
print(f"Total water (Simpson): {water_simpson:.0f} L")
print(f"Difference: {abs(water_simpson - water_trapezoid):.0f} L")
print(f"Peak flow: {flow_lpm.max():.0f} L/min at t = {time_min[flow_lpm.argmax()]:.0f} min")

plt.plot(time_min, flow_lpm, marker="o")
plt.fill_between(time_min, flow_lpm, alpha=0.3)
plt.xlabel("Time (minutes)")
plt.ylabel("Flow rate (L/min)")
plt.title("Irrigation flow; shaded area = total water used")
plt.grid(True)
plt.savefig("images/task_16_water_usage.png", dpi=150)
plt.show()