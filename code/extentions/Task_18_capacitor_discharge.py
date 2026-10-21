import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

R = 4700.0        # ohms
C = 0.001         # farads
V0 = 12.0         # starting voltage (V)
safe_voltage = 1.0

def discharge(t, V):
    return [-V[0] / (R * C)]

def reaches_safe(t, V):
    return V[0] - safe_voltage

reaches_safe.terminal = False
reaches_safe.direction = -1     # only detect the voltage falling through 1 V

t_eval = np.linspace(0, 30, 300)

solution = solve_ivp(
    discharge,
    (0, 30),
    [V0],
    t_eval=t_eval,
    events=reaches_safe,
    rtol=1e-9,
    atol=1e-11
)

exact = V0 * np.exp(-solution.t / (R * C))
safe_time = solution.t_events[0][0]

print("Solver success:", solution.success)
print(f"Time constant RC = {R * C:.2f} s")
print(f"Voltage after 10 s: {np.interp(10, solution.t, solution.y[0]):.3f} V")
print(f"Voltage after 30 s: {solution.y[0, -1]:.4f} V")
print(f"Time to reach {safe_voltage:.0f} V (event): {safe_time:.3f} s")
print(f"Time to reach {safe_voltage:.0f} V (exact): {R * C * np.log(V0 / safe_voltage):.3f} s")
print(f"Maximum error: {np.max(np.abs(solution.y[0] - exact)):.3e} V")

plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact")
plt.axhline(safe_voltage, linewidth=0.8, label="Safe level (1 V)")
plt.axvline(safe_time, linestyle=":", linewidth=0.8)
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Capacitor discharge after power-off")
plt.legend()
plt.grid(True)
plt.savefig("images/task_18_capacitor_discharge.png", dpi=150)
plt.show()