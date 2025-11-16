# Implement AND function using ADALINE with bipolar inputs and outputs.

# ADALINE - Bipolar AND (Short Version)

X = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
T = [-1, -1, -1, 1]  # target outputs

w = [0.0, 0.0, 0.0]  # weights: w1, w2, bias
lr = 0.1  # learning rate

for epoch in range(100):
    total_error = 0
    for i in range(4):
        x1, x2 = X[i]
        net = w[0]*x1 + w[1]*x2 + w[2]*1
        error = T[i] - net
        w[0] += lr * error * x1
        w[1] += lr * error * x2
        w[2] += lr * error * 1
        total_error += error**2
    if total_error < 0.01:
        break

# Results
print("Weights:", [round(x, 2) for x in w])
print("Testing:")
for x in X:
    y = w[0]*x[0] + w[1]*x[1] + w[2]*1
    print(f"{x} => {1 if y >= 0 else -1}")