# Results
In this section we will be showing the results we get from the code from a set of paramaters chosen

# Pollutant Transport Model Setup inputs for test case 1 
what is the max distance you wish to input in metres: 20

what is the resolution needed (in metres): 0.2

Enter total simulation time (seconds): 300

Enter time step (seconds): 10

Enter flow velocity U (m/s): 0.1

enter inititial conditions filename (initial_conditions.csv): initial_conditions

Model parameters successfully captured:
{'x_max': 20.0, 'dx': 0.2, 't_max': 300.0, 'dt': 10.0, 'U': 0.1, 'initial_conditions_file': 'initial_conditions'}

Spatial grid created (first 10 points):
 [0.  0.2 0.4 0.6 0.8 1.  1.2 1.4 1.6 1.8]

Initial concentrations interpolated onto the grid (first 10 values):
 [300. 242. 184. 126.  68.  10.  10.  10.  10.  10.]

Shape of simulation results (time steps, spatial points):
 (31, 101)
Number of time steps (nt) calculated:
 30

# Pollutant Transport Model Setup inputs for test case 3
What is the max distance you wish to input in metres: 50

What is the resolution needed (in metres): 0.2

Enter total simulation time (seconds): 100

Enter time step (seconds): 5

Enter flow velocity U (m/s): 0.05

enter inititial conditions filename (initial_conditions.csv): initial_conditions

Model parameters successfully captured:
{'x_max': 50.0, 'dx': 0.2, 't_max': 100.0, 'dt': 5.0, 'U': 0.05, 'initial_conditions_file': 'initial_conditions'}

Spatial grid created (first 10 points):
 [0.  0.2 0.4 0.6 0.8 1.  1.2 1.4 1.6 1.8]

Initial concentrations interpolated onto the grid (first 10 values):
 [300. 242. 184. 126.  68.  10.  10.  10.  10.  10.]

Shape of simulation results (time steps, spatial points):
 (21, 251)
Number of time steps (nt) calculated:
 20


# Pollutant Transport Model Setup inputs for test case 3
What is the max distance you wish to input in metres: 20

What is the resolution needed (in metres): 1

Enter total simulation time (seconds): 10

Enter time step (seconds): 2

Enter flow velocity U (m/s): 30

Enter inititial conditions filename (initial_conditions.csv): initial_conditions

Model parameters successfully captured:
{'x_max': 20.0, 'dx': 1.0, 't_max': 10.0, 'dt': 2.0, 'U': 30.0, 'initial_conditions_file': 'initial_conditions'}

Spatial grid created (first 10 points):
 [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

Initial concentrations interpolated onto the grid (first 10 values):
 [300.  10.  10.  10.  10.   8.   8.   8.   8.   7.]

Shape of simulation results (time steps, spatial points):
 (6, 21)
Number of time steps (nt) calculated:
 5
