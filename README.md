# US-Labor-Data-and-Mental-Health-Outcomes

## Authors

Mira Chew, Rajiv Perera

## Description
Using Federally collected data from the Bureau of Labor Statistics (BLS) to examine trends of workplace deaths in different states across the USA.

This project pulls data from an API provided by the BLS website. From the json formatted data, we convert it into a dictionary, then to a data frame, and finally to a csv file called data.csv. From this file, we visualize it using the visualizing_data.py file. Visualizing can also be done by running the code cells in the computational essay Jupyter notebook.

## Set-Up

To generate and visualize data, we used a few different libraries (matplotlib, pandas, & requests).

| Library     | Function use               |
| ----------- | -------------------------- |
| matplotlib  | Visualizing/plotting data  |
| pandas      | Creating DataFrames        |
| requests    | Converting data            |

To install these libraries, run
>`pip install -r requirements.txt`

There are two ways to generate and visualize the data. The easiest way is to just use the `data.csv` file as you data. If you use this, you can skip to running the visualizing data section.

The second option requires creating an API key.

To create and API key, access the BLS website, [https://www.bls.gov/developers/home.htm], and sign up to create an key. The key will then appear in your email. Create a new file called `keys.py` with a signle line:
> BLS_key = <your-key>

Save this file and then run `generate_data.py` This should create a csv file called `data.csv`.

## Visualizing The Data

Once you have the `data.csv` file, you can visualize the data simply by running the `visualizing_data.py` file. A first figure will appear. The second figure will appear only once you close the first one.

You can also visualize the data by running all of the code cells in `computational_essay.ipynb`. The very first code cell must be run first to ensure you have imported the data and functions properly.