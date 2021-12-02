import pandas as pd
input = open('f3_input.txt').read().strip().split(' ')
input = [int(x) for x in input]
district, min, max = input 

df = pd.read_csv('result.csv')

df['Average Proficiency Score'] = df['Average Proficiency Score'].str.strip('%').astype(float)


df = df[df['Average Proficiency Score'].between(min, max)]
print(df)
df = round(df[df['District'] == district]['Student Achievement Rating'].mean(),2)
if df >= 0:
    print(df)
else:
    print(0)


