import numpy as np
import matplotlib.pyplot as plt

T_ambient = 22.0
T_initial = 85.0
k = 0.07           # per minute
h = 2.0            # minutes
end_time = 40.0
drinkable = 60.0

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

# First time step at which Euler is at or below the drinkable temperature
idx = np.argmax(temperature <= drinkable)
exact_time = np.log((T_initial - T_ambient) / (drinkable - T_ambient)) / k

print(f"Euler temperature after 40 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 40 min: {exact[-1]:.2f} C")
print(f"Euler first at or below {drinkable:.0f} C at t = {time[idx]:.0f} min ({temperature[idx]:.2f} C)")
print(f"Exact time to reach {drinkable:.0f} C: {exact_time:.1f} min")

plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.axhline(drinkable, linestyle="--", linewidth=0.8, label="Drinkable (60 C)")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a cup of tea")
plt.legend()
plt.grid(True)
plt.savefig("images/task_17_tea.png", dpi=150)
plt.show()