# %load q03_top_in_each_year_1/build.py

import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q03_top_in_each_year_1(df):
    'write your solution here'
    return df[['Year', 'Name', 'Count']].set_index('Name').to_dict()
    
q03_top_in_each_year_1(data)


