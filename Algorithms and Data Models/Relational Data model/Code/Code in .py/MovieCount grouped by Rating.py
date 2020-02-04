import pandas as pd
import matplotlib.pyplot as plt

ratingsFile = pd.read_csv("ratings_27M.csv")
rating_col = ratingsFile.rating
zero5 = 0
one = 0
one5 = 0
two = 0
two5 = 0
three = 0
three5 = 0
four = 0
four5 = 0
five = 0

for x in range(len(rating_col)) :
    if rating_col[x]==0.5 :
        zero5 +=1
    elif rating_col[x]==1 :
        one +=1
    elif rating_col[x]==1.5 :
        one5 +=1        
    elif rating_col[x]==2 :
        two +=1 
    elif rating_col[x]==2.5 :
        two5 +=1
    elif rating_col[x]==3 :
        three +=1
    elif rating_col[x]==3.5 :
        three5 +=1
    elif rating_col[x]==4 :
        four +=1        
    elif rating_col[x]==4.5 :
        four5 +=1
    elif rating_col[x]==5 :
        five +=1

x_axis = []
x = range(0,10)
for a in range(1,11):
    x_axis.append(a/2)
y_axis = [zero5,one,one5,two,two5,three,three5,four,four5,five]


plt.xticks(x,x_axis)
plt.bar(x,y_axis)
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.title("Total count of movies grouped by each rating")
plt.show()
