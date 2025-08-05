import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def cost_function(X, y, weights, bias):
    m = len(X)
    total_error = 0
    for i in range(m):
        prediction = weights * X[i] + bias
        mse = (prediction - y[i]) ** 2
        total_error += mse

    total_cost = (1 / (2 * m)) * total_error
    return total_cost


def calculate_gradient(X, y, weights, bias):
    m = len(X)
    dc_dw = 0
    dc_db = 0

    for i in range(m):
        dc_dw += (weights * X[i] + bias - y[i]) * X[i]
        dc_db += weights * X[i] + bias - y[i]

    dc_dw = (1 / m) * dc_dw
    dc_db = (1 / m) * dc_db
    return dc_dw, dc_db


def perform_gradient_descent(X, y, alpha, n_iterations):
    weights = 0
    bias = 0
    for i in range(n_iterations):
        dc_dw, dc_db = calculate_gradient(X, y, weights, bias)
        weights = weights - alpha * dc_dw
        bias = bias - alpha * dc_db
        print(
            f"Iteration {i+1}: Cost = {cost_function(X, y, weights, bias)}, Weights = {weights}, bias = {bias}"
        )
    return weights, bias


def plot_data(dataset: pd.DataFrame):
    X = dataset["TV"]
    y = dataset["Sales"]
    plt.scatter(X, y)
    plt.xlabel("TV")
    plt.ylabel("Sales")
    plt.show()


def plot_regression_line(X, y, weights, bias):
    X_vals = np.linspace(min(X), max(X), 100)
    y_vals = weights * X_vals + bias
    X = dataset["YearsExperience"].values
    y = dataset["Salary"].values
    plt.scatter(X, y, label="Data points")
    plt.xlabel("YearsExperience")
    plt.ylabel("Salary")
    plt.plot(X_vals, y_vals, color="red", label="Regression line")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    dataset = pd.read_csv("../datasets/Salary_Data.csv")
    X = dataset["YearsExperience"].values
    y = dataset["Salary"].values
    alpha = 0.01
    n_iterations = 10000
    weights, bias = perform_gradient_descent(X, y, alpha, n_iterations)
    print(f"Weights: {weights}, Bias: {bias}")
    plot_regression_line(X, y, weights, bias)
