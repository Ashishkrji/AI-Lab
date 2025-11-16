#Create a back propagation network for a given input pattern. Perform 3 epochs of operation.

import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (4 patterns of XOR logic)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1

# Weights
W1 = np.random.uniform(-1, 1, (input_layer_size, hidden_layer_size))  # (2x2)
W2 = np.random.uniform(-1, 1, (hidden_layer_size, output_layer_size))  # (2x1)

# Biases
b1 = np.zeros((1, hidden_layer_size))
b2 = np.zeros((1, output_layer_size))

# Learning rate
lr = 0.5

# Train for 3 epochs
epochs = 3
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")

    # ----------- FORWARD PASS -----------
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)  # final output

    # ----------- LOSS (mean squared error) -----------
    loss = np.mean((y - a2) ** 2)
    print("Loss:", loss)

    # ----------- BACKWARD PASS -----------
    # Output layer error
    error_output = y - a2
    d_output = error_output * sigmoid_derivative(a2)

    # Hidden layer error
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(a1)

    # ----------- WEIGHT & BIAS UPDATE -----------
    W2 += a1.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr

    W1 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

    print("Updated W1:\n", W1)
    print("Updated W2:\n", W2)

# Final output after training
print("\nFinal output after 3 epochs:")
print(a2)