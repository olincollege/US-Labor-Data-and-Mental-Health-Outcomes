"""
    Methods for any conversions between data types.
    Conversions include simplifiying data to make it more readable.
"""
import pandas as pd


def dict_to_df(state_to_series_ids, series_json, start_year, end_year):
    """
    creates a df object from series_dict with each state as a column of values

    inputs:
        state_to_series_ids: dict
            dict object which contains series values for all timeframes
        series_json: dict
            all data from json api call for all series in state_to_series_ids
        start_year: int
            beginning year
        end_year:   int
            end year

    returns:
        state_yearly_df: pandas dataframe
            dataframe where years are columns and state names are rows.
            years are in left to right descending order
    """

    # swap keys and values in series_to_state
    series_to_state = {state: series for series, state in state_to_series_ids.items()}

    # create dict with all in range years mapping to empty dict
    year_data_dict = {}
    for year in range(end_year, start_year - 1, -1):
        year_data_dict[str(year)] = {}

    # for each set of state data, add data to respective year in year_data_dict
    for state_data in series_json["Results"]["series"]:
        state_name = series_to_state[state_data["seriesID"]]
        for item in state_data["data"]:
            year_data_dict[str(item["year"])][state_name] = item["value"]

    # convert dict to df
    state_yearly_df = pd.DataFrame(year_data_dict)
    return state_yearly_df


def df_to_csv(state_yearly_df, csv_name):
    """
    creates a csv from a dataframe

    inputs:
        state_yearly_df: pandas dataframe
            dataframe where years are columns and state names are rows.
            years are in left to right descending order
        csv_name: str
            name of csv file to be created. Summarize series type

    returns:
        none (creates a csv file)
    """
    with open(csv_name + ".csv", "wb") as csv_file:
        state_yearly_df.to_csv(csv_file)
