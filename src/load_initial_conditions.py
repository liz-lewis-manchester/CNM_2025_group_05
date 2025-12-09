import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os

def load_initial_conditions(filepath):
    """
    Load initial condition data from a CSV file.

    Returns:
        x_observed: numpy array of x locations
        c_observed: numpy array of concentrations
    """

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # reading with different encodings
    encodings = [None, "latin", "gbk"]
    df = None

    for enc in encodings:
        try:
            df = pd.read_csv(filepath) if enc is None else pd.read_csv(filepath, encoding=enc)
            break
        except UnicodeDecodeError:
            continue

    if df is None:
        raise RuntimeError("Unable to read CSV file with tested encodings.")

    x_observed = df.iloc[:, 0].values
    c_observed = df.iloc[:, 1].values

    return x_observed, c_observed
