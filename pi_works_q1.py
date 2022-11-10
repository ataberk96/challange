import numpy as np
import pandas as pd


data = pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')
data['minimum'] = 0
data['minimum'] = data.groupby('country').daily_vaccinations.transform('min')


data['daily_vaccinations'].fillna(data['minimum'],inplace = True)
data['daily_vaccinations'].fillna(0,inplace = True)

#print(data['daily_vaccinations'].min())
data = data.drop('minimum',axis=1)
print(data)