import numpy as np
np.random.seed(42)

# Question 8
ranks = np.repeat(np.arange(13), 4)     # 52 ranks (0..12), 4 suits each
deck_indices = np.arange(52)

def is_full_house(hand_idx):
    """hand_idx: shape (5,), indices into deck (NumPy only)."""
    hand_ranks = ranks[hand_idx]
    _, counts = np.unique(hand_ranks, return_counts=True)
    counts.sort()
    return (counts.size == 2) and (counts[0] == 2) and (counts[1] == 3)

def simulate_full_house(trials=200_000):
    hits = 0
    for _ in range(trials):
        hand = np.random.choice(deck_indices, size=5, replace=False)
        hits += is_full_house(hand)
    return hits / trials


def nCk(n, k):
    k = min(k, n - k)
    if k < 0: return 0
    if k == 0: return 1
    numer = np.arange(n - k + 1, n + 1, dtype=object)
    denom = np.arange(1, k + 1, dtype=object)
    return int(np.prod(numer, dtype=object) // np.prod(denom, dtype=object))

exact = (13 * nCk(4, 3) * 12 * nCk(4, 2)) / nCk(52, 5)

print("Exact probability:", exact)              # ~0.001440576
print("Simulated (≈):   ", simulate_full_house(200_000))


print("Exact probability:", exact)
print("Simulated (≈):   ", simulate_full_house(200_000))






# Question 8
np.random.seed(7)

# Encode friends 0..7 where 0="Alice", 1="Bob"
friends = np.arange(8)

def are_adjacent(perm):
    posA = np.where(perm == 0)[0][0]
    posB = np.where(perm == 1)[0][0]
    return abs(posA - posB) == 1

def simulate_adjacent(trials=100_000):
    hits = 0
    for _ in range(trials):
        p = np.random.permutation(friends)
        hits += are_adjacent(p)
    return hits / trials

print("Exact probability:", 0.25)               # 2*7! / 8! = 1/4
print("Simulated (≈):   ", simulate_adjacent(100_000))


