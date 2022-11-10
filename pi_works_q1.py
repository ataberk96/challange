import numpy as np
import pandas as pd


data = pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')
data['daily_vaccinations'].fillna(0,inplace = True)
data = data.groupby(['country'])['daily_vaccinations'].min()
#print(data['daily_vaccinations'].min())

print(data)