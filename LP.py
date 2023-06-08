from pulp import *

# Create the linear programming problem
prob = LpProblem("ExampleProblem", LpMaximize)

# Define the decision variables
x = LpVariable("x", lowBound=0)  # Variable x >= 0
y = LpVariable("y", lowBound=0)  # Variable y >= 0

# Set the objective function
prob += 3 * x + 5 * y  # Objective function: maximize 3x + 5y

# Add the constraints
prob += 2 * x + y <= 10  # Constraint: 2x + y <= 10
prob += x + 3 * y <= 12  # Constraint: x + 3y <= 12

# Solve the linear programming problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Print the optimal values of the decision variables
print("Optimal Solution:")
for variable in prob.variables():
    print(variable.name, "=", variable.varValue)

# Print the optimal objective value
print("Optimal Objective Value:")
print("Objective =", value(prob.objective))
