# Modelling Pollutant Transport in a River

# Project Summary

This project focuses on building a simple numerical model to simulate how a pollutant moves along a river over time. The aim is to apply what we’ve learned in programming, numerical methods, and data handling to a realistic engineering-style problem

# What the Code Does

The code models pollutant transport in a one-dimensional river using the **advection equation**. It calculates how pollutant concentration changes with time and distance downstream based on a given flow velocity.

The model:
- Uses the **finite difference method** to solve the advection equation
- Simulates pollutant concentration over a user-defined space and time domain
- Automatically generates plots to visualise how the pollutant moves through the river


# Main Features

- User-defined:
  - River length
  - Spatial resolution
  - Time step and total simulation time
  - Flow velocity
- Initial conditions can be:
  - Set manually
  - Read from a CSV file and interpolated onto the model grid
- Boundary conditions are handled at the upstream and downstream edges
- Results are plotted to help analyse model behaviour

---

# Test Cases Implemented

The project includes several test cases to check that the model behaves as expected:

1. **Basic transport test**  
   - 20 m river length  
   - 0.2 m spatial resolution  
   - 5-minute simulation with 10 s time steps  
   - Constant velocity of 0.1 m/s  
   - Initial concentration of 250 µg/m³ at the source

2. **CSV-based initial conditions**  
   - Reads real measurement data from `initial_conditions.csv`
   - Interpolates values onto the model grid

3. **Sensitivity analysis**  
   - Tests how results change when velocity, spatial resolution, and time step are varied

4. **Extended scenarios**  
   - Exponentially decaying pollutant input  
   - Variable velocity profile with random perturbations
