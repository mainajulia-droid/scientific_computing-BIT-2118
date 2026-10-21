import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

beds = 30
mean_patients = 24
N = 100_000

# Poisson distribution suits counts of random arrivals
patients = rng.poisson(mean_patients, N)

full = patients > beds
p_full = full.mean()
shortfall = np.maximum(patients - beds, 0)

print(f"Probability ward exceeds {beds} beds: {p_full:.2%}")
print(f"Average patients: {patients.mean():.2f}")
print(f"Worst day: {patients.max()} patients")
print(f"Average shortfall on overloaded days: {shortfall[full].mean():.2f} beds")

plt.hist(patients, bins=range(8, 46), density=True, alpha=0.7)
plt.axvline(beds + 0.5, linestyle="--", label=f"Capacity ({beds} beds)")
plt.xlabel("Patients present")
plt.ylabel("Fraction of days")
plt.title("Simulated daily ward occupancy")
plt.legend()
plt.grid(True)
plt.savefig("images/task_20_hospital_beds.png", dpi=150)
plt.show()