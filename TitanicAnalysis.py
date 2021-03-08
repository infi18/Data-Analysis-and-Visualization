'''
This program below reads data from the titanic.csv file and performs analysis using Pandas and DataFrames
Author: Siddhi Naik

'''
import pandas as pd
import csv

# Extracting data from csv
data = pd.read_csv('titanic.csv')
t_df = pd.DataFrame(data)

# Total number of people on Titanic
print("Total number of people on the titanic were: ", t_df.shape[0], "\n")

# Total number of males and females on the titanic
male= t_df[t_df['Sex'] == 'male']
female= t_df[t_df['Sex'] == 'female']
print("The total number of females and males on the Titanic: ",male.shape[0]," males and ",female.shape[0], "female\n")

# Average age of person on Titanic
mean = t_df['Age'].mean(axis = 0)
print("The average age of people on Titanic is: ", mean, "\n")

# Number of people with age less than 21
age = t_df[t_df['Age'] < 21]
print("The people on Titanic with age under 21: ", age.shape[0], "\n")

# Below is the number of males and females that survived the titanic
survived = t_df.loc[t_df["Survived"] == 1, ["Survived"]].shape[0]
surv = t_df.loc[t_df["Survived"] == 1, ["Survived", "Sex"]]
surv_males = surv.loc[t_df["Sex"] == "male"].shape[0]
surv_females = surv.loc[t_df["Sex"] == "female"].shape[0]
print("The total number of passengers that survived the Titanic are:", survived, "\n")
print("The total number of males that survived the Titanic are:", surv_males, "\n")
print("The total number of females that survived the Titanic are:", surv_females, "\n")

# Below is the number the males and females that didnt survive the titanic
non_survived = t_df.loc[t_df["Survived"] == 0, ["Survived"]].shape[0]
nsurv = t_df.loc[t_df["Survived"] == 0, ["Survived", "Sex"]]
Nsurv_males = nsurv.loc[t_df["Sex"] == "male"].shape[0]
Nsurv_females = nsurv.loc[t_df["Sex"] == "female"].shape[0]

print("The total number of passengers that did not survive the Titanic:", non_survived, "\n")
print("The total number of males that did not survive the Titanic:", Nsurv_males, "\n")
print("The total number of females that did not survive the Titanic:", Nsurv_females, "\n")


# Prints the names of the people who survived the Titanic with minimum and maximum age
Agesurv = t_df.loc[t_df['Survived'] == 1]
age_surv = Agesurv.loc[1:, ['Age']]

print("The minimum and maximum age that survived titanic is: \n",age_surv.describe().stack()[['min','max']], "\n")
print("Name of the person with minimum age that survived titanic is: \n", t_df.loc[t_df["Age"] == 0.42, "Name"], "\n")
print("Name of the person with maximum age that survived titanic is: \n", t_df.loc[t_df["Age"] == 0.42, "Name"], "\n")


# Prints the name of the people who survived the Titanic
surv_name = t_df.loc[t_df["Survived"] == 1,  "Name"]
print("The names of passengers that survived the titanic: \n", surv_name)


