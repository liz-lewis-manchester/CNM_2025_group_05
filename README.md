# CNM_2025_group_05
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os


def load_initial_conditions(filepath):
    """
    Load initial condition data from a CSV file.
    
    Args:
    filepath (str): Path to the CSV file
    (e.g., "data/initial_conditions.csv")
    
    Returns:
    tuple: Two numpy arrays containing the x-coordinates and
    the corresponding pollutant concentrations.
    """

# Check if the file exists
if not os.path.exists(filepath):
    raise FileNotFoundError(f"File not found: {filepath}")

# Try reading with different encodings
encodings_to_try = [None, "latin", "gbk"]
df = None

for enc in encodings_to_try:
    try:
        if enc is None:
        df = pd.read_csv(filepath)
        else:
        df = pd.read_csv(filepath, encoding=enc)
        break
        except UnicodeDecodeError:
        continue

if df is None:
    raise RuntimeError("Failed to read CSV file with all tested encodings.")

# Extract the first two columns as numpy arrays
x_observed = df.iloc[:, 0].values
c_observed = df.iloc[:, 1].values

return x_observed, c_observed
