import requests
from csv import DictReader
from keys import BLS_key
import json
import pandas as pd

# This file is to store all series ID segments and their meanings in
# dictionaries to make the data acquisition more understandable
def make_state_dict(state_dict_url):
    """
    creates a dictionary from a url

    inputs:
        state_dict_url: str
            url that leads to a list of states and their 2 digit codes

    returns:
        state_dict: dict
            dictionary that maps states to their 2 digit numbers
    """
    states_string = ((requests.get(state_dict_url)).content).decode()
    state_id_list = [string.strip("\r") for string in (states_string.split("\n")[1:])]
    state_id_dict = {}
    for item in state_id_list:
        if item.count("\t") == 1:
            state_id_dict[item.split("\t")[1]] = item.split("\t")[0]
    return state_id_dict


state_dict = make_state_dict("https://download.bls.gov/pub/time.series/sm/sm.state")


def create_all_state_ids(state_idx_dict, sample_series_id):
    """
    creates a dictionary that maps state names to series IDs

    inputs:
        state_dict: dict
            maps str state names to their 2 digit numbers
        sample_series_id: str
            series identifier which will later access the API to a particular dataset

    returns:
        series_ids_dict: dict
            names of states mapped to series IDs within the same series type
            as sample_series_id
    """
    for idx, character in enumerate(sample_series_id):
        if character.isdigit():
            state_int_index = int(idx)
            break
    series_ids_dict = {}
    for key in state_dict:
        this_state_series = (
            sample_series_id[0:state_int_index]
            + str(state_idx_dict[key])
            + sample_series_id[state_int_index + 2 :]
        )
        series_ids_dict[key] = this_state_series
    return series_ids_dict


series_ids_dict = create_all_state_ids(state_dict, "SMU19197802023800001")


def get_series_json(series_ids_dict, start_year, end_year, api_key):
    """
    call BLS API with series ids and return data in specified timeframe

    inputs:
        series_ids_dict: dict
            names of states mapped to series IDs within the same series type
            as sample_series_id
        timeframe: lst
            2 item list: beginning year, end year
        api_key: str
            api key to access BLS database

    returns:
        series_json: dict
            dictionary with nested dictionaries and lists. includes all
            data values for all timeframes and series called
    """

    active_series_list = []
    state_strings_list = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    ]

    for state_string in state_strings_list:
        active_series_list.append(series_ids_dict[state_string])

    headers = {"Content-type": "application/json"}
    data = json.dumps(
        {
            "seriesid": active_series_list,
            "startyear": str(start_year),
            "endyear": str(end_year),
            "registrationkey": api_key,
        }
    )
    p = requests.post(
        "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
    )
    json_data = json.loads(p.text)
    print(json_data)


# get_series_json(series_ids_dict, [2000, 2010], BLS_key)


def json_to_df(series_json):
    """
    creates a df object from series_json with each state as a column of values

    inputs:
        series_json: dict
            json object which contains series values for all timeframes

    returns:
        series_df: pandas dataframe
            accessible table which contains data from all states in all times
    """


def df_to_csv(series_df):
    """
    creates a csv from a dataframe

    inputs:
        series_df: pandas dataframe
            accessible table which contains data from all states in all times

    returns:
        none (creates a csv file)
    """
