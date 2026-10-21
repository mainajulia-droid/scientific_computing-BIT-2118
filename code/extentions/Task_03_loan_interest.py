import numpy as np
import timeit

# Balances of 1,000,000 customers in KES (assumed between 500 and 100,000)
rng = np.random.default_rng(7)
balances = rng.uniform(500, 100_000, 1_000_000)

annual_rate = 0.08
years = 3

def loop_version():
    result = []
    for b in balances:
        result.append(b * (1 + annual_rate) ** years)
    return result

def vectorized_version():
    return balances * (1 + annual_rate) ** years

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

future = vectorized_version()

print("First five future balances (KES):", np.round(future[:5], 2))
print(f"Total bank liability after {years} years: KES {future.sum():,.0f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Speed-up: {loop_time/vector_time:.1f}x")