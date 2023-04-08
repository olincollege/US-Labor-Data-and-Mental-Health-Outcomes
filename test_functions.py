"""
Test api call function to make sure it is calling API properly
and retrieving data
"""
from pathlib import Path
import pandas as pd
from init_state_dicts import make_state_dict, create_all_state_ids
from conversions import dict_to_df, df_to_csv


state_dict = make_state_dict("https://download.bls.gov/pub/time.series/fw/fw.area")
state_ids_dict = create_all_state_ids(state_dict, "FWU00X00000080S40", -3)
test_data = {
    "Results": {
        "series": [
            {
                "seriesID": "1",
                "data": [
                    {"year": "2020", "value": "85"},
                    {"year": "2019", "value": "89"},
                    {"year": "2018", "value": "89"},
                ],
            },
            {
                "seriesID": "2",
                "data": [
                    {"year": "2020", "value": "31"},
                    {"year": "2019", "value": "51"},
                    {"year": "2018", "value": "32"},
                ],
            },
        ]
    }
}
test_state_ids_dict = {"State_1": "1", "State_2": "2"}
data_frame = dict_to_df(test_state_ids_dict, test_data, 2018, 2020)
df_to_csv(data_frame, "test_data")


def test_state_dict_is_dict():
    """
    Check that make_state_dict returns a dict
    """
    assert isinstance(state_dict, dict)


def test_state_dict_len():
    """
    Check that make_state_dict returns dict of length of at least 50
    """
    assert len(state_dict) >= 50


def test_state_dict_has_idaho():
    """
    Chceck that make_state_dict includes Idaho as a key
    """
    assert "Idaho" in state_dict


def test_state_ids_len():
    """
    Check that create_all_state_ids creates dict of length 50
    """
    assert len(state_ids_dict) == 50


def test_state_ids_include_idaho():
    """
    Chceck that create_all_state_ids includes Idaho as a key
    """
    assert "Idaho" in state_ids_dict


def test_state_ids_returns_dict():
    """
    Check that create_all_state_ids returns a dictionary
    """
    assert isinstance(state_ids_dict, dict)


def test_dict_to_df_is_df():
    """
    Check that dict_to_df returns a df
    """
    assert isinstance(data_frame, pd.DataFrame)


def test_csv_exists():
    """
    Check that a csv file with name test_data.csv exists
    """
    assert Path("test_data.csv").exists()


def test_df_state_1():
    """
    Check that State_1 row of dict_to_df returns correct values
    This simultaneously checks that the lengths are the same as well
    """
    state_index = 0
    state_1_data = [int(value) for value in data_frame.iloc[state_index]]
    expected_values = []
    for item in test_data["Results"]["series"][state_index]["data"]:
        expected_values.append(int(item["value"]))
    assert state_1_data == expected_values


def test_df_year_2020():
    """
    Check the data for year of 2020 returns correct values
    """
    expected_year_data = [
        int(item["data"][0]["value"]) for item in test_data["Results"]["series"]
    ]
    actual_year_data = [int(value) for value in data_frame.loc[:, "2020"]]
    assert actual_year_data == expected_year_data
