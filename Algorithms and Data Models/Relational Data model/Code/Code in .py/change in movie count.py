import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

moviesFile = pd.read_csv("movies.csv")
title = moviesFile.title
tens = []
aughts = []
ninties = []
eighties = []
seventies = []
sixties = []
fifties = []
forties = [] 
thirties = []
twenties = []

for x in range(len(title)) :
    yr = title[x].split('(')[-1]
    year = yr[0:4]    
    if year.isdigit():
        year_int = int(year)
        if year_int>2010 and year_int<2021 : 
            tens.append(year_int)
        elif year_int>2000 and year_int<2011 :
            aughts.append(year_int)
        elif year_int>1990 and year_int<2001 :
            ninties.append(year_int)
        elif year_int>1980 and year_int<1991 :
            eighties.append(year_int)
        elif year_int>1970 and year_int<1981 :
            seventies.append(year_int)
        elif year_int>1960 and year_int<1971 :
            sixties.append(year_int)
        elif year_int>1950 and year_int<1961 :
            fifties.append(year_int)
        elif year_int>1940 and year_int<1951 :
            forties.append(year_int)
        elif year_int>1930 and year_int<1941 :
            thirties.append(year_int)
        elif year_int>1920 and year_int<1931 :
            twenties.append(year_int)

x_axis = []
for x in range(192,202) :
    x = x*10
    x_axis.append(x)

y_axis = [len(twenties),len(thirties),len(forties),len(fifties),len(sixties),len(seventies),len(eighties),
         len(ninties),len(aughts),len(tens)]


perChange = [0]
for x in range(len(y_axis)):
   if x < (len(y_axis)-1):
        percentage = (y_axis[x+1]/y_axis[x])*100
        perChange.append(percentage - 100)
        
greenBar = []
redBar = []
mag = []
for x in range(len(perChange)):
    mag.append(np.sign(perChange[x]))
for x in range(len(mag)):
    if mag[x]==0 or mag[x]==1:
        greenBar.append(perChange[x])
        redBar.append(0)
    else: 
        redBar.append(abs(perChange[x]))
        greenBar.append(0)

plt.bar(x_axis,greenBar,width=8,label='Increasing rate',color='green')
plt.bar(x_axis,redBar,width=8,label='decreasing rate', color='red')
plt.legend()
plt.title("Rate of change in number of movies")
plt.xlabel("Percentage Change")
plt.ylabel("Decades")
plt.show()

