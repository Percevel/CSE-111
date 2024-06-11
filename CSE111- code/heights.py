import statistics


heights = [
    1.72, 1.50, 1.96, 2.01, 1.75,
    2.11, 1.60, 1.65, 2.05, 1.50,
    1.80, 1.83, 2.05, 1.79, 1.84
]

print(f"len: {len(heights)}")
print(f"min: {min(heights)}")
print(f"max: {max(heights)}")
print(f"sum: {sum(heights):.2f}")
print(f"mean: {statistics.mean(heights):.2f}")
print(f"median: {statistics.median(heights)}")
print(f"mode: {statistics.mode(heights)}")