import pandas as pd

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/files/athlete_events.csv')

data.drop('ID', axis = 1, inplace = True)
data.drop('Season', axis = 1, inplace = True)
data.drop('NOC', axis = 1, inplace = True)

print(data.head())