# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import math
id = open('input.txt').read().strip('\n')
id = int(id)

users_data = pd.read_csv('users_data.csv')
calls_data = pd.read_csv('calls_data.csv')
msg_data = pd.read_csv('msg_data.csv')
web_data = pd.read_csv('web_data.csv')


users_data = pd.read_csv('users_data.csv')
calls_data = pd.read_csv('calls_data.csv')
msg_data = pd.read_csv('msg_data.csv')
web_data = pd.read_csv('web_data.csv')

plan_type = users_data[users_data['user_id'] == id].plan.item()

calls_data['duration'] = calls_data['duration'].apply(math.ceil)
calls_data = calls_data[(calls_data['user_id'] == id) & (calls_data['month'] == 12)]
calls = calls_data['duration'].sum()

msg = len(msg_data[(msg_data['user_id'] == id) & (msg_data['month'] == 12)])

web_data = web_data[(web_data['user_id'] == id) & (web_data['month'] == 12)]
web = math.ceil(web_data['gb_used'].sum())


if plan_type == 'surf':
    base = 20
    if calls >500:
        call = (calls- 500) *0.03
    else:
        calls = 0
    if msg > 50:
        msg = (msg - 50)* 0.03
    else:
        msg = 0
    if web >15:
        web = (web - 15)*10
    else:
        web = 0
if plan_type == 'ultimate':
    base = 70
    if calls > 3000:
        call = (calls- 3000) *0.01
    else:
        calls = 0
    if msg > 1000:
        msg = (msg - 1000)* 0.01
    else:
        msg = 0
    if web >30:
        (web - 30)*7
    else:
        web = 0
total = base + calls + msg + web
print(total)