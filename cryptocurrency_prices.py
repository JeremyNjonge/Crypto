# Importing relevant modules
import pandas_datareader.data as reader
import datetime as dt
import matplotlib.pyplot as plt

start = dt.date(2021,1,1) # Start date
end = dt.datetime.now() # End date
crypto = ['ETH-USD'] 

df = reader.get_data_yahoo(crypto,start,end)['Close'] # Dataframe with ETH-USD data
df.to_csv('ethdata.csv') # Save to csv file
