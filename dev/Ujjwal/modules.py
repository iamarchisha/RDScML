import pandas as pd
import numpy as np

def sample_data(df):
    
    print("DATA DESCRIPTION")
    print(df.describe())
    print('\n\n\n')
    print(df.info())
    print('\n\n\n')
    print("FIRST FIVE DATA POINTS")
    print(df.head())
    print('\n\n\n')
    print("LAST FIVE DATA POINTS")
    print(df.tail())
    print('\n\n\n')
    print("RANDOM DATA POINTS")
    print(df.sample(5))