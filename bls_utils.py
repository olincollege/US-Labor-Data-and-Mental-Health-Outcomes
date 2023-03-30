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
    states_translation = requests.get(state_dict_url)
    bytes_string = states_translation.content
    raw_string = bytes_string.decode()
    state_idx_list = [string.strip("\r") for string in (raw_string.split("\n")[1:])]
    state_dict = {}
    for item in state_idx_list:
        separated = item.split("\t")
        if len(separated) == 2:
            state_dict[separated[1]] = separated[0]
    return state_dict


state_dict = make_state_dict("https://download.bls.gov/pub/time.series/sm/sm.state")


def make_all_state_ids(state_dict, sample_series_id):
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
            where_is_state_int = int(idx)
            break
    series_ids_dict = {}
    for key in state_dict:
        this_state_series = (
            sample_series_id[0:where_is_state_int]
            + str(state_dict[key])
            + sample_series_id[where_is_state_int + 2 :]
        )
        series_ids_dict[key] = this_state_series
    return series_ids_dict


series_ids_dict = make_all_state_ids(state_dict, "SMU19197802023800001")


def get_series_json(series_ids_dict, timeframe, api_key):
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
    begin_yr = str(timeframe[0])
    end_yr = str(timeframe[1])
    for state_string in state_strings_list:
        active_series_list.append(series_ids_dict[state_string])
    
    headers = {"Content-type": "application/json"}
    data = json.dumps(
        {
            "seriesid": active_series_list,
            "startyear": begin_yr,
            "endyear": end_yr,
            "registrationkey": api_key,
        }
    )
    p = requests.post(
        "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
    )
    json_data = json.loads(p.text)
    print(json_data)


get_series_json(series_ids_dict, [2000, 2010], BLS_key)


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


"state_code\tstate_name\r\n00\tAll States\r\n01\tAlabama\r\n02\tAlaska\r\n04\tArizona\r\n05\tArkansas\r\n06\tCalifornia\r\n08\tColorado\r\n09\tConnecticut\r\n10\tDelaware\r\n11\tDistrict of Columbia\r\n12\tFlorida\r\n13\tGeorgia\r\n15\tHawaii\r\n16\tIdaho\r\n17\tIllinois\r\n18\tIndiana\r\n19\tIowa\r\n20\tKansas\r\n21\tKentucky\r\n22\tLouisiana\r\n23\tMaine\r\n24\tMaryland\r\n25\tMassachusetts\r\n26\tMichigan\r\n27\tMinnesota\r\n28\tMississippi\r\n29\tMissouri\r\n30\tMontana\r\n31\tNebraska\r\n32\tNevada\r\n33\tNew Hampshire\r\n34\tNew Jersey\r\n35\tNew Mexico\r\n36\tNew York\r\n37\tNorth Carolina\r\n38\tNorth Dakota\r\n39\tOhio\r\n40\tOklahoma\r\n41\tOregon\r\n42\tPennsylvania\r\n44\tRhode Island\r\n45\tSouth Carolina\r\n46\tSouth Dakota\r\n47\tTennessee\r\n48\tTexas\r\n49\tUtah\r\n50\tVermont\r\n51\tVirginia\r\n53\tWashington\r\n54\tWest Virginia\r\n55\tWisconsin\r\n56\tWyoming\r\n72\tPuerto Rico\r\n78\tVirgin Islands\r\n99\tAll Metropolitan Statistical Areas\r\n"
