# Construct and test auto associative network for input vector using outer product rule.

import numpy as np

# Bipolar input vector (example)
x = np.array([1, -1, 1, -1])

# Outer product learning rule: W = x * x^T
W = np.outer(x, x)

# Set diagonal to zero (no self-connection)
np.fill_diagonal(W, 0)

# Test the network with original input (should recall same)
def recall(input_vec, W):
    y = np.sign(W @ input_vec)
    return y

print("Weight matrix:\n", W)

# Test with original input
output = recall(x, W)
print("Input vector:     ", x)
print("Recalled output:  ", output)

# Test with noisy input
noisy_input = np.array([1, -1, -1, -1])  # flipped 3rd bit
noisy_output = recall(noisy_input, W)
print("Noisy input:      ", noisy_input)
print("Recalled output:  ", noisy_output)