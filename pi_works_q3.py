import numpy as np
import pandas as pd


data = pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')
data['daily_vaccinations'].fillna(0,inplace = True)
data = data.loc[:, ["date" , "daily_vaccinations"]]
data = data.loc[data.date == "1/6/2021"]
data = data.groupby(['date']).sum()
print(data)

