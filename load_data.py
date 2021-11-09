import numpy as np
import pandas as pd
from collections import Counter, deque
from itertools import chain, product
import heapq
from io import StringIO
import urllib.request
import json


# using with statement to open a file
# open function:
# r: open for reading (default)
# w: open for writing, truncating the file first
# a: open for writing, appending to the end of the file if it exists
# b: open in binary mode
# t: text mode
# +: open for updating, both reading and writing
file_path = 'try.txt'
content = []
with open(file_path, ) as fp:
    lines = fp.readlines()
    for line in lines:
        content.append(line)


# using numpy to open a file
np.loadtxt('try.txt',
           delimiter=',',
           dtype={'names': ('gender', 'age', 'weight'),
                  'formats': ('S1', 'i4', 'f4')})


# using pandas
data = pd.read_csv('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt', sep='\t')
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
print(df.unstack(level=-1))

# using pandas: iterate through rows or columns
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n Example iterrows \n")
for index, col in employees.iterrows():
    print(col)
    print(col['Name'], "--", col['Age'])

print("\n Example itertuples \n")
for row in employees.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), "--", getattr(row, "Age"), '--', getattr(row, 'Index'))

# using pandas: check if the dataframe is empty
df_empty = pd.DataFrame()
if df_empty.empty:
    print('data frame is empty')


# using pandas: using time span to create dataframe
import datetime
import pandas as pd

todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=10, freq='D')

columns = ['A', 'B', 'C']

df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)

print(df)

# using pandas: transform one column to date type
df = pd.DataFrame({'DateOFBirth': [1349720105, 1349806505, 1349892905,
                                   1349979305, 1350065705, 1349792905,
                                   1349730105],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n----------------Before---------------\n")
print(df.dtypes)
print(df)

df['DateOFBirth'] = pd.to_datetime(df['DateOFBirth'], unit='s')

print("\n----------------After----------------\n")
print(df.dtypes)
print(df)

# using pandas: appending/concatenating/ two dataframe
df1 = pd.DataFrame({'Age': [30, 20, 22, 40], 'Height': [165, 70, 120, 80],
                    'Score': [4.6, 8.3, 9.0, 3.3], 'State': ['NY', 'TX',
                                                             'FL', 'AL']},
                   index=['Jane', 'Nick', 'Aaron', 'Penelope'])

df2 = pd.DataFrame({'Age': [32, 28, 39], 'Color': ['Gray', 'Black', 'Red'],
                    'Food': ['Cheese', 'Melon', 'Beans'],
                    'Score': [1.8, 9.5, 2.2], 'State': ['AK', 'TX', 'TX']},
                   index=['Dean', 'Christina', 'Cornelia'])

df3 = df1.append(df2, sort=True)

print(df3)

# using pandas: check if data frame contains a string
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])

if df['State'].str.contains('TX').any():
    print("TX is there")

# using pandas: deleting duplicated rows:
df = pd.DataFrame({'Age': [30, 30, 22, 40, 20, 30, 20, 25],
                   'Height': [165, 165, 120, 80, 162, 72, 124, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\n -------- Duplicate Rows ----------- \n")
print(df)

df1 = df.reset_index().drop_duplicates(subset='index',
                                       keep='first').set_index('index')

print("\n ------- Unique Rows ------------ \n")
print(df1)

# using pandas: replacing with dictionary
df = pd.DataFrame({'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df)

d = {"NY": 1, "TX": 2, "FL": 3, "AL": 4, "AK": 5}
df1 = df.replace({"State": d})

print("\n\n")
print(df1)

# using pandas: find the index of the maximum and minimum values
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Minimum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmin())

print("\n----------- Maximum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmax())

# loading & writing json file from/to local
with open('data.json', ) as f:
    data_json = json.load(f)

d = {
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}

with open('sample.json', 'w') as f:
    json.dump(d, f)

url = "https://api.gdax.com/products/BTC-EUR/ticker"
data3 = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data3)

# output some object attributes
print('$ ' + obj['price'])
print('$ ' + obj['volume'])


