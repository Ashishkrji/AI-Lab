# Create a perceptron with appropriate no. of inputs and outputs. Train it using fixed
# increment learning algorithm until no change in weights is required. Output the final weights.

# Perceptron using Fixed Increment Learning Algorithm

# Training data for AND gate
training_inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Corresponding target outputs
targets = [0, 0, 0, 1]

# Parameters
learning_rate = 1
epochs = 100  # maximum iterations to prevent infinite loop

# Initialize weights (2 for inputs + 1 for bias)
weights = [0, 0, 0]  # w1, w2, bias

# Training loop
for epoch in range(epochs):
    error_count = 0
    for inputs, target in zip(training_inputs, targets):
        x1, x2 = inputs
        bias_input = 1  # bias input is always 1

        # Weighted sum
        weighted_sum = weights[0]*x1 + weights[1]*x2 + weights[2]*bias_input

        # Activation (step function)
        output = 1 if weighted_sum > 0 else 0

        # Error
        error = target - output

        # Update rule if error
        if error != 0:
            weights[0] += learning_rate * error * x1
            weights[1] += learning_rate * error * x2
            weights[2] += learning_rate * error * bias_input
            error_count += 1

    # Stop if no errors
    if error_count == 0:
        print(f"Training converged at epoch {epoch + 1}")
        break

# Output final weights
print("Final weights:")
print(f"w1 = {weights[0]}, w2 = {weights[1]}, bias = {weights[2]}")