# Making plots as a visual representation of our tests
We plot polutant concentration at several time snapshots setting our parameters as the following- results: 2D array(time,space), x_grid: 1D array(distance), dt: timestep(s), n_plots: number of snapshots to display
# Comparing data 
We also plot multiple simulation results on the same graph for comparison setting our parameters as- results_dict: dict of {'label' : result_array}, x_grid: model spatial grid, dt: timestep(s) using only the final time step
# A second visual representation of our tests
We also produce a heatmap showing concentration over time
