import numpy as np

# Our starting variables
n_trials = 1_000_000  # number of simulations
urn = np.array(['R']*5 + ['B']*7)  # 5 red, 7 blue

# Simulate: randomly choose 2 balls without replacement
draws = np.array([np.random.choice(urn, size=2, replace=False) for _ in range(n_trials)])

# First and second draws
first = draws[:, 0]
second = draws[:, 1]

# Filter only trials where first ball is red
mask = (first == 'R')
first_red_total = np.sum(mask)

# Among these, we can count cases where second is blue
blue_condition_red = np.sum(second[mask] == 'B')

# Estimate our probability
estimate = blue_condition_red / first_red_total
exact = 7/11

print(f"Trials with first red: {first_red_total}")
print(f"Second blue among those: {blue_condition_red}")
print(f"Estimate P(second blue | first red) = {estimate:.6f}")
print(f"Exact value = 7/11 = {exact:.6f}")
print(f"Absolute error = {abs(estimate - exact):.6f}")
