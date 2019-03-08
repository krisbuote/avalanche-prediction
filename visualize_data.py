import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data_path = './data/sample_weather_prepared.csv'
df = pd.read_csv(data_path, usecols=["Date/Time","Data Quality","Max Temp (°C)","Min Temp (°C)",
	"Mean Temp (°C)","Heat Deg Days (°C)","Cool Deg Days (°C)","Total Rain (mm)",
	"Total Snow (cm)","Total Precip (mm)","Snow on Grnd (cm)"])

df.drop(df.index[60:] , inplace=True)# Just use the first 60 entries available
print(df.describe())

hist = df.hist(bins=6)
plt.show()