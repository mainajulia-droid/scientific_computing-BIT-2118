import numpy as np

# Daily rainfall (mm) at a farm over 7 days
rain_mm = np.array([0.0, 2.5, 10.2, 0.0, 5.1, 18.4, 3.3])

print(f"Total rainfall: {np.sum(rain_mm):.1f} mm")
print(f"Average per day: {np.mean(rain_mm):.2f} mm")
print(f"Wettest day: {np.max(rain_mm):.1f} mm (day {np.argmax(rain_mm) + 1})")
print(f"Dry days: {np.sum(rain_mm == 0)}")

# Vectorized conversion to inches
rain_in = rain_mm / 25.4
print("Rainfall in inches:", np.round(rain_in, 2))
