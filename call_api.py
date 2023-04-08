"""
    Includes any functions that make an API call
    MAX 200 CALLS PER DAY
"""
import json
import requests


def get_series_json(state_to_series_ids, start_year, end_year, api_key):
    """
    call BLS API with series ids and return data in specified timeframe

    inputs:
        state_to_series_ids: dict
            names of states mapped to series IDs within the same series type
            as sample_series_id
        start_year: int
            beginning year for accessed data
        end_year:   int
            end year for accessed data
        api_key: str
            api key to access BLS database

    returns:
        series_json: dict
            dictionary with nested dictionaries and lists. includes all
            data values for all timeframes and series called
    """

    # creates list of series ids only for states in state_strings_list
    active_series_list = []
    for state_string in state_to_series_ids:
        active_series_list.append(state_to_series_ids[state_string])

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

    series_json = json_data.json()
    # converts json object to dict and returns
    return series_json
