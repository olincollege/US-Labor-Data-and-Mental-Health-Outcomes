"""
    Methods for any conversions between data types.
    Conversions include simplifiying data to make it more readable.
"""
import pandas as pd


def dict_to_df(series_ids_dict, series_data_dict, start_year, end_year):
    """
    creates a df object from series_dict with each state as a column of values

    inputs:
        series_ids_dict: dict
            dict object which contains series values for all timeframes
        series_data_dict: dict
            all data from json api call
        start_year: int
            beginning year
        end_year:   int
            end year

    returns:
        series_df: pandas dataframe
            accessible table which contains data from all states in all times
    """

    # swap keys and values in series_to_state
    series_to_state = {state: series for series, state in series_ids_dict.items()}

    # create dict with all in range years mapping to empty dict
    year_data_dict = {}
    for year in range(end_year, start_year - 1, -1):
        year_data_dict[str(year)] = {}

    # for each set of state data, add data to respective year in year_data_dict
    for state_data in series_data_dict["Results"]["series"]:
        state_name = series_to_state[state_data["seriesID"]]
        for item in state_data["data"]:
            year_data_dict[str(item["year"])][state_name] = item["value"]

    # convert dict to df
    state_yearly_df = pd.DataFrame(year_data_dict)
    return state_yearly_df


def df_to_csv(series_df):
    """
    creates a csv from a dataframe

    inputs:
        series_df: pandas dataframe
            accessible table which contains data from all states in all times

    returns:
        none (creates a csv file)
    """
    with open("test_data.csv", "wb") as csv_file:
        series_df.to_csv(csv_file)
