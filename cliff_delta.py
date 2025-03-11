# Data from bug closed & frequency review
bugs_closed = [278, 909, 337, 124, 75]
total_reviews = [1545, 3920, 1728, 738, 202]

# Initialize counters
count_greater = 0
count_less = 0
m = len(total_reviews)  # Size of first sample
n = len(bugs_closed)  # Size of second sample

# Compare each pair
for x in bugs_closed:
    for y in total_reviews:
        if x > y:
            count_greater += 1
        elif x < y:
            count_less += 1

# Calculate Cliff's Delta
delta = (count_greater - count_less) / (m * n)

print(f"Cliff's Delta - REVIEWER FREQUENCY: {delta}")