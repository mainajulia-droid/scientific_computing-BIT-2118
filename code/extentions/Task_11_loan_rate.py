from scipy.optimize import root_scalar

# Borrower receives 20,000 now and repays 4,000 at the end of each of 6 months
cash_flows = [20000] + [-4000] * 6

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1)
               for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.05, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.01, x1=0.10, method="secant", xtol=1e-12)

monthly = newton.root
nominal_annual = monthly * 12
effective_annual = (1 + monthly)**12 - 1

print(f"Monthly rate (Newton): {monthly:.4%}")
print(f"Monthly rate (Secant): {secant.root:.4%}")
print(f"Nominal annual rate: {nominal_annual:.2%}")
print(f"Effective annual rate: {effective_annual:.2%}")
print(f"Total repaid: {4000 * 6} KES, interest paid: {4000 * 6 - 20000} KES")