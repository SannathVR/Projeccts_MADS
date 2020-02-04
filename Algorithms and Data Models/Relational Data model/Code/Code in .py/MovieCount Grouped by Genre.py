import pandas as pd
import matplotlib.pyplot as plt

moviesFile = pd.read_csv('movies_60K.csv')
genres_col = moviesFile.genres

Action = 0
Adventure = 0
Animation = 0
Childrens = 0
Comedy = 0
Crime = 0
Documentary = 0
Drama = 0
Fantasy = 0
Film_Noir = 0
Horror = 0
Imax = 0
Musical = 0
Mystery = 0
Romance = 0
Sci_Fi = 0
Thriller = 0
War = 0
Western = 0
no_genres_listed = 0

for x in range(len(genres_col)) : 
    genres = genres_col[x].split('|')
    for y in range(len(genres)) :    
        if genres[y]=="Action" :
            Action +=1
        elif genres[y]=="Adventure" :
            Adventure +=1
        elif genres[y]=="Animation" :
            Animation +=1
        elif genres[y]=="Children" :
            Childrens +=1
        elif genres[y]=="Comedy" :
            Comedy +=1
        elif genres[y]=="Crime" :
            Crime +=1
        elif genres[y]=="Documentary" :
            Documentary +=1
        elif genres[y]=="Drama" :
            Drama +=1
        elif genres[y]=="Fantasy" :
            Fantasy +=1
        elif genres[y]=="Film-Noir" :
            Film_Noir +=1
        elif genres[y]=="Horror" :
            Horror +=1
        elif genres[y]=="IMAX" :
            Imax +=1
        elif genres[y]=="Musical" :
            Musical +=1
        elif genres[y]=="Mystery" :
            Mystery +=1
        elif genres[y]=="Romance" :
            Romance +=1
        elif genres[y]=="Sci-Fi" :
            Sci_Fi +=1
        elif genres[y]=="Thriller" :
            Thriller +=1
        elif genres[y]=="War" :
            War +=1
        elif genres[y]=="Western" :
            Western +=1
        elif genres[y]=="(no genres listed)" :
            no_genres_listed +=1

x_axis = ['Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy',
          'Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','no genres listed']
y_axis = [Action,Adventure,Animation,Childrens,Comedy,Crime,Documentary,Drama,Fantasy,
          Film_Noir,Horror,Musical,Mystery,Romance,Sci_Fi,Thriller,War,Western,no_genres_listed]

plt.barh(x_axis,y_axis)
plt.ylabel("GENRES")
plt.xlabel("# Movies")
plt.title("Count of Movies per Genre")
plt.show()

print(y_axis)
