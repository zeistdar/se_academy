# import what you need
import pandas as pd
import json

# Read players.csv
with open('players.csv') as csv_file:
    csv_data = csv_file.read()
print(csv_data)

df_csv = pd.read_csv('players.csv')
print(df_csv)

# Read stats.json
with open('stats.json') as json_file:
    json_data = json.load(json_file)
print(json_data)

# get data of the files into pandas dataframes (need to normalize the json data)
df_json = pd.io.json.json_normalize(json_data['players'])
print(df_json)

# Combine the data with pandas (what function?)
df_comb = pd.merge(df_csv, df_json, 'outer')
print(df_comb)


# Result could e.g. look like this:
#               name              team    position  goals  matches
# 0      Teemu Pukki   Norwich City FC     Forward   25.0     80.0
# 1        Tim Sparv     FC Mitjylland    Midfield    1.0     74.0
# 2  Paulus Arajuuri          Pafos FC    Defender    NaN      NaN
# 3   Lukas Hradecky  Bayer Leverkusen  Goalkeeper    0.0     58.0
# 4     Joona Toivio               NaN         NaN    3.0     65.0

# Write the combined data into a file (if you want try writng the file compressed (e.g. gzip))
df_comb.to_csv('combined_data.csv')

# csv data modification
split_data = csv_data.split('\n')
print(split_data)
split_data = [x.split(',') for x in csv_data.split('\n')]
print(split_data)

# First collect all names
names = set([x['name'] for x in json_data['players']] + [x[0] for x in split_data[1:]])
print(names)

columns = set(split_data[0])

# Extract the column names from the json data

print(columns)

name_list = list(names)
column_list = list(columns)

