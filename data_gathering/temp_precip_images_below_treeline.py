#This saves images for all years of interest

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from datetime import date, timedelta
# %matplotlib inline

# The whistler_weather_good.csv is weather data captured at 650m elevation. 
# This is "below treeline" and so this is the danger rating we will try to predict with this data.
df = pd.read_csv('../data/whistler_weather_good.csv')

dateTime = df['Date/Time']
year = df['Year']
month = df['Month']
day = df['Day']
maxT = df['Max Temp']
meanT = df['Mean Temp']
minT = df['Min Temp']
P = df['Total Precip (mm)']

startYear = 2012
finalYear = 2012

inds = []
dates = []
for year in range(startYear,finalYear+1):

    startDate = str(year)+'-01-01' #YYYY-MM-DD
    finalDate = str(year)+'-03-31'

    d1 = date(int(startDate[0:4]), int(startDate[5:7]), int(startDate[8:10]))  # start date
    d2 = date(int(finalDate[0:4]), int(finalDate[6]), int(finalDate[8:10]))  # end date

    delta = d2 - d1
    dates = dates+[str(d1+timedelta(i)) for i in range(delta.days+1)] #list of dates (strings) during time range of interest
     
#get indices in weather data that correspond to these dates -- this is bulky but my MATLAB brain struggles with simple python things sometimes...
inds = [np.argwhere(dateTime==dates[i]) for i in range(len(dates))] #this is a list of arrays
inds = [inds[i].tolist() for i in range(len(inds))]
indsDummy = []
i = 0
for index in inds:
    indsDummy.append(index[0][0])
    i+=1
inds = indsDummy

#max/min values on the x/y axis need to all be the same on all images
xmin = np.nanmin([meanT[i] for i in inds])
xmax = np.nanmax([meanT[i] for i in inds])
ymin = np.nanmin([P[i] for i in inds])
ymax = np.nanmax([P[i] for i in inds])

s = 1 # Segment length -- we colour the line in segments in order to get a gradient of a colourmap across the line in time
numPrevDays = 30
n = numPrevDays
rgb = cm.get_cmap(name='Reds',lut=n)

for ind in inds: #for each day
    
    currDay = dateTime[ind]
    prevDayInds = range(np.subtract(ind,30)+1,ind)
    
    x = [meanT[i] for i in prevDayInds]
    y = [P[i] for i in prevDayInds]
    
    plt.subplot(1,1,1)
    for i in range(0,n,s): #this plots and colours each segment on the current plot
        plt.plot(x[i:i+s+1],y[i:i+s+1],color=rgb(i)[0:3])
        
    plt.xlim([xmin,xmax])
    plt.ylim([ymin,ymax])
    plt.axis('off')
    plt.show()
    
    fileDir = '../data/temp_prec_images/'
    filename = 'temp_precip_prev' + str(numPrevDays) + '_Reds_' + currDay + '.png'
    
    if saveIt is True:
        plt.savefig(fileDir+filename)