from extract import df_new_york, df_john_hopkins

#print(extract.df_john_hopkins) #Test that I can see the data from extract

def df_transform():
    global df_new_york
    global df_john_hopkins
    df_new_york = df_new_york.astype({'date': 'datetime64[ns]', 'cases': 'int64', 'deaths': 'int64'})
    #print(df_new_york.head()) # Test transform so far
    df_john_hopkins = df_john_hopkins[df_john_hopkins['Country/Region'] == 'US']
    print(df_john_hopkins)

df_transform()