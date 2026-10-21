import numpy as np
import matplotlib.pyplot as plt

n = 9
A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

b = np.zeros(n)
b[0] = 200.0    # left end temperature
b[-1] = 50.0    # right end temperature


def jacobi(A, b, tol=1e-8, max_iter=2000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x_new, errors

        x = x_new

    return x, errors


def gauss_seidel(A, b, tol=1e-8, max_iter=2000):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()

        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x, errors

    return x, errors


x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Exact temperatures:", np.round(x_exact, 2))
print("Jacobi max error vs exact:", np.max(np.abs(x_j - x_exact)))
print("Gauss-Seidel max error vs exact:", np.max(np.abs(x_gs - x_exact)))
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence for a 9-point rod")
plt.legend()
plt.grid(True)
plt.savefig("images/task_08_longer_rod.png", dpi=150)
plt.show()