import numpy as np

# Input bipolar patterns
X = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])

# Corresponding output bipolar patterns
Y = np.array([
    [1, 1, -1],
    [-1, 1, 1]
])

# Initialize weight matrix
W = np.zeros((X.shape[1], Y.shape[1]))

# Hebbian Learning using Outer Product Method
for i in range(len(X)):
    W = W + np.outer(X[i], Y[i])

# Display weight matrix
print("Weight Matrix:")
print(W)

# Test input pattern
test_input = np.array([1, -1, 1, -1])

# Calculate net input
net_input = np.dot(test_input, W)

print("\nNet Input:")
print(net_input)

# Bipolar activation function
recalled_output = np.where(net_input >= 0, 1, -1)

# Display recalled output
print("\nRecalled Output Pattern:")
print(recalled_output)