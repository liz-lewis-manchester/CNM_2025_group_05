# Initial Condition Interpolation Module

This repository contains a clean and modular implementation for:

1. Loading initial condition data from a CSV file
2. Performing linear interpolation onto a model grid
3. Testing and validating the interpolation results

# Features

- Linear interpolation using scipy.interpolate.interp1d
- Handling of out-of-range values (fill_value)
- Function separating data loading and interpolation
