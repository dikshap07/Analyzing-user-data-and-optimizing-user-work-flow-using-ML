import pandas as pd
from pandas import DataFrame as 
import seaborn as sns
clickstream = pd.read_csv("C://Users//Dikhsha//FinalSpreadsheet_dikshapaliwal.xlsx - Sheet3.csv")

data = pd.DataFrame(clickstream)

data[:].fillna("N0", inplace = True) 

data = data.drop(columns = "1")
data

Row_list =[] 
  
# Iterate over each row 
for i in range((data.shape[0])): 
  
    # Using iloc to access the values of  
    # the current row denoted by "i" 
    Row_list.append(list(data.iloc[i, :])) 
  
# Print the list 
#print(Row_list) 
clean_list = []

for row in Row_list:
    new_row = []
    for i in range(len(row)):
        if row[i] != "N0" : 
            new_row.append(row[i])
    clean_list.append(new_row)        
print(clean_list)            
from markovclick.models import MarkovClickstream
m = MarkovClickstream(clean_list)
sns.heatmap(m.prob_matrix, xticklabels=m.pages, yticklabels=m.pages)
#heatmap indicates the probability matrix,the y axis represnts the current page and the x axis represents the next page.
#The lighter the color the more the probability of 
#to go from onepage to another.
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Dikhsha/Anaconda3/Library/bin/graphviz/'
from markovclick.viz import visualise_markov_chain
graph = visualise_markov_chain(m)
graph