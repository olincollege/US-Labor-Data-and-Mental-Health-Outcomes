"""
    All functions which plot data including loading data
"""
from statistics import mean
import matplotlib.pyplot as plt
import pandas as pd


def load_data(data_file):
    """
    Loads data as df from data_file

    Args:
        data_file: string of file name/path

    Returns:
        dataframe from csv
    """
    data = pd.read_csv(data_file)
    data.columns.values[0] = "State"

    return data


def plot_all_data(data):
    """
    Plots all data

    Args:
        data: dataframe with data to plot
    """
    years = [int(year) for year in data if year != "State"]

    for i in range(len(data)):
        single_state_data = [int(value) for value in data.iloc[i][1:]]
        plt.plot(years, single_state_data, label=data.iloc[i][0])

    plt.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.05),
        fancybox=True,
        shadow=True,
        ncol=5,
    )

    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Fatalities Per Year in Each State")


def plot_beyond_change_threshold_data(data, change_ratio, plot_row, plot_col, plot_num):
    """
    Args:
        data: dataframe with data to plot
        change_ratio: float which is the floor or ceiling for comparison
        plot_row: int num rows in subplot
        plot_col: int num cols in subplot
        plot_num: int which plot

    """
    plt.subplot(plot_row, plot_col, plot_num)

    years = [int(year) for year in data if year != "State"]

    for i in range(len(data)):
        single_state_data = [int(value) for value in data.iloc[i][1:]]
        if change_ratio > 1:
            comparison = "Increased"
            if single_state_data[0] / single_state_data[-1] > change_ratio:
                plt.plot(years, single_state_data, label=data.iloc[i][0])
        if change_ratio < 1:
            comparison = "Decreased"
            if single_state_data[0] / single_state_data[1] < change_ratio:
                plt.plot(years, single_state_data, label=data.iloc[i][0])

    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title(
        f"Deaths in States which {comparison} Fatalities by a factor of {change_ratio}"
    )


def plot_mean_data(data, plot_row, plot_col, plot_num):
    """
    Plot mean data for all states in each year

    Args:
        data: dataframe with data to plot
        plot_row: int num rows in subplot
        plot_col: int num cols in subplot
        plot_num: int which plot
    """
    plt.subplot(plot_row, plot_col, plot_num)

    years = [int(year) for year in data if year != "State"]

    mean_data = [mean(data[str(year)]) for year in years]

    plt.plot(years, mean_data)
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Average Fatalities Per Year Across States")


def plot_state(data, state_name, plot_row, plot_col, plot_num):
    """
    Plots data for a single state

    Args:
        data: dataframe with data to plot
        state_name: string with state name
        plot_row: int num rows in subplot
        plot_col: int num cols in subplot
        plot_num: int which plot
    """
    plt.subplot(plot_row, plot_col, plot_num)

    years = [int(year) for year in data if year != "State"]

    for row in data.iterrows():
        if row[1][0] == state_name:
            state_data = row[1][1:]
            break

    plt.plot(years, state_data)
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Fatalities Per Year in " + state_name)
