directions = ["Arrow / U Turn Right", "Arrow / Sharp Right", "Arrow / Right", "Arrow / Slight Right", "Arrow / Straight", "Arrow / Slight Left", "Arrow / Left", "Arrow / Sharp Left", "Arrow / U Turn Left"]

numberOfDirectionsUsed = 2

# The number of combinations of n distinct objects, taken r at a time is:
# nCr = n! / r! (n - r)!

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

combinationsResulting = list(combinations(directions, numberOfDirectionsUsed))

print(combinationsResulting)