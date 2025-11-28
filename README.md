# CNM_2025_group_05

import numpy as np
import pandas as pd

def load_initial_conditions(csv_path: str) -> pd.DataFrame:
 
  df = pd.read_csv(csv_path)

  # Check required columns
  required_cols = {"distance", "concentration"}
  if not required_cols.issubset(df.columns):
      raise ValueError(
           f"CSV {csv_path} must contain columns: {required_cols}")

  return df

def create_model_domain(x_max: float, dx: float) -> np.ndarray:
  if x_max <= 0:
      raise ValueError("x_max must be positive.")
  if dx <= 0:
      raise ValueError("dx must be positive.")
  if dx > x_max:
      raise ValueError("dx must be smaller than x_max.")

  # Create grid from 0 to x_max inclusive
  grid = np.arange(0, x_max + dx, dx)

  return grid
def get_user_inputs():

  print("Pollutant Transport Model Setup")

  # Domain settings
  x_max = float(input("Enter model domain length (x_max in meters): "))
  dx = float(input("Enter spatial resolution (dx in meters): "))

  # Time settings
  t_max = float(input("Enter total simulation time (seconds): "))
  dt = float(input("Enter time step (seconds): "))

  # Velocity
  U = float(input("Enter flow velocity U (m/s): "))

  # Initial conditions file
  ic_file = input("Enter initial conditions filename (e.g. data/initial_conditions.csv): ")
    # Creating Parameters
   params = {                        
      "x_max": x_max,
      "dx": dx,
      "t_max": t_max,
      "dt": dt,
      "U": U,
      "initial_conditions_file": ic_file}

  return params

def main():
params = get_user_inputs()      # Extract parameters
    x_max = params["x_max"]
    dx = params["dx"]
    t_max = params["t_max"]
    dt = params["dt"]
    U = params["U"]
    ic_file = params["initial_conditions_file"]
    # Create grids
    grid_x = create_model_domain(x_max, dx)
    times = np.arange(0, t_max + dt, dt)
