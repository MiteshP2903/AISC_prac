import numpy as np
import matplotlib.pyplot as plt

# Define universe
x = np.linspace(0, 10, 500)

# 1. Custom Triangular Function
def custom_trimf(x, a, b, c):
    """
    a: left foot, b: peak, c: right foot
    """
    term1 = (x - a) / (b - a)
    term2 = (c - x) / (c - b)
    return np.maximum(0, np.minimum(term1, term2))

# 2. Custom Trapezoidal Function
def custom_trapmf(x, a, b, c, d):
    """
    a, d: feet edges | b, c: plateau edges
    """
    term1 = (x - a) / (b - a)
    term2 = (d - x) / (d - c)
    return np.maximum(0, np.minimum(np.minimum(term1, 1), term2))

# 3. Custom Gaussian Function
def custom_gaussmf(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Generate values
tri_y = custom_trimf(x, 2, 5, 8)
trap_y = custom_trapmf(x, 1, 3, 7, 9)
gauss_y = custom_gaussmf(x, 5, 1.5)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, tri_y, label='Custom Triangular', linewidth=2)
plt.plot(x, trap_y, label='Custom Trapezoidal', linewidth=2)
plt.plot(x, gauss_y, label='Custom Gaussian', linewidth=2, linestyle='--')

plt.title('Fuzzy Membership Functions')
plt.xlabel('Universe of Discourse')
plt.ylabel('Membership Degree (μ)')
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True)
plt.show()
