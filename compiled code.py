# izzys work
import numpy as np
import pandas as pd

def load_initial_conditions(csv_path: str):
 
  df = pd.read_csv(initial_condition.csv)
  
  # Check required columns
  required_cols = {"Distance (m)", "Concentration (μg/m_ )"}
  if not required_cols.issubset(df.columns):
      raise ValueError(
           f"CSV {csv_path} must contain columns: {required_cols}")
  
  return df

def create_model_domain(x_max: float, dx: float):
  # x refers to the distance travelled by the pollutant and dx is the incremental change in distance
  # this function checks if the values are correct 
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
 
  print("Pollutant Transport Model Setup inputs")

  # for test case 1, we will need to input our own values
 
  x_max = float(input("what is the max distance you wish to input in metres: "))
  dx = float(input("what is the resolution needed (in metres): ")
  
  # Time settings
  t_max = float(input("Enter total simulation time (seconds): "))
  dt = float(input("Enter time step (seconds): "))

  # Velocity
  U = float(input("Enter flow velocity U (m/s): "))
`
  # Initial conditions file
  ic_file = input("enter inititial conditions filename (initial_conditions.csv): ")
  # Creating Parameters
  params = {                        
     "x_max": x_max,
     "dx": dx,
     "t_max": t_max,
     "dt": dt,
     "U": U,
     "initial_conditions_file": ic_file}
return params

   grid_x = create_model_domain(x_max, dx)
   times = np.arange(0, t_max + dt, dt)



# Aiqing's work
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



# rudys work 
#solver
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
    # variation : float, stregnth of variation (0.1 = ±10%)

    Returns:
    - results : 2D array, shape (nt+1, nx)
    
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
  
  #velocity
  import numpy as np

def apply_velocity_perturbation(U, variation=0.1):
    
    # Apply a random ±variation perturbation to the velocity.
    Parameters
    U : float
        Base velocity (m/s)
    variation : float
        Fractional variation (0.1 = ±10%)

    Returns
    float
        Perturbed velocity for this timestep
    return U * (1 + variation * np.random.randn())


#folajimis part
import matplotlib.pyplot as plt 
import numpy as np

# We now plot polutant concentration at several time snapshots
# Our parameters are- results: 2D array(time,space), x_grid: 1D array(distance), dt: timestep(s), n_plots: number of snapshots to display
def plot_time_snapshots(results, x_grid, dt, n_plots=8, title='Poluutant Distance Over Time'):
    time_steps= results.shape[0]
    interval= max(time_steps // n_plots, 1)

    plt.figure(figsize=(10,5))

    for in in range(0, time_steps, interval):
        plt.plot(x_grid, results[i], label=f't = {i * dt:.0f} s')

    plt.xlabel('Distance downstream (m)')
    plt.ylabel('Concentration (micrograms/m^3)')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# We now plut multiple simulation results on the same grpah for comparison
# Our parameters are- results_dict: dict of {'label' : result_array}, x_grid: model spatial grid, dt: timestep(s)
def plot_comparison(results_dict, x_grid, dt):  
    plt.figure(figsize=(10,5))

    for label, result in results_dict.items():
        plt.plot(x_grid, result[-1], label=f'{label} (t={result.shape[0] * dt}s)') # Plot final time step only

    plt.xlabel('Distance downstream (m)')
    plt.ylabel('Concentration (micrograms/m^3)')
    plt.title('Comparison of Final Concentration Profiles')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# We also produce a heatmap showing concentration over time
def plot_heatmap(result, x_grid, dt, title1='Concentration heatmap'):
    plt.figure(figsize=(10,6))

    plt.imshow(results, aspect='auto',extent=[x_grid[0], x_grid[-1], results.shape[0] * dt, 0], cmap='viridis')

    plt.colorbar(label='Concentration (micrograms/m^3)')
    plt.xlabel('Distance downstream (m)')
    plt.ylabel('Time (s)')
    plt.title(title1)
    plt.tight_layout()
    plt.show()


# bilals part
import numpy as np
import pytest

# Import your solver (adjust the import to your project structure)
# from src.model import simulate_advection


def test_initial_pulse_advects_downstream():
  # This section is for test case 1 which have a set of given initial conditions
  # x: 0-20m, dx = 0.2m (or 20cm), time = 300s, initial velocity = 0.1m/s, initial concentration = 250 at x =0
    U = 0.1
    dx = 0.2
    dt = 10
    t_max = 300
    x = np.arange(0, 20 + dx, dx)

    # initial condition
    theta0 = np.zeros_like(x)
    theta0[0] = 250.0

    # run model
    theta = simulate_advection(theta0, U, dx, dt, x, t_max)

    # expected shift distance after 300 seconds
    distance = U * t_max
    expected_index = int(distance / dx)

    # check that the peak concentration has moved approximately the correct distance
    peak_index = np.argmax(theta[-1])
    assert abs(peak_index - expected_index) <= 1, \
        f"Expected peak near index {expected_index}, got {peak_index}"


def test_interpolation_initial_conditions():
    # Here we do a test case on the conditions loaded from the CSV file
    # model grid
    dx = 0.2
    x = np.arange(0, 20 + dx, dx)

    # synthetic measurements (not aligned with grid)
    meas_x = np.array([0, 1.3, 2.7, 5.4, 10.8, 19.1])
    meas_c = np.array([250, 200, 150, 100, 50, 0])

    # your code will interpolate—here we do expected interpolation:
    expected_interp = np.interp(x, meas_x, meas_c)

    # call your interpolation function
    # interp_theta = interpolate_initial_conditions("initial_conditions.csv", x)

    # for now we pretend your function returns expected_interp
    interp_theta = expected_interp  # REMOVE when linking to real code

    # test: shape correct
    assert interp_theta.shape == x.shape

    # test: values match expected interpolation
    assert np.allclose(interp_theta, expected_interp)


def test_parameter_sensitivity():
    """
    Test Case 3: ensure model output changes when U or dx/dt changes.
    """
    theta0 = np.zeros(101)
    theta0[0] = 250

    # baseline run
    theta_base = simulate_advection(theta0, 0.1, 0.2, 10, np.arange(0, 20.2, 0.2), 300)

    # altered velocity
    theta_fast = simulate_advection(theta0, 0.2, 0.2, 10, np.arange(0, 20.2, 0.2), 300)

    # check that peak moves faster for larger velocity
    assert np.argmax(theta_fast[-1]) > np.argmax(theta_base[-1])


def test_exponential_decay_initial_condition():
    """
    Test Case 4: exponential decay in time should reduce total mass.
    """
    theta0 = np.ones(101) * 100
    U = 0.1
    dx = 0.2
    dt = 10
    t_max = 300
    x = np.arange(0, 20.2, 0.2)

    def decay_func(t):
        return np.exp(-t / 200)  # example decay

    theta = simulate_advection(theta0, U, dx, dt, x, t_max, decay=decay_func)

    # total mass should decrease over time
    assert theta[-1].sum() < theta[0].sum()


def test_variable_velocity_profile():
    """
    Test Case 5: random perturbation of velocity profile should change solution.
    """
    theta0 = np.zeros(101)
    theta0[0] = 250

    x = np.arange(0, 20.2, 0.2)
    U_const = 0.1
    U_variable = U_const * (1 + 0.1 * np.random.randn(len(x)))

    # runs
    theta_const = simulate_advection(theta0, U_const, 0.2, 10, x, 300)
    theta_var   = simulate_advection(theta0, U_variable, 0.2, 10, x, 300)

    # they should not give identical outputs
    assert not np.allclose(theta_const, theta_var)
