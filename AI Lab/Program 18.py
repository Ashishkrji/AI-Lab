# Implement Union, Intersection, Complement and Difference operations on fuzzy sets.
# Also create fuzzy relation by Cartesian product of any two fuzzy sets and perform maxmin
# composition on any two fuzzy relations.

import numpy as np


# ---------- Fuzzy Set Operations ----------

def fuzzy_union(A, B):
    return np.maximum(A, B)


def fuzzy_intersection(A, B):
    return np.minimum(A, B)


def fuzzy_complement(A):
    return 1 - A


def fuzzy_difference(A, B):
    return np.minimum(A, 1 - B)


# ---------- Fuzzy Cartesian Product (Relation) ----------

def cartesian_product(A, B):
    # Outer product to form relation matrix
    return np.minimum.outer(A, B)


# ---------- Max-Min Composition ----------

def max_min_composition(R1, R2):
    # R1: m x n, R2: n x p
    m, n = R1.shape
    n2, p = R2.shape
    assert n == n2, "Incompatible dimensions for composition"

    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            result[i, j] = np.max(np.minimum(R1[i, :], R2[:, j]))
    return result


# ---------- Example Fuzzy Sets ----------

A = np.array([0.2, 0.5, 0.8])
B = np.array([0.7, 0.4, 0.6])

print("Set A:", A)
print("Set B:", B)

# Fuzzy Set Operations
print("\n--- Fuzzy Set Operations ---")
print("Union (A ∪ B):", fuzzy_union(A, B))
print("Intersection (A ∩ B):", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
print("Difference (A - B):", fuzzy_difference(A, B))

# Fuzzy Relations via Cartesian Product
print("\n--- Fuzzy Relations ---")
R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
print("Relation R1 (A × B):\n", R1)
print("Relation R2 (B × A):\n", R2)

# Max-Min Composition
print("\n--- Max-Min Composition (R1 o R2) ---")
R_composed = max_min_composition(R1, R2)
print("R1 o R2:\n", R_composed)