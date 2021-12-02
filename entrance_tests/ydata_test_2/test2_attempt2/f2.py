# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
df = pd.read_csv('schools (1).csv')

df = df[df['Student Attendance Rate'].str.rstrip('%').astype('int')/100 >0]
df = df[df['Rigorous Instruction'].str.rstrip('%').astype('int')/100 >0]
df = df[df['Students Chronically Absent'].str.rstrip('%').astype('int')/100 <1]

df =df.dropna(subset = ['Student Achievement Rating', 'Average Proficiency Score'])

def change(n):
    if n == 'Exceeding Target': return 1.0
    if n == 'Meeting Target': return 0.8
    if n == 'Approaching Target': return 0.5
    if n == 'Not Meeting Target': return 0.0
df['Student Achievement Rating'] = df['Student Achievement Rating'].apply(change)



# %%

result = df.to_csv('result.csv', index = False)

def find_best(i):
    bests = 0
    result = 0
    valid = []
    
    six =  df.loc[i]['Year 6 - Top Scoring']/ df.loc[i]['Year 6 - All Students Tested']
    if df.loc[i]['Year 6 - All Students Tested'] >= 0:
        if six >= bests:
            bests = six
            result = 6
            valid.append(6)
    five = df.loc[i]['Year 5 - Top Scoring']/  df.loc[i]['Year 5 - All Students Tested'] 
    if df.loc[i]['Year 5 - All Students Tested'] >= 0:
        if five >= bests:
            bests = five
            result = 5
            valid.append(5)
    four =  df.loc[i]['Year 4 - Top Scoring']/ df.loc[i]['Year 4 - All Students Tested']
    if df.loc[i]['Year 4 - All Students Tested'] >= 0:
        if four >= bests:
            bests = four
            result = 4
            valid.append(4)
    three = df.loc[i]['Year 3 - Top Scoring']/ df.loc[i, 'Year 3 - All Students Tested'] 
    if df.loc[i]['Year 3 - All Students Tested'] != 0:
        if three >= bests:
            bests = three
            result = 3
            valid.append(3)
    if len(valid) == 0:
        return 0
    return result
    # return(min(best, key = best.get))


file = open('f2_input.txt').read().strip()
i = int(file)

df = df.set_index('School Index')
print(df.head(5))
print(find_best(i))
    
