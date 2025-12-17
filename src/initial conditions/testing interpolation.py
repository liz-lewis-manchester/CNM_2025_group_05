# testing interpolation
from initial_conditions import interpolate_initial_conditions
import numpy as np
grid = np.arange(0,20, 0.2)
c0 = interpolate_initial_conditions("initial_conditions.csv", grid)
print(c0[:10])  # preview first few values

