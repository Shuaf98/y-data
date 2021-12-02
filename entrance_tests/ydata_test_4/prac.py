import pandas as pd

df = pd.read_csv('weather_data.csv')

#create the weather columns in the weather data
weather = list(df['description'])
def weatherType(y):
    
    if y == "sky is clear":
        return 'clear'
    elif y == "mist" or y == "fog" or y == "haze":
        return 'impaired visibility'
    elif 'clouds' in y:
        return 'cloudy'
    elif 'rain' in y or 'drizzle' in y or 'thunderstorm' in y:
        return 'rainy'
    elif y == "light snow":
        return "snow"
df['weather_type'] = df['description'].apply(weatherType)


def code(x):
    if x == "clear":
        return 1
    elif x == 'impaired visibility':
        return 2
    elif x =='cloudy':
        return 3
    elif x == 'rainy':
        return 4
    elif x == 'snowy':
        return 5
df['code'] = df['weather_type'].apply(code)

df2 = pd.read_csv('rides_data.csv')
input = open('inputF2.txt').read().strip()
input = int(input)

start = df2[df2['TRIP_ID'] == input].START_TS.item()


index = df[df['ts'] == start].code.item()
print(int(index))

