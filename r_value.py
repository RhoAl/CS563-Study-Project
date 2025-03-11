# Data for bugs closed, total reviews, and review depth
bugs_closed = [278, 909, 337, 124, 75]
total_reviews = [1545, 3920, 1728, 738, 202]
# This is in data of review depth is in percentage
review_depths = [1.77, 0.99, 1.07, 0.65, 0.35]

# Calculate the necessary sums for Pearson's correlation formula
sum_x = sum(bugs_closed)
sum_y = sum(total_reviews)
sum_z = sum(review_depths)
sum_x2 = sum(x**2 for x in bugs_closed)
sum_y2 = sum(y**2 for y in total_reviews)
sum_z2 = sum(y**2 for y in review_depths)
sum_xy = sum(x * y for x, y in zip(bugs_closed, total_reviews))
sum_xy2 = sum(x * y for x, y in zip(bugs_closed, review_depths))

# Number of data points
n = len(bugs_closed)

# Calculate Pearson correlation coefficient (r)
r = (n * sum_xy - sum_x * sum_y) / ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
r2 = (n * sum_xy2 - sum_x * sum_z) / ((n * sum_x2 - sum_x ** 2) * (n * sum_z2 - sum_z ** 2)) ** 0.5

# Output the result
print("Pearson correlation coefficient (r): REVIEWER FREQUENCY - ", r)
print("Pearson correlation coefficient (r): REVIEWER DEPTH - ", r2)


