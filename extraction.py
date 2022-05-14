#extract and store files

import pandas as pd

#Where the data to extract is stored

nytURL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
jhURL = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

dfNYT = pd.read_csv(nytURL) #dataframe for NYT data
dfJH = pd.read_csv(jhURL) #dataframe for JH data

#verify that data is being pulled
#print(dfNYT.head())
#print(dfJH.head())

dfNYT.to_csv('NYT_DATA.csv', index=False)
dfJH.to_csv('John_Hopkins_Data.csv', index=False)

#test
#Test