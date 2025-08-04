import pandas as pd

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/files/athlete_events.csv')

data2 = data.dropna() # Drop lines with n/a 

is_null = data.isnull()

missing = data.isnull().sum()
missing_perc = (data.isnull().sum() / len(data['ID'])) * 100

data['Medal'].fillna('None', inplace = True)
data['Age'].fillna(data['Age'].mean(), inplace = True)
data['Height'].fillna(data['Height'].mean(), inplace = True)
data['Weight'].fillna(data['Weight'].mean(), inplace = True)