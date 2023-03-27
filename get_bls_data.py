from keys import BLS_key
import json
import requests
import prettytable
import pandas as pd


def json_extract(json_data, state):
    """
    creates a pandas dataframe from a json object created by BLS API call

    args:
        json_data:  dict
            dictionary with json data for single state
        state: str
            name of state (full, not shortened) i.e. Georgia

    returns:
        pandas df
    """
    seriesID = json_data["Results"]["series"][0]["seriesID"]

    series_list = []
    # pd.DataFrame(columns=["year/month", "value"])

    series_data = json_data["Results"]["series"][0]["data"]
    for month_data in series_data:
        year_and_month = month_data["year"] + "/" + month_data["periodName"]
        data_value = month_data["value"]
        series_list.append([year_and_month, data_value])
    series_dataframe = pd.DataFrame(series_list, columns=["year/month", state])

    return series_dataframe


def grab_json(api_key, state_name, series_id_sample):

    # data = json.dumps(
    #     {
    #         "seriesid": active_series_list,
    #         "startyear": "2000",
    #         "endyear": "2008",
    #         "registrationkey": BLS_key,
    #     }
    #     )
    pass
# -----------------------------------------------------------------------------

active_series_list = []
#### for series: SM -> state and area employment, hours, earnings
active_series_list.append("SMU19197802023800001")
# 19 -> iowa, 19780 -> des moines,20238000 -> specialty trade contractors,
# 01 -> datatype all employees 10000s

active_series_list.append("SMU12000000500000002")
# 19 -> iowa, 00000 -> statewide ,05000000 -> total private,
# 01 -> datatype all employees (1000s))
# 02	Average Weekly Hours of All Employees [[[not typically present]]]
# 03	Average Hourly Earnings of All Employees, In Dollars [[[not typically present]]]
# 06	Production or Nonsupervisory Employees, In Thousands
# 07	Average Weekly Hours of Production Employees
# 08	Average Hourly Earnings of Production Employees, In Dollars
# 11	Average Weekly Earnings of All Employees, In Dollars


headers = {"Content-type": "application/json"}
data = json.dumps(
    {
        "seriesid": active_series_list,
        "startyear": "2000",
        "endyear": "2008",
        "registrationkey": BLS_key,
    }
)
p = requests.post(
    "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
)
json_data = json.loads(p.text)
print(json_data)
# json_extract(json_data)



{
    "series": [
        {
            "seriesID": "SMU12000000500000002",
            "data": [
                {
                    "year": "2008",
                    "period": "M12",
                    "periodName": "December",
                    "value": "34.8",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M11",
                    "periodName": "November",
                    "value": "35.2",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M10",
                    "periodName": "October",
                    "value": "35.1",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M09",
                    "periodName": "September",
                    "value": "34.9",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M08",
                    "periodName": "August",
                    "value": "35.1",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M07",
                    "periodName": "July",
                    "value": "35.4",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M06",
                    "periodName": "June",
                    "value": "36.2",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M05",
                    "periodName": "May",
                    "value": "35.0",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M04",
                    "periodName": "April",
                    "value": "35.0",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M03",
                    "periodName": "March",
                    "value": "35.3",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M02",
                    "periodName": "February",
                    "value": "35.2",
                    "footnotes": [{}],
                },
                {
                    "year": "2008",
                    "period": "M01",
                    "periodName": "January",
                    "value": "35.7",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M12",
                    "periodName": "December",
                    "value": "35.7",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M11",
                    "periodName": "November",
                    "value": "35.2",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M10",
                    "periodName": "October",
                    "value": "35.0",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M09",
                    "periodName": "September",
                    "value": "35.4",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M08",
                    "periodName": "August",
                    "value": "35.2",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M07",
                    "periodName": "July",
                    "value": "35.6",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M06",
                    "periodName": "June",
                    "value": "35.4",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M05",
                    "periodName": "May",
                    "value": "35.1",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M04",
                    "periodName": "April",
                    "value": "36.0",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M03",
                    "periodName": "March",
                    "value": "35.3",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M02",
                    "periodName": "February",
                    "value": "35.8",
                    "footnotes": [{}],
                },
                {
                    "year": "2007",
                    "period": "M01",
                    "periodName": "January",
                    "value": "35.2",
                    "footnotes": [{}],
                },
            ],
        }
    ]
}
