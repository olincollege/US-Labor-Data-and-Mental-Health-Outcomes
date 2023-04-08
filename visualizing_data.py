"""
    Visualize data using functions from plot_functions.py
"""
import matplotlib.pyplot as plt

from plot_functions import (
    load_data,
    plot_all_data,
    plot_beyond_change_threshold_data,
    plot_mean_data,
    plot_state,
)


csv_data = load_data("data.csv")

subplot_rows, subplot_cols = 2, 2
plot_all_data(csv_data)
plt.show()
plot_beyond_change_threshold_data(csv_data, 0.65, subplot_rows, subplot_cols, 1)
plot_beyond_change_threshold_data(csv_data, 1.25, subplot_rows, subplot_cols, 2)
plot_mean_data(csv_data, subplot_rows, subplot_cols, 3)
plot_state(csv_data, "Massachusetts", subplot_rows, subplot_cols, 4)
plt.show()
