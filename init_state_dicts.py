"""
    Initialize any state dictionaries where keys depend on state names/ids
"""
from csv import reader as csv_reader
import requests


def make_state_dict(state_dict_url):
    """
    creates a dictionary from a url with state id info

    inputs:
        state_dict_url: str
            url that leads to a list of states and their 2 digit codes

    returns:
        state_dict: dict
            dictionary that maps states to their 2 digit numbers
    """

    # string w states separated from their ids with \t, each separated with \n
    states_string = (requests.get(state_dict_url)).content.decode()

    # dict mapping "state name": 3 character state ID
    state_id_dict = {}
    for string in states_string.split("\r\n")[1:-1]:
        if string[0] == "S":  # state data identifying character
            state_id_dict[string.split("\t")[1]] = string.split("\t")[0]
    # dict with state names mapping to state ids
    return state_id_dict


def create_all_state_ids(state_dict, sample_series_id, state_location_in_series_id):
    """
    creates a dictionary that maps state names to series IDs

    inputs:
        state_dict: dict
            maps str state names to their 2 digit numbers
        sample_series_id: str
            series identifier which later access the API to particular dataset

    returns:
        series_ids_dict: dict
            names of states mapped to series IDs within the same series type
            as sample_series_id
    """

    # creates list of state names from states.csv file
    with open("states.csv", "r", encoding="UTF-8") as states_file:
        state_strings_list = list(csv_reader(states_file, delimiter=","))[0]

    # creates dict with state names mappig to series id with proper state id
    series_ids_dict = {}
    for key in state_dict:
        if key in state_strings_list:
            this_state_series = sample_series_id[0:state_location_in_series_id] + (
                str(state_dict[key])
            )
            series_ids_dict[key] = this_state_series
    return series_ids_dict
