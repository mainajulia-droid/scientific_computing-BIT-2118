import numpy as np

# Node order: Market, V1, V2, V3, V4
# The market town is joined by road to each village; villages are not joined to each other.
roads = np.array([
    [0., 1., 1., 1., 1.],
    [1., 0., 0., 0., 0.],
    [1., 0., 0., 0., 0.],
    [1., 0., 0., 0., 0.],
    [1., 0., 0., 0., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(roads)

index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
vector = np.abs(np.real(eigenvectors[:, index]))
centrality = vector / vector.sum()

places = ["Market", "V1", "V2", "V3", "V4"]

print("All eigenvalues:", np.round(np.sort(np.real(eigenvalues)), 4))
print("Dominant eigenvalue:", round(dominant_value, 4))
for place, score in zip(places, centrality):
    print(f"{place}: {score:.4f}")

v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(roads @ v - dominant_value * v))