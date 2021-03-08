'''
Program on Data Visualization using Seaborn
Author : Siddhi Naik
CWID: A20444173
'''

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import mean

# Reading and Loading Data from files
titanic=sns.load_dataset("titanic")
workerstip=pd.read_csv("workerstips.csv")
flightsData=pd.read_csv("flightsData.csv")


# Scatter Plot of worker's tip against total bill
def Worker_tip():
    sns.scatterplot(x="total_bill", y="tip", data=workerstip)
    plt.title("Scatter Plot of Worker's Tip")
    plt.show()


# Scatter Plot of Workers Who smoke and those who don't smoke
def Somking_Workers():
    sns.scatterplot(x="total_bill", y="tip", hue="smoker", size="size", sizes=(10, 300), data=workerstip)
    plt.title("Scatter Plot of Smoking and Non-Smoking Workers")
    plt.show()


# Average tip of Workers using Bar Plot
def Average_Tip():
    sns.barplot(x="day", y="tip", data=workerstip, order=["Thur", "Fri", "Sat", "Sun"])
    plt.title("Average Tip of Workers")
    plt.show()


# Graph of Lunch and Dinner Time Division
def Lunch_Dinner():
    # ScatterPlot
    sns.scatterplot(x="total_bill", y="tip", hue="time", size="size", sizes=(10, 300), data=workerstip)
    plt.title("Time Division of Workers")
    plt.show()
    # BoxPlot
    sns.boxplot(x="day", y="total_bill", data=workerstip, hue="time",
                hue_order=["Lunch", "Dinner"], order=["Thur", "Fri", "Sat", "Sun"])
    plt.title("Lunch and Dinner time Division")
    plt.show()


# Line plot of average passengers travelling per month
def Average_Passengers():
    #sns.relplot(x="year", y="passengers", data=flightsData, kind="line")
    sns.lineplot(x="year", y="passengers",hue="month", dashes=False, style="month", data=flightsData, estimator=mean)
    plt.title("Average Passengers per Year per Month")
    plt.show()


# Line Plot of Passengers travelling per year
def Passengers():
    sns.lineplot(x="year", y="passengers", data=flightsData)
    plt.title("Passengers Travelling per Year")
    plt.show()


# Categorical data from the Titanic
def Titanic_Count():
    sns.set(style="darkgrid")
    sns.catplot(x="class", hue="who", col="survived",
                data=titanic, kind="count",
                height=5, aspect=.5)
    plt.title("Titanic data")
    plt.show()


# Beginning of the Program
Worker_tip()
Somking_Workers()
Average_Tip()
Lunch_Dinner()
Average_Passengers()
Passengers()
Titanic_Count()
