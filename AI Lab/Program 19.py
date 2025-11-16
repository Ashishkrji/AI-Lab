# Maximize the function f(x)=x2 using GA, where x ranges form 0-25. Perform 6 iterations.

import numpy as np
import random

# Parameters
population_size = 6
chromosome_length = 5  # 5 bits to represent numbers from 0 to 31
crossover_rate = 0.7
mutation_rate = 0.1
generations = 6

# Fitness function
def fitness(x):
    return x ** 2

# Decode binary string to integer
def decode(chromosome):
    return int("".join(str(bit) for bit in chromosome), 2)

# Generate initial population
def generate_population():
    return [np.random.randint(0, 2, chromosome_length).tolist() for _ in range(population_size)]

# Selection: roulette wheel
def roulette_wheel_selection(pop, fitnesses):
    total_fit = sum(fitnesses)
    probs = [f / total_fit for f in fitnesses]
    selected_indices = np.random.choice(range(population_size), size=2, p=probs)
    return [pop[i] for i in selected_indices]

# Crossover: one-point
def crossover(p1, p2):
    if random.random() < crossover_rate:
        point = random.randint(1, chromosome_length - 1)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    return p1, p2

# Mutation: flip a bit
def mutate(chromosome):
    return [
        bit if random.random() > mutation_rate else 1 - bit
        for bit in chromosome
    ]

# Run GA
population = generate_population()

print("\nInitial Population:")
for chrom in population:
    x = decode(chrom)
    print(f"{chrom} => x={x}, f(x)={fitness(x)}")

for gen in range(generations):
    print(f"\n--- Generation {gen + 1} ---")
    new_population = []

    # Evaluate fitness
    fitnesses = [fitness(decode(chrom)) for chrom in population]

    # Create next generation
    while len(new_population) < population_size:
        # Selection
        parent1, parent2 = roulette_wheel_selection(population, fitnesses)

        # Crossover
        child1, child2 = crossover(parent1, parent2)

        # Mutation
        child1 = mutate(child1)
        child2 = mutate(child2)

        new_population.append(child1)
        if len(new_population) < population_size:
            new_population.append(child2)

    # Update population
    population = new_population

    # Display current generation
    for chrom in population:
        x = decode(chrom)
        print(f"{chrom} => x={x}, f(x)={fitness(x)}")

# Find best solution
best = max(population, key=lambda c: fitness(decode(c)))
best_x = decode(best)
print(f"\n✅ Best solution after {generations} generations:")
print(f"Chromosome: {best}, x = {best_x}, f(x) = {fitness(best_x)}")