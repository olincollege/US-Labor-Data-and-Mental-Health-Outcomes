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
    