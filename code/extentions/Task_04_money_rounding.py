import numpy as np
import math
from decimal import Decimal

fee = 0.1          # KES per transaction
n = 1_000_000      # number of transactions

# 1. Naive float accumulation
total_float = 0.0
for _ in range(n):
    total_float += fee

# 2. Accurate summation
total_fsum = math.fsum([fee] * n)

# 3. Decimal arithmetic (exact decimals, used in finance)
total_decimal = Decimal("0.1") * n

expected = 100000.0
print(f"Naive float total: {total_float:.8f}")
print(f"math.fsum total:   {total_fsum:.8f}")
print(f"Decimal total:     {total_decimal}")
print(f"Naive equals expected? {total_float == expected}")
print(f"isclose to expected?   {np.isclose(total_float, expected)}")
print(f"Absolute error: {abs(total_float - expected):.8f}")
print(f"Relative error: {abs(total_float - expected)/expected:.3e}")