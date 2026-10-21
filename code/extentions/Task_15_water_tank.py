import numpy as np
import matplotlib.pyplot as plt

# Time in minutes and tank volume in litres
time = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)
volume = np.array([1000, 940, 890, 850, 820, 800, 790], dtype=float)

rate = np.zeros_like(volume)
rate[0] = (volume[1] - volume[0]) / (time[1] - time[0])

for i in range(1, len(time) - 1):
    rate[i] = (volume[i + 1] - volume[i - 1]) / (time[i + 1] - time[i - 1])

rate[-1] = (volume[-1] - volume[-2]) / (time[-1] - time[-2])

for t, v, r in zip(time, volume, rate):
    print(f"t={t:.0f} min, volume={v:.0f} L, rate of change={r:.2f} L/min")

plt.plot(time, -rate, marker="o")
plt.xlabel("Time (min)")
plt.ylabel("Outflow rate (L/min)")
plt.title("Water outflow rate estimated from tank volume")
plt.grid(True)
plt.savefig("images/task_15_water_tank.png", dpi=150)
plt.show()