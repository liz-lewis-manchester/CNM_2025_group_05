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

# We now plut multiple simulation results on the same graph for comparison
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
