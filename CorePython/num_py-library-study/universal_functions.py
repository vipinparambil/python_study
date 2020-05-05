# maths ans statistics
import numpy as np

angles = np.array([0, 30, 45, 60, 90])

# convert to radians
angles_radians = np.radians(angles)

print(f"convert to radians : {angles_radians}")

# sin
sin_values = np.sin(angles_radians)
print(f"sin values : {sin_values}")

# cos
cos_valus = np.cos(angles_radians)
print(f"Cos value : {cos_valus}")

# convert radians
radians_ = np.arcsin(sin_values)
print(f"radians from sin values : {radians_}")

angles_dgree = np.degrees(radians_)
print(f"angles in degrees from radians : {angles_dgree}")

# statistics

ages = np.array([23, 24, 28, 29, 30, 23, 25])
print(f"mean : {np.mean(ages)}")
print(f"median : {np.median(ages)}")

# read from file
salaries = np.genfromtxt('data/salary.csv', delimiter=",")
print(salaries.shape)

mean = np.mean(salaries)
median = np.median(salaries)
varience = np.var(salaries)
sd = np.std(salaries)

print(f"Mean : {mean:.3f}")
print(f"Median : {median: 0.3f}")
print(f"standard deviation : {sd: 0.3f}")
print(f"Variance : {varience: 0.3f}")