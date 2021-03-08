'''
This program below creates Series, DataFrames using Pandas and performs operations on them.
Author: Siddhi Naik

'''

import pandas as pd
import random as rd

# Part one Series

# Pandas  series created from list
ls=[7, 11, 13, 17]
ds=pd.Series(ls)
print("The Series is: \n",ds, "\n")

# Series containing 5 times 100.0
ds2=pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])
print("Series with value 5 times 100.0 is: \n",ds2, "\n")

# Series containing 20 random numbers from 0 to 100
ds3=pd.Series(rd.sample(range(0, 100), 20))
print("The Series with 20 random numbers from 1 to 100 is: \n",ds3, "\n")

# Descriptive Stats for Series with Random Numbers
print("The descriptive Statistics for series with random number are: \n",ds3.describe(), "\n")

# Series temperature with customized index values
temperatures=pd.Series([98.6, 98.9, 100.2, 97.9])
temperatures.index=['Julie', 'Charlie', 'Sam', 'Andrea']
print("The series temperature is: \n",temperatures, "\n")

# Converting Series to Dictionary and then Dictionaryu back to Series
t1 = temperatures.to_dict()
print("Dictionary created using Series temperatures is: \n ",t1, "\n")
temperatures2 = pd.Series(t1)
print("The series temperature after recreating from Dictionary is: \n",temperatures2, "\n")


# Part2 DataFrames
# Pandas data frame with temperatures for each person
data = [[98.5, 97.8, 98.2], [100.5, 99.6, 99.0], [ 99.4, 100.0, 99.8]]
temperatures = pd.DataFrame(data, columns=['Maxine', 'James', 'Amanda'])
print("The dataframe Temperatures is: \n",temperatures, "\n")

# Recreated Dataframe with custom indexes
temperatures = pd.DataFrame(data, index=['Morning', 'Afternoon', 'Evening'], columns=['Maxine', 'James', 'Amanda'])
print("The recreated dataframe Temperatures is \n",temperatures, "\n")

# Temperatures for Maxine
print("Temperatures for Maixne are: \n",temperatures['Maxine'], "\n")

# Temperatures in morning
print("Temperatures in Morning are: \n",temperatures.loc['Morning', :], "\n")

# Temperatures in morning and evening
print("Temperatures in Morning and Evening  are: \n",temperatures.loc[['Morning', 'Evening'], :], "\n")

# Temperatures for Amanda and Maxine
print("Temperatures for Amanda and Maxine  are: \n",temperatures.loc[:, ['Maxine','Amanda']], "\n")

# Temperatures in morning and afternoon for Amanda and Maxine
print("Temperatures for Amanda and Maxine in Morning and Afternoon are: \n",temperatures.loc[['Morning', 'Afternoon'], ['Maxine','Amanda']], "\n")

# Descriptive Statistics on the Dataframe
print("The descriptive Statistics for the temperatures are: \n",temperatures.describe(), "\n")

# Transpose of DataFrame
print("The transposed dataframe 'Temperatures' is: \n",temperatures.transpose(), "\n")

# Sorting Data Frame
temperature = temperatures.sort_index()
print("The sorted columns dataframe 'Temperatures' are: \n",temperature.transpose(), "\n")



