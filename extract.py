#extract and store files
import pandas as pd
#Where the data to extract is stored

nytURL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
jhURL = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

def extract_NYT():
    try:
        df_NYT = pd.read_csv(nytURL) #dataframe for NYT data
        #print(df_NYT.head()) #Test that data is pulled
        return df_NYT
    except:
        print("Unable to extract the NYT data")

def extract_JH():
    try:
        df_JH = pd.read_csv(jhURL) #dataframe for JH data
        #print(df_JH.head()) #Test that data is pulled
        return df_JH
    
    except:
        print("Unable to extract the JH data")

df_new_york = extract_NYT()
df_john_hopkins = extract_JH()