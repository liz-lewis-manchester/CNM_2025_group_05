import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# Load initial condition data from a CSV file.
def load_initial_conditions(csv_paths):
    df = pd.read_csv(csv_paths)
    # Ensure correct column names
    required_cols = ["Distance (m)", "Concentartion (µg/m_ )"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"CSV must contain columns: {required_cols}")
    return df["Distance (m)"].values, df["Concentraion (µg/m_ )"].values

# Now we interpolate concentration values onto the model grid
def interpolate_initial_conditions(csv_paths, grid):
    # Load raw CSV data 
    raw_Dist, raw_Conc = load_initial_conditions(csv_paths)
    # Create linear interpolation function
    interpolator = interpld(raw_Dist, raw_Conc, kind="linear", fill_value="extrapolate")    # the last bit of code allows values outside the CSV range
    # Now we evaluate on model grid
    interpolated = interpolator(grid)
    return interpolated 
