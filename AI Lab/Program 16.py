#Construct and test heteroassociative network for binary inputs and targets.

import numpy as np

# Define binary inputs and targets
inputs = np.array([[0,0],
                   [0,1],
                   [1,0],
                   [1,1]])

targets = np.array([[1,0],
                    [1,1],
                    [0,0],
                    [0,1]])

# Convert binary {0,1} to bipolar {-1,1} for Hebbian learning
def binary_to_bipolar(x):
    return 2*x - 1

inputs_bipolar = binary_to_bipolar(inputs).T  # shape: (input_dim, samples)
targets_bipolar = binary_to_bipolar(targets).T  # shape: (target_dim, samples)

# Hebbian learning: W = sum of (target * input^T)
W = targets_bipolar @ inputs_bipolar.T

print("Weight matrix W:\n", W)

# Test recall function
def recall(input_vec, W):
    net = W @ input_vec
    # Apply sign activation and convert back to binary
    output_bipolar = np.sign(net)
    output_bipolar[output_bipolar == 0] = 1  # treat zeros as 1
    output_binary = (output_bipolar + 1) // 2
    return output_binary

print("\nTesting Heteroassociative Network:")
for i in range(inputs.shape[0]):
    inp = inputs_bipolar[:, i]
    out = recall(inp, W)
    print(f"Input (binary): {inputs[i]} => Output (binary): {out.flatten()}") 