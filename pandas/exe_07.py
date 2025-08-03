import pandas as pd

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/pandas/files/athlete_events.csv')

data.rename(columns={'Name':'Athlete', 'Team':'Country'},  # Rename Columns
            inplace=True)

print(data)

print('-----------------------------------')

height = data['Height']
print(height)

print('-----------------------------------')

print(data['Medal'].value_counts()) 

print('-----------------------------------')
