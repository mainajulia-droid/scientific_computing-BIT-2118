import numpy as np

# Farm plot corners in metres: 40 m by 25 m
plot = np.array([
    [0.0, 0.0],
    [40.0, 0.0],
    [40.0, 25.0],
    [0.0, 25.0]
])

angle = np.deg2rad(30)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Map distortion: 1.2 on x, 0.8 on y
distortion = np.diag([1.2, 0.8])

T = rotation @ distortion
mapped = plot @ T.T

original_area = 40 * 25
mapped_area = original_area * np.linalg.det(T)

print("Mapped corners:\n", np.round(mapped, 2))
print("Determinant:", round(np.linalg.det(T), 4))
print(f"Original area: {original_area} m^2")
print(f"Mapped area: {mapped_area:.1f} m^2")