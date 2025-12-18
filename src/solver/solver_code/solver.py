import numpy as np
import pandas as pd
from .velocity import apply_velocity_perturbation

def step_forward(theta, U, dx, dt):
    # One time step using an upwind scheme for the 1D advection equation.
    # θ_{i}^{n+1} = θ_{i}^n - c (θ_{i}^n - θ_{i-1}^n)
    # where c = U dt / dx
    theta_new = theta.copy()
    c = U * dt / dx
    # Updating all grid points except the first one. 
    theta_new[1:] = theta[1:] - c * (theta[1:] - theta[:-1])
    return theta_new


def run_model(theta0, U, dx, dt, nt, use_random_velocity=False, variation=0.1):
    # Run the pollutant transport model.

    # Parameters:
    # theta0 : array, initial concentration values
    # U : float, base river velocity
    # dx : float, spatial step
    # dt : float, time step
    # nt : int, number of time steps
    # use_random_velocity : bool, enable velocity perturbation
    # variation : float, stregnth of variation (0.1 = +/-10%)

    # Returns:- results : 2D array, shape (nt+1, nx)
    
    theta = theta0.copy()
    results = [theta.copy()]

    for _ in range(nt):

        # Velocity updates each timestep if perturbation is enabled
        if use_random_velocity:
            U_t = apply_velocity_perturbation(U, variation)
        else:
            U_t = U

        # Take one time step forward
        theta = step_forward(theta, U_t, dx, dt)
        results.append(theta.copy())

    return np.array(results)
