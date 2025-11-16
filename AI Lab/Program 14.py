# Construct and test auto associative network for input vector using HEBB rule.

import numpy as np

# Bipolar input pattern (can be more than one)
X = np.array([[1, -1, 1, -1]])  # shape: (1, 4)

# Hebbian learning rule: W = X^T * X
W = X.T @ X

# Set diagonal to 0 (no self-connection)
np.fill_diagonal(W, 0)

# Test input (can also try with noisy input)
test_input = np.array([1, -1, 1, -1])

# Compute output: Y = sign(W * X)
output = np.sign(W @ test_input)

print("Weight matrix:\n", W)
print("Test input:    ", test_input)
print("Recalled output:", output)