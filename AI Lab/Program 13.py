# Implement AND function using MADALINE with bipolar inputs and outputs.

# MADALINE for AND Function (Bipolar Inputs/Outputs)

X = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
T = [-1, -1, -1, 1]

# Initialize weights and biases for 2 hidden ADALINE units
w1 = [0.0, 0.0]  # weights for neuron 1
w2 = [0.0, 0.0]  # weights for neuron 2
b1, b2 = 0.0, 0.0
lr = 0.1

# Activation function (sign)
def sign(n): return 1 if n >= 0 else -1

for epoch in range(100):
    for i in range(4):
        x1, x2 = X[i]
        t = T[i]

        # Hidden layer outputs
        net1 = w1[0]*x1 + w1[1]*x2 + b1
        net2 = w2[0]*x1 + w2[1]*x2 + b2
        z1, z2 = sign(net1), sign(net2)

        # Output of MADALINE (majority vote or sign sum)
        y = sign(z1 + z2)

        # If output is wrong, apply minimal disturbance
        if y != t:
            # Try flipping z1
            y1 = sign(-z1 + z2)
            if y1 == t:
                # Adjust only neuron 1
                w1[0] += lr * (t - y) * x1
                w1[1] += lr * (t - y) * x2
                b1 += lr * (t - y)
            else:
                # Adjust only neuron 2
                w2[0] += lr * (t - y) * x1
                w2[1] += lr * (t - y) * x2
                b2 += lr * (t - y)

# Test MADALINE
print("Testing MADALINE AND function:")
for x in X:
    net1 = w1[0]*x[0] + w1[1]*x[1] + b1
    net2 = w2[0]*x[0] + w2[1]*x[1] + b2
    z1, z2 = sign(net1), sign(net2)
    y = sign(z1 + z2)
    print(f"{x} => {y}")