
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# This line lets us plot on our ipython notebook
get_ipython().magic('matplotlib inline')

# Read in the data

df = pd.read_csv('Desktop/github/big-data-spring2018/week-03/data/skyhook_2017-07.csv', sep=',')

df.head()

# Create a new date column formatted as datetimes.
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Determine which weekday a given date lands on, and adjust it to account for the fact that '0' in our hours field corresponds to Sunday, but .weekday() returns 0 for Monday.
df['weekday'] = df['date'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7, 0, inplace = True)

# Remove hour variables outside of the 24-hour window corresponding to the day of the week a given date lands on.
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)


    
#Problem 1.

df['count']

df.groupby('date')['count'].sum().plot(kind='bar', title ="Pings Per Day",figsize=(7.5,5),legend=True, fontsize=12)


#Problem 2.
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
if (j>i):
        df['hour'].replace(range(j, j + 5, 1), range(-5, 0, 1), inplace=True)
        df['hour'].replace(range(i, i + 19, 1), range(0, 19, 1), inplace=True)
else:
        df['hour'].replace(range(j, i + 19, 1), range(0, 24, 1), inplace = True)

df['hour'].unique()



## Problem 3.

df['hour_new'] = pd.to_timedelta(df['hour'], unit='h')
df['time_stamp'] = df['date'] +  df['hour_new']


#Problem 4.

fig, axs = plt.subplots(1,2)

df.groupby('time_stamp')['count'].sum().plot(kind='line', title='Total Pings Time Series',figsize=(7.5,5), legend=True, fontsize=10, ax=axs[0])

df.groupby('hour')['count'].sum().plot(kind='bar', title='Pings by Hour', figsize=(7.5,5), legend=True, fontsize=15, ax=axs[1])


# Problem 5.

df[df['date']=='2017-07-10'].plot.scatter(x='lon', y='lat', figsize=(15,10), legend=True, fontsize=12)

df[df['date']=='2017-07-10'].groupby(['lat','lon'])['count'].sum().reset_index().plot.scatter(x='lon', y='lat', s=df['count']/3000, title='GPS pings 7/10/2017', figsize=(15,10), legend=True, fontsize=12)

df.dtypes
df[df['hour'].isin([8])].groupby(['lat','lon'])['count'].sum().reset_index().plot.scatter(x='lon', y='lat', s=df['count']/3000, title='GPS pings at 8am', figsize=(15,10), legend=True, fontsize=12)

df[df['hour'].isin([18])].groupby(['lat','lon'])['count'].sum().reset_index().plot.scatter(x='lon', y='lat', s=df['count']/3000, title='GPS pings 6pm', figsize=(15,10), legend=True, fontsize=12)

df[df['hour'].isin([22])].groupby(['lat','lon'])['count'].sum().reset_index().plot.scatter(x='lon', y='lat', s=df['count']/3000, title='GPS pings at 10pm', figsize=(15,10), legend=True, fontsize=12)


# Problem 6.

# I deliberately chose 8am and 6pm since they represent rush hour times and I wanted to compare these times to 10pm at night.
# I was really surprised to see a huge disparity between the morning rush hour and evening rush hour. 6pm seems have much more GPS pings than the other time slots. 6pm also shows the most amount of activity in the downtown areas of Boston which signals the rise in both commuting as well as commercial activity at this time.
# This exercise highlights the most used transport routes in the metro area. However, one of the limitations of the data is just that, the widely transportation routes are identified, however, the dataset says much less about settlement patterns and economic activity- though these things may be all correlated we may need to compliment this dataset with more information.
#This data can give us insight on which transportation routes are most used and which of these highly used routes are prone to the effects of climate change. This datasets can help policy makers ensure that precautions are taken to ensure these routes are safe. 

