import numpy as np

def apply_velocity_perturbation(U, variation=0.1):
    """
    Apply a random ±variation perturbation to the velocity.

    Parameters
    ----------
    U : float
        Base velocity (m/s)
    variation : float
        Fractional variation (0.1 = ±10%)

    Returns
    -------
    float
        Perturbed velocity for this timestep
    """
    return U * (1 + variation * np.random.randn())
  
