"""
    Includes any functions that make an API call
    MAX 200 CALLS PER DAY
"""
import json
import requests


def get_series_json(series_ids_dict, start_year, end_year, api_key):
    """
    call BLS API with series ids and return data in specified timeframe

    inputs:
        series_ids_dict: dict
            names of states mapped to series IDs within the same series type
            as sample_series_id
        start_year: int
            beginning year
        end_year:   int
            end year
        api_key: str
            api key to access BLS database

    returns:
        series_dict: dict
            dictionary with nested dictionaries and lists. includes all
            data values for all timeframes and series called
    """

    # # creates list of state names from states.csv file
    # with open("states.csv", "r") as states_file:
    #     state_strings_list = list(csv_reader(states_file, delimiter=","))[0]

    # creates list of series ids only for states in state_strings_list
    active_series_list = []
    for state_string in series_ids_dict:
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

    # API CALL: MAX 200 PER DAY
    json_data = requests.post(
        "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
    )

    # converts json object to dict and returns
    return json_data.json()
