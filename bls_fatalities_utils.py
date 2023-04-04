"""
    Convert data from an API call to a readable CSV with states, years, & data
"""
from init_state_dicts import make_state_dict, create_all_state_ids
from call_api import get_series_json
from keys import BLS_key
from conversions import dict_to_df, df_to_csv


state_dict = make_state_dict("https://download.bls.gov/pub/time.series/fw/fw.area")
series_ids_dict = create_all_state_ids(state_dict, "FWU00X00000080S40", -3)

begin_year, end_year = 2011, 2020

state_fatalities_json = get_series_json(series_ids_dict, begin_year, end_year, BLS_key)

fatal_panda = dict_to_df(series_ids_dict, state_fatalities_json, begin_year, end_year)


df_to_csv(fatal_panda)
