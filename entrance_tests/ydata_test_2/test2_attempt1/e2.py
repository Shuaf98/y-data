
import pandas as pd
import numpy as np
import os
os.chdir(r"C:\Users\sfrie\Ydata_practice\Test_2")
df = pd.read_csv('purchase_data.csv')
input = open('e1_input.txt').read()
prod1, prod2 = input.split()

members = list(df['memberID'].unique())

def find_common(prod1, prod2):
    all_members = []
    for x in members:
        test = df[df['memberID'] == x]
        if int(prod1) in test['productID'].values and int(prod2) in test['productID'].values:
            all_members.append(x)
    if all_members != []:
        return all_members
    else:
        return 0

def similarity (product_1, product_2):  
    common = find_common(product_1, product_2) 
    sum_mult =0
    sum_sq_1=0
    sum_sq_2=0
    for member in common:  
        prod1_count = len(df[(df['memberID'] == member) & (df['productID'] == int(product_1))])
        prod2_count = len(df[(df['memberID'] == member) & (df['productID'] == int(product_2))])
        prod1_score = int(df[df['productID'] == int(product_1)]['productScore'].unique())
        prod2_score = int(df[df['productID'] == int(product_2)]['productScore'].unique())
        sum_mult += (prod1_count - prod1_score) *  (prod2_count - prod2_score)  
        sum_sq_1 += pow((prod1_count - prod1_score), 2)
        sum_sq_2 += pow((prod2_count - prod2_score), 2)
    similarity = sum_mult / (np.sqrt(sum_sq_1) * np.sqrt(sum_sq_2))
    if similarity != np.nan:
        return round(similarity, 2)
    else:
        return 'NA'
if int(prod1) in list(df['productID']) and int(prod2) in list(df['productID']):
    print(similarity(prod1, prod2))
else:
    print('NA')


