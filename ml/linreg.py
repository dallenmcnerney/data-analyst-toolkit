import numpy as np
import matplotlib.pyplot as plt


# Create scatter plot of x and y value
def plot_data(x, y, x_label=None, y_label=None):
    plt.scatter(x, y, c='red', marker='x')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# Returns result of sum of squares cost function given x, y, and theta arrays
def compute_cost(x, y, theta):
    m = len(y)
    x = np.column_stack((np.ones(m), x))
    cost = (1 / (2 * m)) * sum(np.power((np.matmul(x, theta) - y), 2))
    return cost


# Runs linear regression gradient descent over values
# May need to update alpha, theta, and iterations
def gradient_descent(x, y, theta, alpha, iterations=1000):
    m = len(y)
    j_history = np.zeros(iterations)
    x = np.column_stack((np.ones(m), x))
    for i in range(iterations):
        theta = theta - (alpha * (1/m) * np.matmul(np.transpose(x), (np.matmul(x, theta) - y)))
        j_history[i] = compute_cost(x, y, theta)
    return theta, j_history


# Normal equation for linear regression
def normal_equation(x, y):
    m = len(y)
    x = np.column_stack((np.ones(m), x))
    theta = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(x), x)), np.transpose(x)), y)
    return theta
