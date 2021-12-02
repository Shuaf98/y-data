# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

# %%
# create list of lists of the input file.
## (could have done this with just one list)
input = open('input_f3.txt').readlines()
input = [x.split() for x in input]
input.pop(0)
# %%
df = pd.read_csv('titanic_new.csv')
df.head()
# %%
#The original pseudocode called for calling on the dataframe each time the function was called.
# This made the script run for too long. Therefore, I changed the function, and the later code, to
# read in the data frame as a list of lists. I changed the pseudocode to read that list of listsm as opposed to
# reading the data frame each time.
def similarity(id1, id2):  
    result = 0
    passenger_a = all_rows[id1-1]
    passenger_b = all_rows[id2-1]
    #Keep in mind, that this is calling on the new, edited excel file, not the original.
    # In teh new one, we deleted columns from the old, so the column indexes will be different.
    # for example, index of "Fare" is now 8, not 9. 
    if passenger_a[2] == passenger_b[2]:  
        result += 1  
    if passenger_a[4] == passenger_b[4]:  
        result += 3  
    if passenger_a[6] == passenger_b[6]:  
        result += 1  
    if passenger_a[7] == passenger_b[7]:  
        result += 1  
    result += max(0, 2 - abs(float(passenger_a[5]) - float(passenger_b[5])) / 10.0)  
    result += max(0, 2 - abs(float(passenger_a[8]) - float(passenger_b[8])) / 5.0)  
    return result / 10.0

# %%
#Make list of lists of each row, to iterate over (to find id2).
all_rows = []
for x in df.index:
   all_rows.append(list(df.iloc[x]))

# %%
for x in input:
    id1 = int(x[0])
    best_score = 0
    score_id = 0
    for row in all_rows:
        id2 = row[0]
        if id1 != id2:
            score = round(similarity(id1, id2), 2)
            #IF the similarity score is the current highest, make it the best score.
            ## This also allows for, in case of a tie, to ensure that the smallest index is called (assuming that the passengers are in numerical order)
            if score > best_score:
                best_score = score
                score_id = id2
    print(score_id)

  