# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np


# %%
input = open('input_f1.txt').readlines()
input = [x.split() for x in input]
input.pop(0)


# %%
df = pd.read_csv('titanic_new.csv')
df.head()


# %%
def similarity(id1, id2):  
    result = 0
    passenger_a = df.loc[id1-1]
    passenger_b = df.loc[id2-1]  
    if passenger_a.Pclass == passenger_b.Pclass:  
        result += 1  
    if passenger_a.Sex == passenger_b.Sex:  
        result += 3  
    if passenger_a.SibSp == passenger_b.SibSp:  
        result += 1  
    if passenger_a.Parch == passenger_b.Parch:  
        result += 1  
    result += max(0, 2 - abs(passenger_a.Age - passenger_b.Age) / 10.0)  
    result += max(0, 2 - abs(passenger_a.Fare - passenger_b.Fare) / 5.0)  
    return result / 10.0


# %%
for x in input:
    id1 = int(x[0])
    id2 = int(x[1])
    print(similarity(id1, id2))


