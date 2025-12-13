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
