import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os


def load_initial_conditions(filepath):

    #Parameters
    filepath:str
        Path to the CSV file (e.g., 'data/initial_conditions.csv').

    #Returns
    tuple of np.ndarray
        A tuple containing:
        - x_observed (np.ndarray): Observed x-coordinates.
        - c_observed (np.ndarray): Observed pollutant concentrations.

    #Raises
    FileNotFoundError
        If the file does not exist.
    RuntimeError
        If an error occurs during file reading or data extraction.

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Cannot find file: {filepath}")

    try:
        # Try reading the CSV using different encodings
        try:
            df = pd.read_csv(filepath)
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(filepath, encoding='latin1')
            except UnicodeDecodeError:
                df = pd.read_csv(filepath, encoding='gbk')

        # Extract the first two columns: x and concentration
        x_observed = df.iloc[:, 0].values
        c_observed = df.iloc[:, 1].values

        return x_observed, c_observed

    except Exception as e:
        raise RuntimeError(f"Error when loading initial conditions: {str(e)}")


def interpolate_initial_conditions(filepath, model_grid_x):
    #Load the initial conditions file and interpolate concentrations
    onto a given model grid.

    #Parameters
    filepath : str
        Path to the CSV file containing initial concentration data.
    model_grid_x : np.ndarray
        The x-coordinates of the model grid.

    #Returns
    tuple
        - model_grid_x (np.ndarray): The model grid (returned unchanged).
        - interpolated_concentration (np.ndarray): Interpolated concentrations.
    # Load observed data
    x_observed, c_observed = load_initial_conditions(filepath)

    # Linear interpolation (as required in coursework)
    interpolation_func = interp1d(
        x_observed,
        c_observed,
        kind='linear',
        bounds_error=False,
        fill_value=0  # Outside the observed range, assign 0
    )

    # Evaluate on the model grid
    interpolated_concentration = interpolation_func(model_grid_x)

    return model_grid_x, interpolated_concentration
