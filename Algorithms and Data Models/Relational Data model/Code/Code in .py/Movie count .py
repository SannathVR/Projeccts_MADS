import pandas as pd
from matplotlib import pyplot as plt

moviesFile = pd.read_csv("movies_60K.csv")

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

y_axis = [len(twenties),len(thirties),len(forties),len(fifties),len(sixties),len(seventies),len(eighties),
         len(ninties),len(aughts),len(tens)]

x_axis = []
for x in range(192,202) :
    x = x*10
    x_axis.append(x)

plt.plot(x_axis,y_axis,color='black')
plt.plot(x_axis,y_axis,'o', color='red')
plt.xlabel("Decades")
plt.ylabel("Movies Count")
plt.title("Number of movies per decade from 1920-2010")
plt.show()

plt.bar(x_axis,y_axis)
plt.xlabel("Decades")
plt.ylabel("Movies Count")
plt.title("Number of movies per decade from 1920-2010")
plt.show()


plt.pie(y_axis,labels=y_axis,textprops={'fontsize': 9}, counterclock=False,startangle=180)
plt.axis('equal')
plt.legend(x_axis,title='Decades', bbox_to_anchor=(1,0.5),loc='right', bbox_transform=plt.gcf().transFigure)
plt.title("Number of movies per decade from 1920-2010")
plt.show()
