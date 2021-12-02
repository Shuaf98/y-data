import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\sfrie\Ydata_practice\Test_2\output.csv")
ratio3 = df['Year 3 - All Students Tested']/ df['Year 3 - Top Scoring']
ratio4 = df['Year 4 - All Students Tested']/ df['Year 4 - Top Scoring']
ratio5 = df['Year 5 - All Students Tested']/ df['Year 5 - Top Scoring']
ratio6 = df['Year 6 - All Students Tested']/ df['Year 6 - Top Scoring']

df2 = pd.concat([ratio3, ratio4, ratio5, ratio6], axis =1).set_index(df['School Index'])
df2.columns = ['3', '4', '5', '6']

n = int(open('f2_input.txt').read())
print(n)
highest = df2.loc[n].max()

for x in df2.loc[n]:
    if x == highest:
        print(df2.loc[n].idxmax(axis=1))
        break
else:
    print(0)  


